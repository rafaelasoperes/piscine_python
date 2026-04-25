"""
Exercise 1: Alien Contact Logs
Objective: Master custom validation using
@model_validator for complex business rules.
"""
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field  # type: ignore
from pydantic import ValidationError, model_validator  # type: ignore


class ContactType(str, Enum):
    """Enum defining the possible types of alien contact."""
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Model representing an alien contact report
    with custom validation rules."""

    contact_id: str = Field(..., min_length=5, max_length=15,
                            description="Contact report ID")
    timestamp: datetime = Field(..., description="Date and time "
                                "of the contact event")
    location: str = Field(..., min_length=3, max_length=100,
                          description="Contact location")
    contact_type: ContactType = Field(...,
                                      description="Type of alien contact")
    signal_strength: float = Field(..., ge=0.0, le=10.0,
                                   description="Signal strength (0-10)")
    duration_minutes: int = Field(..., ge=1, le=1440,
                                  description="Duration in minutes (max 24h)")
    witness_count: int = Field(..., ge=1, le=100,
                               description="Number of witnesses")
    message_received: Optional[str] = Field(
        default=None, max_length=500, description="Message content if received"
    )
    is_verified: bool = Field(default=False,
                              description="Whether the report is verified")

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Apply business rules that depend on multiple fields together."""
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self


def main() -> None:
    """Demonstrate AlienContact model with valid and invalid reports."""

    print("Alien Contact Log Validation")
    print("=" * 38)
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 6, 21, 3, 15, 0),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )
    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Type: {valid_contact.contact_type.value}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print(f"Witnesses: {valid_contact.witness_count}")
    print(f"Message: '{valid_contact.message_received}'")
    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_BAD_001",
            timestamp=datetime(2024, 6, 21, 4, 0, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=False,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
