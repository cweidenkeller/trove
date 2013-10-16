import os
import os.path
from trove.common import cfg
from trove.common import instance as rd_instance
from trove.common import utils
from trove.common.exception import ProcessExecutionError
from trove.instance import models as rd_models
from trove.guestagent import dbaas
from trove.guestagent import backup
from trove.guestagent import volume
from trove.openstack.common import log as logging
from trove.openstack.common.gettextutils import _
from trove.openstack.common import periodic_task


LOG = logging.getLogger(__name__)
CONF = cfg.CONF
MOUNT_POINT = '/var/lib/redis'
CONFIG_FILE = '/etc/redis/redis.conf'
CONFIG_PATH = '/etc/redis'
TMP_CONFIG_PATH = '/tmp/redis.conf'
TMP_PATH = '/tmp'
SERVICE_PATH = '/etc/init.d/redis-server'
RCD_CMD = 'update-rc.d'
SERVICE_NAME = 'redis-server'


class Manager(periodic_task.PeriodicTasks):
    _status = None
    _pending_status = None
    guest_id = CONF.guest_id

    def _initialize_status(self):
        """
        Check to see if self.status is set.
        """
        status = rd_models.InstanceServiceStatus.find_by(
            instance_id=self.guest_id)
        self._status = status.status
        self._pending_status = status.status

    @periodic_task.periodic_task(ticks_between_runs=3)
    def update_status(self, context):
        """Update the status of the Redis service"""
        LOG.info(_('Updating Redis Status'))
        if not self._status:
            self._initialize_status()
        if self._status != self._pending_status:
            db_status = rd_models.InstanceServiceStatus.find_by(instance_id=
                                                                self.guest_id)
            db_status.status = status
            db_status.save()
            self._status = self._pending_status

    def prepare(self, context, databases, memory_mb, users, device_path=None,
                mount_point=None, backup_id=None, config_contents=None,
                root_password=None):
        """
        Sets up the base redis instance and ensures the mount points are
        all set correctly.
        """
        LOG.info(_('Inside Redis prepare call'))
        self._pending_status = rd_instance.ServiceStatuses.BUILDING
        try:
            utils.execute_with_timeout('mkdir',
                                       '-p',
                                       MOUNT_POINT,
                                       run_as_root=True,
                                       root_helper='sudo')

            utils.execute_with_timeout('chown',
                                       'redis:redis',
                                       MOUNT_POINT,
                                       run_as_root=True,
                                       root_helper='sudo')

            if not os.path.isdir(CONFIG_PATH):
                utils.execute_with_timeout('mkdir',
                                           '-p',
                                           CONFIG_PATH,
                                           run_as_root=True,
                                           root_helper='sudo')
            else:
                if os.path.isfile(CONFIG_FILE):
                    utils.execute_with_timeout('rm',
                                               CONFIG_FILE,
                                               run_as_root=True,
                                               root_helper='sudo')
            if not os.path.isdir(TMP_PATH):
                utils.execute_with_timeout('mkdir',
                                           '-p',
                                           TMP_PATH,
                                           run_as_root=True,
                                           root_helper='sudo')
            else:
                if os.path.isfile(TMP_CONFIG_PATH):
                    utils.execute_with_timeout('rm',
                                               TMP_CONFIG_PATH,
                                               run_as_root=True,
                                               root_helper='sudo')
        except ProcessExecutionError:
            LOG.ERROR(_("Unable to bootstrap base instance."))
            self._pending_status = rd_instance.ServiceStatuses.FAILED
            return
        with open(TMP_CONFIG_PATH, 'w') as fd:
            fd.write(config_contents)
        try:
            utils.execute_with_timeout('mv',
                                       TMP_CONFIG_PATH,
                                       CONFIG_FILE,
                                       run_as_root=True,
                                       root_helper='sudo')
            utils.execute_with_timeout(SERVICE_PATH,
                                       'restart',
                                       run_as_root=True,
                                       root_helper='sudo')
        except ProcessExecutionError:
            LOG.ERROR(_("Unable to bootstrap base instance."))
            self._pending_status = rd_instance.ServiceStatuses.FAILED
            return
        if device_path:
            device = volume.VolumeDevice(device_path)
            device.format()
            device.mount(MOUNT_POINT)
            LOG.debug(_('Mounted the volume.'))
        self._pending_status = rd_instance.ServiceStatuses.RUNNING

    def restart(self, context):
        """
        Restarts the redis-server instace.
        """
        try:
            utils.execute_with_timeout(SERVICE_PATH,
                                       'restart',
                                       run_as_root=True,
                                       root_helper='sudo')
        except ProcessExecutionError:
            LOG.ERROR(_("Unable to restart redis instance."))
            self._pending_status = rd_instance.ServiceStatuses.CRASHED

    def stop_db(self, context, do_not_start_on_reboot=False):
        """
        Stops the redis-server instance.
        """
        try:
            utils.execute_with_timeout(SERVICE_PATH,
                                       'stop',
                                       run_as_root=True,
                                       root_helper='sudo')
            if do_not_start_on_reboot:
                utils.execute_with_timeout(RCD_COMMAND,
                                           SERVICE_NAME,
                                           'disable',
                                           run_as_root=True,
                                           root_helper='sudo')
        except ProcessExecutionError:
            LOG.ERROR(_("Unable to stop redis instance."))
            self._pending_status = rd_instance.ServiceStatuses.CRASHED
            return
        self._pending_status = rd_instance.ServiceStatuses.SHUTDOWN
