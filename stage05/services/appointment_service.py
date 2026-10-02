from domain.appointment import Appointment


class AppointmentService:
    def __init__(self, appointment_repository):
        self.appointment_repository = appointment_repository

    def create_appointment(
        self,
        appointment_id: str,
        patient,
        practitioner,
    ) -> Appointment:
        appointment = Appointment(
            appointment_id,
            patient,
            practitioner,
        )
        self.appointment_repository.save(appointment)
        return appointment

    def cancel_appointment(self, appointment_id: str) -> Appointment:
        appointment = self.appointment_repository.find_by_id(
            appointment_id
        )
        if appointment is None:
            raise ValueError("Appointment not found")
        appointment.cancel()
        self.appointment_repository.save(appointment)
        return appointment
