"""
Salary service – business logic for salaries.
"""
import uuid

from app.models.salary import Salary
from app.repositories.json_repository import JsonRepository


class SalaryService:
    def __init__(self, repo: JsonRepository[Salary]) -> None:
        self._repo = repo

    def create_salary(self, data: dict) -> dict:
        salary = Salary(
            id=str(uuid.uuid4()),
            employee_id=data["employee_id"],
            basic_salary=data["basic_salary"],
            bonus=data["bonus"],
            allowances=data["allowances"],
        )
        self._repo.create(salary)
        return salary.to_dict()

    def get_salary_by_employee(self, employee_id: str) -> list[dict]:
        salaries = self._repo.get_by_field("employee_id", employee_id)
        return [s.to_dict() for s in salaries]