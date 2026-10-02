# SmartCare v0.5 – Architecture Review

## Current SmartCare v0.4

SmartCare v0.4 contains the main domain classes:

- Patient
- Practitioner
- Appointment
- AppointmentStatus

The domain classes are responsible for representing clinic information and protecting basic business rules.

## Current Architecture Problems

### 1. No Service Layer

There is currently no dedicated service layer for coordinating appointment workflows.

### 2. No Repository Abstraction

There is no repository abstraction for storing and retrieving appointments.

### 3. No Persistence Layer

Data storage responsibilities have not yet been separated into a persistence layer.

### 4. Presentation and Testing

The test script directly creates and interacts with domain objects. A presentation layer should interact with a service rather than coordinate the complete workflow itself.

### 5. Separation of Responsibilities

As the system grows, workflow, data access and presentation responsibilities need to be separated from the domain model.

## Refactoring Goal

SmartCare v0.5 will use a layered architecture:

Presentation
↓
Service
↓
Domain

Service
↓
Repository abstraction
↑
Persistence

This structure will separate user interaction, workflow coordination, domain behaviour and data-access responsibilities.
