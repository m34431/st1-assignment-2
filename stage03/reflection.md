# Stage 3 Reflection

The hardest modelling decision was deciding which concepts should become classes and which should stay as attributes or responsibilities. Patient, Practitioner, and Appointment were clear choices because they are directly supported by the functional requirements.

Status and Appointment History were less straightforward. I kept status as an attribute of Appointment because FR-07 only requires the system to record an appointment status. I also decided not to create a separate AppointmentHistory class because FR-08 requires history to be retained but does not say that it needs its own class.

The AI review helped identify assumptions in my original model. Patient ID, practitioner ID, appointment ID, and name seemed like sensible attributes, but the requirements do not define exactly what information must be stored. I therefore marked these attributes as provisional and left them open for client validation.

The review also showed that `Practitioner.get_information()` was not directly supported. FR-03 requires practitioner information to be recorded, but it does not explicitly require it to be retrieved. I removed this operation from the final model and the Python skeleton.

My final decisions were based on tracing the model back to FR-01 through FR-10. I used the AI suggestions when they were supported by the requirements and rejected ideas that would add functionality without clear evidence. The final diagram now shows the three classes, their main attributes and methods, and the one-to-many relationships between appointments and patients or practitioners.
