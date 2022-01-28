import datetime
import uuid
from typing import List

from models.appointment_model import AppointmentSubmittal, Appointment

__aptmt: List[Appointment] = []


# async def get_apmt()
async def get_all_appointments():
    appointments = __aptmt
    return appointments


async def book_appointment(aptmt: Appointment):
    created_time = datetime.datetime.now()
    appointment = Appointment(id=str(uuid.uuid4()),
                              date_created=created_time,
                              name=aptmt.name,
                              dose=aptmt.dose,
                              appoint_time=aptmt.appoint_time)
    # print(appointment)
    __aptmt.append(appointment)
    __aptmt.sort(key=lambda a: a.date_created, reverse=True)
    return appointment
