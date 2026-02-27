import pytest
from unittest.mock import MagicMock, patch
from app.services.task_service import TaskService

@patch('app.services.task_service.TaskRepository')
class TestTaskService:


    # CREATE TASK
    def test_create_task_success(self, mock_repo):
        data = {
                    "title" : "task 1",
                    "description" : "task1 description",
                    "user_id": 1
                }
        mock_task = MagicMock()
        mock_task.title = data['title']
        mock_repo.create_task.return_value = mock_task

        result = TaskService.create_task(data)
        assert result.title == "task 1"
        mock_repo.create_task.assert_called_once_with(data)

    def test_create_task_validation_error(self, mock_repo):
        with pytest.raises(ValueError) as exc:
            TaskService.create_task({"title" : "",
                    "description" : "task1 description",
                    "user_id": 0})
        assert "title is required" in str(exc.value).lower()



    def test_create_task_user_not_found(self, mock_task_repo):
        """Tes error jika user_id tidak terdaftar di database"""
        # data
        data = {"title": "Task Baru", "description" : "task1 description","user_id": 99}
        
        mock_task_repo.check_user.return_value = False

        with pytest.raises(ValueError) as exc:
            TaskService.create_task(data)
        
        assert "user dengan id tersebut tidak di temukan" in str(exc.value).lower()
        # Pastikan create_task di repo tidak terpanggil
        mock_task_repo.create_task.assert_not_called()

    # GET TASK
    def test_get_all_task(self, mock_repo):
        mock_repo.get_all_task.return_value = [MagicMock(), MagicMock()]

        result = TaskService.get_all_task()
        assert len(result) == 2
        mock_repo.get_all_task.assert_called_once()

    def test_get_single_task(self, mock_repo):
        mock_task = MagicMock()
        mock_task.id = 1
        mock_repo.get_task_by_id.return_value = mock_task

        result = TaskService.get_task(1)
        assert result.id == 1
        mock_repo.get_task_by_id.assert_called_with(1)

    # DELETE TASK
    def test_delete_task_success(self, mock_repo):
        mock_task = MagicMock()
        mock_repo.get_task_by_id.return_value = mock_task

        result = TaskService.delete_task(1)
        assert result == mock_task
        mock_repo.delete_task.assert_called_with(mock_task)

    def test_delete_user_not_found(self, mock_repo):
        mock_repo.get_task_by_id.return_value = None

        result = TaskService.delete_task(99)
        assert result is None
        mock_repo.delete_task.assert_not_called()

    # UPDATE TASK
    def test_update_task_success(self, mock_repo):
        mock_task = MagicMock()
        mock_task.title = "task1"
        mock_task.status = "Complete"
        mock_repo.get_task_by_id.return_value = mock_task

        data_update =   {
                            "title" : "task1",
                            "description" : "task1 description",
                            "status" : "Complete",
                            "user_id": 1
                        }
        
        mock_repo.update_task.return_value = mock_task

        result = TaskService.update_task(1, data_update)

        assert mock_task.title == "task1"
        assert mock_task.status == "Complete"
        assert mock_task.description == "task1 description"

        mock_repo.update_task.assert_called_once()

    def test_update_task_not_found(self, mock_repo):
        mock_repo.get_task_by_id.return_value = None
        with pytest.raises(ValueError) as exc:
            TaskService.update_task(99, {'title' : 'task1'})
        assert "task not found" in str(exc.value).lower()

    def test_update_task_validation_error(self, mock_repo):
        with pytest.raises(ValueError) as exc:
            TaskService.update_task(1, {"title" : "",
                    "description" : "task1 description",
                    "user_id": 1})
        assert "title cannot be empty" in str(exc.value).lower()


    # GET RELATION
    def test_get_tasks_by_user_success(self, mock_task_repo):
        user_id = 1
        # Mocking: Simulasikan user ditemukan
        mock_task_repo.check_user.return_value = True
        
        # Mocking: Simulasikan daftar task yang dikembalikan
        mock_tasks = [MagicMock(), MagicMock()]
        mock_task_repo.get_by_user_id.return_value = mock_tasks

        result = TaskService.get_tasks_by_user(user_id)

        assert len(result) == 2
        mock_task_repo.check_user.assert_called_once_with(user_id)
        mock_task_repo.get_by_user_id.assert_called_once_with(user_id)

    def test_get_tasks_by_user_not_found(self, mock_task_repo):

        user_id = 999
        # Mocking: Simulasikan user TIDAK ditemukan
        mock_task_repo.check_user.return_value = False

        result = TaskService.get_tasks_by_user(user_id)

        assert result is None
        # Pastikan get_by_user_id tidak dipanggil jika user tidak ada
        mock_task_repo.get_by_user_id.assert_not_called()

