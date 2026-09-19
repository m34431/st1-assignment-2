# ===== TASK 1: Simple version =====
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


# ===== TASK 1 ENHANCED: Better version with functions =====
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("\nWelcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()

# ===== PART F: TEST CASES =====
print("\n--- TEST 1: Normal Appointment ---")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
display_appointments()

print("\n--- TEST 2: Blank Patient Name ---")
try:
    book_appointment('', 'Dr. John Doe', '2024-07-20 10:00 AM')
except ValueError as e:
    print(f"Error caught: {e}")

print("\n--- TEST 3: Double-Booking Same Practitioner ---")
appointments.clear()  # Start fresh
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. John Doe', '2024-07-20 10:00 AM')
display_appointments()

print("\n--- TEST 4: None Values ---")
try:
    book_appointment(None, 'Dr. John Doe', '2024-07-20 10:00 AM')
except ValueError as e:
    print(f"Error caught: {e}")# ===== TASK 1: Simple version =====
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


# ===== TASK 1 ENHANCED: Better version with functions =====
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("\nWelcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()

# ===== PART F: TEST CASES =====
print("\n--- TEST 1: Normal Appointment ---")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
display_appointments()

print("\n--- TEST 2: Blank Patient Name ---")
try:
    book_appointment('', 'Dr. John Doe', '2024-07-20 10:00 AM')
except ValueError as e:
    print(f"Error caught: {e}")

print("\n--- TEST 3: Double-Booking Same Practitioner ---")
appointments.clear()  # Start fresh
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. John Doe', '2024-07-20 10:00 AM')
display_appointments()

print("\n--- TEST 4: None Values ---")
try:
    book_appointment(None, 'Dr. John Doe', '2024-07-20 10:00 AM')
except ValueError as e:
    print(f"Error caught: {e}")