from pydantic import BaseModel
from typing import Dict

class WheelFormBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Dict[str, str]

class WheelFormCreate(WheelFormBase):
    pass

class WheelFormResponse(BaseModel):
    success: bool
    message: str
    data: dict
