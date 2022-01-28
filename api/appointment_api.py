from typing import List
from services import appointment_service as aps
import fastapi
from fastapi import Depends

from models.appointment_model import Appointment, AppointmentSubmittal

router = fastapi.APIRouter()


# @router.get('/api/appointments/{name}')
# def appointments(aptmt: Appointment = Depends()):
#     return f"{aptmt.name}'s appointment for dose  {apmt.dose} is schedules at  {apmt.appoint_time}"

@router.get('/api/appointments', name='Get scheduled appointments', response_model=List[Appointment])
async def get_appointments() -> List[Appointment]:
    return await aps.get_all_appointments()


@router.post('/api/appointments', name='Book an Appointment', response_model=Appointment)
async def appointment_post(aptmt:AppointmentSubmittal)-> Appointment:
    return await aps.book_appointment(aptmt)


