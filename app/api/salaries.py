from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.models.salary import Salary
from app.repositories.json_repository import JsonRepository
from app.services.salary_service import SalaryService

salaries_bp = Blueprint("salaries", __name__)

repo = JsonRepository("data/salaries.json", Salary)
service = SalaryService(repo)


@salaries_bp.route("/api/v1/salaries", methods=["POST"])
@jwt_required()
def create_salary():
    data = request.get_json()
    salary = service.create_salary(data)
    return jsonify(salary), 201


@salaries_bp.route("/api/v1/salaries/employee/<employee_id>", methods=["GET"])
@jwt_required()
def get_salary_by_employee(employee_id):
    salaries = service.get_salary_by_employee(employee_id)
    return jsonify(salaries), 200