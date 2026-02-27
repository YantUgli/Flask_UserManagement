from flask import Blueprint, request
from app.utils.response import success_response, error_response
from app.services.task_service import TaskService
from sqlalchemy.exc import SQLAlchemyError

task_blueprint = Blueprint("tasks", __name__)

@task_blueprint.route("/tasks", methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all_task()
    
    tasks_data = [task.to_dict() for task in tasks]

    return success_response(tasks_data)

@task_blueprint.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()

    try:
        task = TaskService.create_task(data)
        # return success_response({
        #     "id": task.id,
        #     "title": task.title,
        #     "description": task.description,
        #     "status": task.status,
        #     "user_id": task.user_id,
        #     "created_at": task.created_at
        # }, "task created", 201)

        return success_response(task.to_dict(), "task created", 201)

    except ValueError as e:
        return error_response(str(e), 400)
    except SQLAlchemyError:
        return error_response("Database error", 500)
    
@task_blueprint.route("/tasks/<int:task_id>", methods=['GET'])
def get_task(task_id):
    task = TaskService.get_task(task_id)

    if not task:
        return error_response("task not found", 404)
    
    return success_response(task.to_dict())

@task_blueprint.route("/tasks/<int:task_id>", methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return error_response("invalid JSON body", 400)

    try:
        task = TaskService.update_task(task_id, data)

        return success_response(task.to_dict())
    except ValueError as e:
        return error_response(str(e), 400)
    except SQLAlchemyError:
        return error_response("Database error", 500)
    

@task_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = TaskService.delete_task(task_id)

    if not task:
        return error_response("Task not Found", 404)
    
    return success_response(task.to_dict(),"task deleted")