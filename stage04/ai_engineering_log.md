# SmartCare v0.4 – AI Engineering Log

## AI Prompt

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

## AI Generated Contribution

AI was used to assist with the implementation of the Appointment class and AppointmentStatus enum.

The generated implementation included:

- Appointment ID validation.
- References to a Patient and Practitioner.
- AppointmentStatus enum.
- SCHEDULED and CANCELLED statuses.
- A protected `_status` attribute.
- A `cancel()` method.
- A `get_information()` method.
- Validation to prevent an appointment from being cancelled more than once.

AI was not used to implement the Patient or Practitioner classes.

## Review of AI Contribution

The generated code was reviewed against the approved SmartCare domain design.

The implementation did not introduce:

- Database or SQL logic.
- User interface logic.
- Notification logic.
- Service classes.
- Unnecessary inheritance.
- Unnecessary external dependencies.

The AI implementation assumed that a newly created appointment starts with the SCHEDULED status.

This decision was accepted because it supports the required SCHEDULED to CANCELLED transition while keeping the implementation simple.

## Modifications and Decisions

The AI-generated solution was kept simple and limited to the Appointment domain class.

Public modification of appointment status was not allowed. The `_status` attribute is protected and status changes are performed through the `cancel()` method.

No database, UI, notification or service functionality was added because these responsibilities do not belong in the domain class.

No unnecessary inheritance was introduced.

## Verification Evidence

The implementation was manually tested.

The following checks were performed:

1. A valid Patient object was created.
2. A valid Practitioner object was created.
3. A valid Appointment object was created.
4. A new appointment displayed SCHEDULED status.
5. The appointment was successfully cancelled.
6. The appointment remained as an object after cancellation.
7. The status changed from SCHEDULED to CANCELLED.
8. A second cancellation attempt raised a ValueError.
9. Invalid Patient input raised a ValueError.
10. Invalid Practitioner input raised a ValueError.
11. Invalid Appointment input raised a ValueError.

These tests confirmed that the basic domain behaviour and protected status transition worked as expected.

## Reflection

The most useful AI-generated part was the protected appointment status transition.

I retained the use of the AppointmentStatus enum and the `cancel()` method because they keep status changes controlled by the Appointment class.

I rejected adding any unnecessary database, UI, notification or service functionality because these features were outside the approved domain design.

The approved UML and the task constraints helped limit the AI contribution and prevented unnecessary features from being added.
