from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient,
        practitioner,
    ):
        if not appointment_id or not appointment_id.strip():
            raise ValueError("appointment_id cannot be empty")
        if patient is None:
            raise ValueError("patient cannot be empty")
        if practitioner is None:
            raise ValueError("practitioner cannot be empty")

        self.appointment_id = appointment_id.strip()
        self.patient = patient
        self.practitioner = practitioner
        # New appointments always begin as scheduled.
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def get_information(self) -> str:
        return (
            f"Appointment ID: {self.appointment_id}, "
            f"Patient: {self.patient.name}, "
            f"Practitioner: {self.practitioner.name}, "
            f"Status: {self._status.value}"
        )

    def cancel(self) -> None:
        # Cancelled appointments remain as objects, as required.
        self._status = AppointmentStatus.CANCELLED
