# Stage 5 Reflection

The architecture review supported separating presentation, workflow coordination, domain behaviour and persistence. I accepted the recommendation to keep the appointment status transition inside `Appointment`. `AppointmentService` calls `appointment.cancel()` and saves the result, while the domain object controls the transition from `SCHEDULED` to `CANCELLED`.

I modified the repository suggestion to keep the contract as small as the current use cases require. `AppointmentService` receives a repository through its constructor and uses only `save()` and `find_by_id()`. The in-memory implementation satisfies that contract. I did not add extra repository operations or introduce a dependency-injection framework.

I rejected and deferred the suggestion to use microservices, an event bus, many additional interfaces or a dependency-injection framework. This application has one small appointment workflow, and those additions would increase complexity without meeting a current requirement. I also kept persistence in memory because database storage is not needed to demonstrate the architecture.

The presentation script initially could not import the sibling Stage 5 packages when run with the handout's direct-script command. I added a small path setup in the presentation entry point so `python3 presentation/main.py` works from `stage05`. I reran the program and confirmed that it prints the appointment as `Scheduled` and then `Cancelled`.

This review reinforced that AI suggestions need to be checked against the code and assignment requirements. I kept the changes that protected domain behaviour and clarified the layers, and left out patterns that the current system does not need.
