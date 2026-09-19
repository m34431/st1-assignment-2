# SmartCare v0.2 Requirements

## 1. Problem and Scope

### Problem

SmartCare currently uses spreadsheets and paper records to manage clinic information. This causes problems such as duplicate bookings, difficulty finding patient information, inconsistent appointment statuses, and limited appointment history.

SmartCare v0.2 will be a small, maintainable system for managing patients, practitioners, and appointments.

### Included in This Version

- Patient information
- Practitioner information
- Appointment information
- Appointment statuses
- Appointment history
- Searching for patient information
- Checking for duplicate bookings

### Not Included Unless Confirmed

The client brief does not confirm the following features:

- Online payments
- Facial recognition
- AI treatment recommendations
- SMS reminders

These should not be added as requirements without confirmation from the client.

### Areas That Still Need Clarification

- Whether patients can access the system themselves
- Whether practitioners can manage appointments directly
- Whether appointment reminders are needed
- Which appointment statuses are required

## 2. Stakeholders

### Clinic Staff

Need to manage appointments and find patient information more easily. The client brief mentions duplicate bookings and difficulty finding patient information.

### Patients

Need their patient and appointment information to be recorded accurately. Patient information is included in the SmartCare brief.

### Practitioners

Need their practitioner and appointment information to be recorded accurately. The brief says the system will manage practitioner and appointment information.

### Management

Need a small and maintainable system for managing SmartCare information. This is stated directly in the client brief.

## 3. Functional Requirements

FR-01: Staff can record patient information.

FR-02: Staff can retrieve stored patient information.

FR-03: Staff can record practitioner information.

FR-04: Staff can record appointment information.

FR-05: Each appointment is linked to a patient.

FR-06: Each appointment is linked to a practitioner.

FR-07: The system records the status of each appointment.

FR-08: The system keeps a history of appointments.

FR-09: Staff can view stored appointment information.

FR-10: The system can identify possible duplicate bookings.

## 4. Non-Functional Requirements

NFR-01: The system should be simple for clinic staff to use.

NFR-02: Patient, practitioner, and appointment information should remain accurate and consistent.

NFR-03: The system should be easy to maintain and update without unnecessarily affecting other parts of the system.

NFR-04: The main appointment features should be testable on their own.

NFR-05: Appointment information and appointment history should be stored reliably.

## 5. User Stories

US-01: As a clinic staff member, I want to record patient information so that I can find it when needed.

US-02: As a clinic staff member, I want to record an appointment for a patient and practitioner so that appointments are managed accurately.

US-03: As a clinic staff member, I want to check for duplicate bookings so that booking conflicts can be found.

US-04: As a clinic staff member, I want to update an appointment status so that the current status is recorded correctly.

US-05: As a clinic staff member, I want to view appointment history so that I can access previous appointment information.

## 6. Acceptance Criteria

### AC-01: Record an Appointment

Given that a patient and practitioner have been identified, when clinic staff record an appointment, the system stores it and links it to the patient and practitioner.

### AC-02: Find Patient Information

Given that patient information has already been recorded, when clinic staff search for it, the system retrieves the matching information.

### AC-03: Update an Appointment Status

Given that an appointment exists, when its status is changed, the system stores the updated status.

### AC-04: Identify a Duplicate Booking

Given that an appointment already exists for a practitioner at a particular time, when another appointment is entered for the same practitioner and time, the system identifies it as a possible duplicate.

## 7. Assumptions and Open Questions

### Assumptions

- Clinic staff will use the SmartCare system, but their exact permissions have not been confirmed.
- Appointments will have a status, but the allowed status values have not been specified.
- Duplicate bookings should be identified, but the exact rules still need to be agreed with the client.

### Open Questions

1. What information needs to be stored for each patient?
2. What information needs to be stored for each practitioner?
3. Which appointment statuses should the system support?
4. Should the system prevent duplicate bookings or only warn staff about them?
5. How should staff search for patients?
6. Who can create, change, or cancel appointments?
7. How long should appointment history be kept?
8. Do patients or practitioners need direct access to the system?

## 8. Requirements Review Record

The following points were identified during the review of the requirements.

1. Patient information is not clearly defined. This was accepted because the requirements do not list the fields that need to be stored. This is covered by Open Question 1.

2. Practitioner information is not clearly defined. This was accepted because FR-03 does not list the information that needs to be recorded. This is covered by Open Question 2.

3. Appointment information is not clearly defined. This was accepted because FR-04 does not list the required appointment fields. The client needs to clarify this.

4. The duplicate-booking rules are unclear. This was accepted because AC-04 uses the same practitioner and time as an example, but the exact rule has not been confirmed. The client needs to validate it.

5. The phrase "simple for clinic staff to use" is subjective. There is currently no measurable definition, so NFR-01 cannot be tested objectively.

6. Patients and practitioners may benefit from the system without using it directly. The client brief does not confirm whether they will have direct access.

7. The system needs a way to identify patients uniquely. The current requirements do not define a patient identifier, so this needs to be discussed with the client.

8. It is not clear whether appointment information can be edited. The requirements cover creating and viewing appointments, but they do not confirm general editing.
