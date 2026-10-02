from domain.patient import Patient
from domain.practitioner import Practitioner
from domain.appointment import Appointment

patient = Patient("P001", "John Smith")
practitioner = Practitioner(
    "PR001",
    "Dr Sarah Lee",
    "General Practice",
)
appointment = Appointment(
    "A001",
    patient,
    practitioner,
)
print(appointment.get_information())

print("\n--- Cancellation Test ---")
appointment.cancel()
print("After cancellation:")
print(appointment.get_information())

print("\n--- Invalid Patient Test ---")
try:
    invalid_patient = Patient("", "")
except ValueError as error:
    print("Expected error:", error)

print("\n--- Invalid Practitioner Test ---")
try:
    invalid_practitioner = Practitioner(
        "",
        "",
        "",
    )
except ValueError as error:
    print("Expected error:", error)

print("\n--- Invalid Appointment Test ---")
try:
    invalid_appointment = Appointment(
        "",
        patient,
        practitioner,
    )
except ValueError as error:
    print("Expected error:", error)
