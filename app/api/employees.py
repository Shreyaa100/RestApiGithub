from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.models.employee import Employee
from app.repositories.json_repository import JsonRepository
from app.services.employee_service import EmployeeService

employees_bp = Blueprint("employees", __name__)

repo = JsonRepository("data/employees.json", Employee)
service = EmployeeService(repo)


@employees_bp.route("/api/v1/employees", methods=["POST"])
@jwt_required()
def create_employee():
    data = request.get_json()
    employee = service.create_employee(data)
    return jsonify(employee), 201


@employees_bp.route("/api/v1/employees", methods=["GET"])
@jwt_required()
def list_employees():
    return jsonify(service.list_employees()), 200


@employees_bp.route("/api/v1/employees/<employee_id>", methods=["GET"])
@jwt_required()
def get_employee(employee_id):
    employee = service.get_employee(employee_id)
    if employee is None:
        return jsonify({"message": "Employee not found"}), 404
    return jsonify(employee), 200


@employees_bp.route("/api/v1/employees/<employee_id>", methods=["PUT"])
@jwt_required()
def update_employee(employee_id):
    data = request.get_json()
    employee = service.update_employee(employee_id, data)
    if employee is None:
        return jsonify({"message": "Employee not found"}), 404
    return jsonify(employee), 200


@employees_bp.route("/api/v1/employees/<employee_id>", methods=["DELETE"])
@jwt_required()
def delete_employee(employee_id):
    deleted = service.delete_employee(employee_id)
    if not deleted:
        return jsonify({"message": "Employee not found"}), 404
    return jsonify({"message": "Employee deleted"}), 200