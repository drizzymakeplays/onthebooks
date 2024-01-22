from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
# from models.appointments import AppointmentIn, AppointmentOut
# from queries.appointments import AppointmentQueries


router = APIRouter()

@router.get("/api/appointments/")
async def get_all_appointments():
    pass


@router.get("/api/appointments/{id}")
async def get_appointment():
    pass


@router.post("/api/appointments/book-appointment/")
async def create_appointment():
    pass
#     apt: AppointmentIn, repo: AppointmentQueries = Depends()
# ):
#     apt = repo.create(apt)
#     return apt


@router.delete("/api/appointments/cancel-appointment/{id}")
async def cancel_appointment():
    pass


@router.put("/api/appointments/update-appointment/{id}")
async def update_appointment():
    pass
