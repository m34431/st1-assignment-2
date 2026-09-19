class Patient:
    def __init__(self, patient_id=None, name=None):
        # These attributes are provisional and require client validation.
        self.patient_id = patient_id
        self.name = name

    def get_information(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id=None, name=None):
        # These attributes are provisional and require client validation.
        self.practitioner_id = practitioner_id
        self.name = name


class Appointment:
    def __init__(self, appointment_id=None, patient=None,
                 practitioner=None, status=None):
        # appointment_id is provisional and requires validation.
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner

        # Status is supported by FR-07.
        self.status = status

    def get_information(self):
        pass

    def check_duplicate(self):
        pass