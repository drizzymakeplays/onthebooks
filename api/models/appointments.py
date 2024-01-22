from pydantic import BaseModel, validator
from datetime import datetime, date


# class Error(BaseModel):
#     message: str


# class AppointmentIn(BaseModel):
#     patient_id: int
#     hcp_id: int
#     appt_date: str
#     appt_time: str
#     appt_reason: str
#     status: bool

#     @validator("appt_date")
#     def parse_dob(cls, v):
#         return datetime.strptime(v, "%m-%d-%Y").date()


# class AppointmentOut(BaseModel):
#     id: int
#     patient_id: int
#     hcp_id: int
#     appt_date: date
#     appt_time: str
#     appt_reason: str
#     status: bool
