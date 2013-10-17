from trove.guestagent.manager.base_manager import BaseManager

from testtools import TestCase, ExpectedException


class BaseManagerTest(TestCase):
    """
    Tests the BaseManager class 
    """
    def setUp(self):
        """
        Setup by instantiating the BaseManager class.
        """
        super(BaseManagerTest, self).setUp()
        self.manager = BaseManager()

    def tearDown(self):
        """
        No Tear Down Used yet.
        """
        super(BaseManagerTest, self).tearDown()

    def test_update_status(self):
        """
        Tests update_status We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'update_status not implemented.'):
            self.manager.update_status('')

    def test_change_passwords(self):
        """
        Tests change_passwords We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'change_passwords not implemented.'):
            self.manager.change_passwords('', '')

    def test_update_attributes(self):
        """
        Tests update_attributes We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'update_attributes not implemented.'):
            self.manager.update_attributes('', '', '', '')

    def test_reset_configuration(self):
        """
        Tests reset_configuration We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'reset_configuration not implemented.'):
            self.manager.reset_configuration('', '')

    def test_create_database(self):
        """
        Tests create_database We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'create_database not implemented.'):
            self.manager.create_database('', '')

    def test_create_user(self):
        """
        Tests create_user We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'create_user not implemented.'):
            self.manager.create_user('', '')

    def test_delete_database(self):
        """
        Tests delete_database We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'delete_database not implemented.'):
            self.manager.delete_database('', '')

    def test_delete_user(self):
        """
        Tests delete_user We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'delete_user not implemented.'):
            self.manager.delete_user('', '')

    def test_get_user(self):
        """
        Tests get_user We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'get_user not implemented.'):
            self.manager.get_user('', '', '')

    def test_grant_access(self):
        """
        Tests grant_access We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'grant_access not implemented.'):
            self.manager.grant_access('', '', '', '')

    def test_revoke_access(self):
        """
        Tests revoke_access We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'revoke_access not implemented.'):
            self.manager.revoke_access('', '', '', '')

    def test_list_access(self):
        """
        Tests list_access We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'list_access not implemented.'):
            self.manager.list_access('', '', '')

    def test_list_databases(self):
        """
        Tests list_databases We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'list_databases not implemented.'):
            self.manager.list_databases('', '', '', '')

    def test_list_users(self):
        """
        Tests list_users We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'list_users not implemented.'):
            self.manager.list_users('', '', '', '')

    def test_enable_root(self):
        """
        Tests enable_root We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'enable_root not implemented.'):
            self.manager.enable_root('')

    def test_is_root_enabled(self):
        """
        Tests is_root_enabled We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'is_root_enabled not implemented.'):
            self.manager.is_root_enabled('')

    def test_perform_restore(self):
        """
        Tests _perform_restore We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, '_perform_restore not implemented.'):
            self.manager._perform_restore('', '', '', '')

    def test_prepare(self):
        """
        Tests prepare We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'prepare not implemented.'):
            self.manager.prepare('', '', '', '', '', '', '', '')

    def test_enable_root(self):
        """
        Tests restart We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'restart not implemented.'):
            self.manager.restart('')

    def start_db_with_conf_changes(self):
        """
        Tests start_db_with_conf_changes We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'start_db_with_conf_changes not implemented.'):
            self.manager.start_db_with_conf_changes('', '')

    def stop_db(self):
        """
        Tests stop_db We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'stop_db not implemented.'):
            self.manager.stop_db('', '')

    def test_filesystem_stats(self):
        """
        Tests get_filesystem_stats We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'get_filesystem_stats not implemented.'):
            self.manager.get_filesystem_stats('', '')

    def test_create_backup(self):
        """
        Tests create_backup We want to raise a NotImplementedError.
        """
        with ExpectedException(NotImplementedError, 'create_backup not implemented.'):
            self.manager.create_backup('', '')

