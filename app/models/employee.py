from dataclasses import dataclass

@dataclass
class Employee:
    id: str
    first_name: str
    last_name: str
    gender: str
    date_of_birth: str
    department_id: str