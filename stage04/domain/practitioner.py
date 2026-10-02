class Practitioner:
    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
    ):
        # validate practitioner_id
        if not practitioner_id or not practitioner_id.strip():
            raise ValueError("practitioner_id cannot be empty")

        # validate name
        if not name or not name.strip():
            raise ValueError("name cannot be empty")

        # validate specialty
        if not specialty or not specialty.strip():
            raise ValueError("specialty cannot be empty")

        # store practitioner_id
        self.practitioner_id = practitioner_id.strip()

        # store name
        self.name = name.strip()

        # store specialty
        self.specialty = specialty.strip()
