# SmartCare v0.4 – UML Review

## Domain Classes

### Patient

Attributes:

- patient_id: str
- name: str

Responsibilities:

- Store patient identification and name.
- Validate basic patient information.
- Provide patient information when required.

### Practitioner

Attributes:

- practitioner_id: str
- name: str
- specialty: str

Responsibilities:

- Store practitioner identification, name and specialty.
- Validate basic practitioner information.
- Represent a practitioner in the SmartCare domain.
- Does not contain database logic.

### Appointment

Attributes:

- appointment_id: str
- patient: Patient
- practitioner: Practitioner
- status: AppointmentStatus

Responsibilities:

- Represent an appointment between a Patient and Practitioner.
- Maintain the appointment's current status.
- Allow a scheduled appointment to be cancelled.
- Protect appointment status from invalid transitions.
- Retain cancelled appointments rather than deleting them.

## Relationships

- A Patient can be associated with appointments.
- A Practitioner can be associated with appointments.
- Each Appointment is associated with a Patient.
- Each Appointment is associated with a Practitioner.
- Appointment uses composition/association rather than inheritance
  with Patient and Practitioner.

## Appointment Status

The current implementation uses:

- SCHEDULED
- CANCELLED

A new appointment begins with SCHEDULED status.

The valid transition currently implemented is:

SCHEDULED -> CANCELLED

A CANCELLED appointment cannot be cancelled again.

## Design Constraints

The domain classes should contain domain behaviour only.

They should not contain:

- Database or SQL logic
- User interface logic
- Notification logic
- Service-layer logic

The implementation should remain simple and consistent with the
approved SmartCare domain design.
