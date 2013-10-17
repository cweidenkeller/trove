from trove.common import cfg
from trove.openstack.common import log as logging
from trove.openstack.common.gettextutils import _

LOG = logging.getLogger(__name__)
CONF = cfg.CONF


class BaseManager():
    """
    Base manager class to hold base impl and db specific calls.
    This allows for other DB types that don't support users perhaps...
    To implement a Manager class without having to have implementation
    for unsupported calls.
    """
    def update_status(self, context):
        """
        Base update_status.
        """
        LOG.info(_('update_status not implemented.'))
        raise NotImplementedError('update_status not implemented.')

    def change_passwords(self, context, users):
        """
        Base change_passwords.
        """
        LOG.info(_('change_passwords not implemented.'))
        raise NotImplementedError('change_passwords not implemented.')

    def update_attributes(self, context, username, hostname, user_attrs):
        """
        Base update_attributes.
        """
        LOG.info(_('update_attributes not implemented.'))
        raise NotImplementedError('update_attributes not implemented.')

    def reset_configuration(self, context, configuration):
        """
        Base reset_configuration.
        """
        LOG.info(_('reset_configuration not implemented.'))
        raise NotImplementedError('reset_configuration not implemented.')

    def create_database(self, context, databases):
        """
        Base create_database.
        """
        LOG.info(_('create_database not implemented.'))
        raise NotImplementedError('create_database not implemented.')

    def create_user(self, context, users):
        """
        Base create_user.
        """
        LOG.info(_('create_user not implemented.'))
        raise NotImplementedError('create_user not implemented.')

    def delete_database(self, context, database):
        """
        Base delete_database.
        """
        LOG.info(_('delete_database not implemented.'))
        raise NotImplementedError('delete_database not implemented.')

    def delete_user(self, context, user):
        """
        Base delete_user.
        """
        LOG.info(_('delete_user not implemented.'))
        raise NotImplementedError('delete_user not implemented.')

    def get_user(self, context, username, hostname):
        """
        Base get_user.
        """
        LOG.info(_('get_user not implemented.'))
        raise NotImplementedError('get_user not implemented.')

    def grant_access(self, context, username, hostname, databases):
        """
        Base grant_access.
        """
        LOG.info(_('grant_access not implemented.'))
        raise NotImplementedError('grant_access not implemented.')

    def revoke_access(self, context, username, hostname, database):
        """
        Base revoke_access.
        """
        LOG.info(_('revoke_access not implemented.'))
        raise NotImplementedError('revoke_access not implemented.')

    def list_access(self, context, username, hostname):
        """
        Base list_access.
        """
        LOG.info(_('list_access not implemented.'))
        raise NotImplementedError('list_access not implemented.')

    def list_databases(self, context, limit=None, marker=None,
                       include_marker=False):
        """
        Base list_databases.
        """
        LOG.info(_('list_databases not implemented.'))
        raise NotImplementedError('list_databases not implemented.')

    def list_users(self, context, limit=None, marker=None,
                   include_marker=False):
        """
        Base list_users.
        """
        LOG.info(_('list_users not implemented.'))
        raise NotImplementedError('list_users not implemented.')

    def enable_root(self, context):
        """
        Base enable_root.
        """
        LOG.info(_('enable_root not implemented.'))
        raise NotImplementedError('enable_root not implemented.')

    def is_root_enabled(self, context):
        """
        Base is_root_enabled.
        """
        LOG.info(_('is_root_enabled not implemented.'))
        raise NotImplementedError('is_root_enabled not implemented.')

    def _perform_restore(self, backup_id, context, restore_location, app):
        """
        Base _perform_restore.
        """
        LOG.info(_('_perform_restore not implemented.'))
        raise NotImplementedError('_perform_restore not implemented.')

    def prepare(self, context, databases, memory_mb, users, device_path=None,
                mount_point=None, backup_id=None, config_contents=None):
        """
        Base prepare.
        """
        LOG.info(_('prepare not implemented.'))
        raise NotImplementedError('prepare not implemented.')

    def restart(self, context):
        """
        Base restart.
        """
        LOG.info(_('restart not implemented.'))
        raise NotImplementedError('restart not implemented.')

    def start_db_with_conf_changes(self, context, config_contents):
        """
        Base start_db_with_conf_changes.
        """
        LOG.info(_('start_db_with_conf_changes not implemented.'))
        raise NotImplementedError('start_db_with_conf_changes not implemented.')

    def stop_db(self, context, do_not_start_on_reboot=False):
        """
        Base stop_db.
        """
        LOG.info(_('stop_db not implemented.'))
        raise NotImplementedError('stop_db not implemented.')

    def get_filesystem_stats(self, context, fs_path):
        """
        Base get_filesystem_stats
        """
        LOG.info(_('get_filesystem_stats not implemented.'))
        raise NotImplementedError('get_filesystem_stats not implemented.')

    def create_backup(self, context, backup_id):
        """
        Base create_backup.
        """
        LOG.info(_('create_backup not implemented.'))
        raise NotImplementedError('create_backup not implemented.')

