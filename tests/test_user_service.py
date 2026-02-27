import pytest
from unittest.mock import MagicMock, patch
from app.services.user_service import UserServices

@patch('app.services.user_service.UserRepository')
class TestUserService:

    # --- TEST CREATE USER ---
    def test_create_user_success(self, mock_repo):
        data = {"name": "Budi", "email": "budi@mail.com"}
        
        mock_user = MagicMock()
        mock_user.name = data["name"]
        mock_repo.create_user.return_value = mock_user

        result = UserServices.create_user(data)
        assert result.name == "Budi"
        mock_repo.create_user.assert_called_once_with(data)

    def test_create_user_validation_error(self, mock_repo):
        # Test jika name kosong
        with pytest.raises(ValueError) as exc:
            UserServices.create_user({"name": "", "email": "a@a.com"})
        assert "name and email are required" in str(exc.value).lower()

    # --- TEST GET USERS ---
    def test_get_all_users(self, mock_repo):
        mock_repo.get_all_users.return_value = [MagicMock(), MagicMock()]
        
        result = UserServices.get_all_users()
        assert len(result) == 2
        mock_repo.get_all_users.assert_called_once()

    def test_get_single_user(self, mock_repo):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_repo.get_user_by_id.return_value = mock_user

        result = UserServices.get_user(1)
        assert result.id == 1
        mock_repo.get_user_by_id.assert_called_with(1)

    # --- TEST DELETE USER ---
    def test_delete_user_success(self, mock_repo):
        mock_user = MagicMock()
        mock_repo.get_user_by_id.return_value = mock_user

        result = UserServices.delete_user(1)
        assert result == mock_user
        mock_repo.delete_user.assert_called_once_with(mock_user)

    def test_delete_user_not_found(self, mock_repo):
        mock_repo.get_user_by_id.return_value = None
        
        result = UserServices.delete_user(99)
        assert result is None
        mock_repo.delete_user.assert_not_called()

    # --- TEST UPDATE USER ---
    def test_update_user_success(self, mock_repo):
        mock_user = MagicMock()
        mock_user.name = "Old Name"
        mock_repo.get_user_by_id.return_value = mock_user
        
        data_update = {"name": "New Name", "email": "new@mail.com"}
        mock_repo.update_user.return_value = mock_user

        result = UserServices.update_user(1, data_update)
        
        assert mock_user.name == "New Name"
        assert mock_user.email == "new@mail.com"
        mock_repo.update_user.assert_called_once()

    def test_update_user_not_found(self, mock_repo):
        mock_repo.get_user_by_id.return_value = None
        with pytest.raises(ValueError) as exc:
            UserServices.update_user(99, {"name": "Test"})
        assert "user not found" in str(exc.value).lower()

    def test_update_user_empty_fields(self, mock_repo):
        mock_repo.get_user_by_id.return_value = MagicMock()
        
        # Test name empty
        with pytest.raises(ValueError) as exc:
            UserServices.update_user(1, {"name": ""})
        assert "name cannot be empty" in str(exc.value).lower()

        # Test email empty
        with pytest.raises(ValueError) as exc:
            UserServices.update_user(1, {"email": ""})
        assert "email cannot be empty" in str(exc.value).lower()