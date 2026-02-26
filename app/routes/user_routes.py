from flask import Blueprint, request
from app.services.suser_service import UserServices
from app.utils.response import success_response, error_response
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


user_blueprint = Blueprint("users", __name__)

@user_blueprint.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = UserServices.create_user(data)
        return success_response(
            {
            "id" : user.id,
            "name" : user.name,
            "email" : user.email
            }, "user created", 201
        )
    except IntegrityError:
        return error_response("Email already exists", 409)
    except SQLAlchemyError:
        return error_response("Database error", 500)
    
    # user  = UserServices.create_user(data)

    # if error:
    #     return error_response(error)
    
    # return success_response({
    #     "id" : user.id,
    #     "name" : user.name,
    #     "email" : user.email
    # }, "user created", 201)


@user_blueprint.route("/users", methods=['GET'])
def get_users():
    users = UserServices.get_all_users()

    result = [
        {
        "id" : u.id,
        "name" : u.name,
        "email" : u.email
        } for u in users
    ]

    return success_response(result)

@user_blueprint.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = UserServices.get_user(user_id)

    if not user:
        return error_response("user not found", 404)
    
    return success_response({
        "id" : user.id,
        "name" : user.name,
        "email" : user.email
    })


@user_blueprint.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    user = UserServices.delete_user(user_id)
    
    if not user:
        return error_response("user not found", 404)
    
    return success_response({
    "id": user.id,
    "name": user.name
}, "User deleted")