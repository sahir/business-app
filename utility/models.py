# Models
from pydantic import BaseModel
from datetime import date

# Pydantic schema definition
class BusinessCreateModel(BaseModel):
    name: str
    legal_name: str = ""
    address: str = ""
    owner_info: str = ""
    employee_size: int = 0
    founded_date: date = date.today()
    founders: str = ""
    last_funding_type: str = ""
    phone_number: str = ""
    contact_email: str = ""

class BusinessModel(BaseModel):
    id: int
    name: str
    legal_name: str
    address: str
    owner_info: str
    employee_size: int
    founded_date: date
    founders: str
    last_funding_type: str
    phone_number: str
    contact_email: str