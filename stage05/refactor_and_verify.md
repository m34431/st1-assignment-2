# SmartCare v0.5 – Refactor and Verification

## Refactoring Decisions

SmartCare was refactored from the v0.4 domain implementation into a simple layered architecture.

The following layers were introduced:

- Presentation
- Service
- Domain
- Repository
- Persistence

### Changes Made

1. Appointment workflow coordination was moved into AppointmentService.

2. Appointment domain behaviour remained inside the Appointment class.

3. An AppointmentRepository abstraction was introduced for data-access operations.

4. An InMemoryAppointmentRepository was created to provide simple appointment storage.

5. Presentation responsibilities were separated from domain and persistence responsibilities.

6. No unnecessary frameworks, microservices or complex design patterns were introduced.

## Verification

The refactored SmartCare v0.5 system was tested to confirm that existing behaviour remained unchanged.

The following behaviour was verified:

- A Patient can be created.
- A Practitioner can be created.
- An Appointment can be created.
- A new Appointment begins with SCHEDULED status.
- The Appointment can be stored using the repository.
- An Appointment can be found using its appointment ID.
- AppointmentService can coordinate appointment creation.
- AppointmentService can coordinate appointment cancellation.
- Appointment.cancel() still controls the status transition.
- A cancelled appointment remains stored as an object.
- The appointment status changes from SCHEDULED to CANCELLED.

## Result

The required SmartCare behaviour continued to work after refactoring.

The layered architecture improved separation of concerns without changing the core domain behaviour.
