class PilotLicense:
    """
    Represents a pilot license or certification.
    """

    ALLOWED_LICENSE_TYPES = ["PPL", "CPL", "ATPL", "Other"]

    def __init__(self, license_type: str, other_description: str = None):
        """
        Initializes a new PilotLicense object.

        Args:
            license_type: The type of license (PPL, CPL, ATPL, or Other).
            other_description: A description of the license if the type is "Other".
        """
        if license_type not in self.ALLOWED_LICENSE_TYPES:
            raise ValueError(f"Invalid license type: {license_type}. Allowed types are: {self.ALLOWED_LICENSE_TYPES}")

        if license_type == "Other" and not other_description:
            raise ValueError("Other description is required when license type is 'Other'.")

        self.license_type = license_type
        self.other_description = other_description

    def __repr__(self):
        return f"PilotLicense(license_type='{self.license_type}', other_description='{self.other_description}')"