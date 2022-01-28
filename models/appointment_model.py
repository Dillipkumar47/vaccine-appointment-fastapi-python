import datetime
from typing import List

from pydantic import BaseModel


class AppointmentSubmittal(BaseModel):
    name: str
    dose: int
    appoint_time: datetime.datetime


class Appointment(AppointmentSubmittal):
    id: str
    date_created: datetime.datetime

