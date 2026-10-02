class Patient:
    def __init__(self, patient_id: str, name: str):
        if not patient_id or not patient_id.strip():
            raise ValueError("patient_id cannot be empty")

        if not name or not name.strip():
            raise ValueError("name cannot be empty")

        self.patient_id = patient_id.strip()
        self.name = name.strip()
