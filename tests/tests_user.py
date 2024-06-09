import unittest
from unittest.mock import MagicMock
from user.user_services import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para cada teste
        self.user_dao_mock = MagicMock()
        self.user_service = UserService()
        self.user_service.user_dao = self.user_dao_mock

    def test_create_user(self):
        # Testa o método create_user
        user_data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
        self.user_service.create_user(user_data)
        self.user_dao_mock.create_user.assert_called_once_with(user_data)

    def test_get_user_by_id(self):
        # Testa o método get_user_by_id
        user_id = 1
        self.user_service.get_user_by_id(user_id)
        self.user_dao_mock.get_user_by_id.assert_called_once_with(user_id)

    def test_get_all_users(self):
        # Testa o método get_all_users
        self.user_service.get_all_users()
        self.user_dao_mock.get_all_users.assert_called_once()

    def test_delete_user(self):
        # Testa o método delete_user
        user_id = 1
        self.user_service.delete_user(user_id)
        self.user_dao_mock.delete_user.assert_called_once_with(user_id)

    def test_update_user(self):
        # Testa o método update_user
        user_data = {"id": 1, "name": "Alice", "email": "alice@example.com"}
        self.user_service.update_user(user_data)
        self.user_dao_mock.update_user.assert_called_once_with(user_data)

if __name__ == "__main__":
    unittest.main()
