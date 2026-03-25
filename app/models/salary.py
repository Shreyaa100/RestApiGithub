from dataclasses import dataclass

@dataclass
class Salary:
    id: str
    employee_id: str
    basic_salary: float
    bonus: float
    allowances: float