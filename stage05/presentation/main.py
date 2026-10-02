import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from domain.patient import Patient
from domain.practitioner import Practitioner
from services.appointment_service import AppointmentService
from persistence.in_memory_appointment_repository import (
    InMemoryAppointmentRepository,
)


def main():
    repository = InMemoryAppointmentRepository()
    service = AppointmentService(repository)
    patient = Patient(
        "P001",
        "John Smith",
    )
    practitioner = Practitioner(
        "PR001",
        "Dr Sarah Lee",
        "General Practice",
    )
    appointment = service.create_appointment(
        "A001",
        patient,
        practitioner,
    )
    print("Appointment created:")
    print(appointment.get_information())
    cancelled_appointment = service.cancel_appointment("A001")
    print("\nAppointment cancelled:")
    print(cancelled_appointment.get_information())


if __name__ == "__main__":
    main()
