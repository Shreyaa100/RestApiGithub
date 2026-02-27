from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.models.department import Department
from app.repositories.json_repository import JsonRepository
from app.services.department_service import DepartmentService

departments_bp = Blueprint("departments", __name__)

repo = JsonRepository("data/departments.json", Department)
service = DepartmentService(repo)


@departments_bp.route("/api/v1/departments", methods=["POST"])
@jwt_required()
def create_department():
    data = request.get_json()
    department = service.create_department(data)
    return jsonify(department), 201


@departments_bp.route("/api/v1/departments", methods=["GET"])
@jwt_required()
def list_departments():
    return jsonify(service.list_departments()), 200