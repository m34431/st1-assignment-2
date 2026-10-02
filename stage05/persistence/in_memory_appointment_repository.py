from domain.appointment import Appointment
from repositories.appointment_repository import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self._appointments = {}

    def save(self, appointment: Appointment) -> None:
        self._appointments[appointment.appointment_id] = appointment

    def find_by_id(self, appointment_id: str) -> Appointment | None:
        return self._appointments.get(appointment_id)
