"""
Department service – business logic for departments.
"""
import uuid

from app.models.department import Department
from app.repositories.json_repository import JsonRepository


class DepartmentService:
    def __init__(self, repo: JsonRepository[Department]) -> None:
        self._repo = repo

    def list_departments(self) -> list[dict]:
        return [d.to_dict() for d in self._repo.get_all()]

    def create_department(self, data: dict) -> dict:
        department = Department(
            id=str(uuid.uuid4()),
            department_name=data["department_name"],
            location=data["location"],
        )
        self._repo.create(department)
        return department.to_dict()