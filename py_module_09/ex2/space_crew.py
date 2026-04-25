"""
Exercise 2: Space Crew Management
Objective: Master nested Pydantic models and complex data relationships.
"""

from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator # noqa f401


class Rank(str, Enum):
    """Enum defining the possible crew ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Model representing an individual crew member."""

    member_id: str = Field(..., min_length=3, max_length=10,
                           description="Member identifier")
    name: str = Field(..., min_length=2, max_length=50,
                      description="Full name")
    rank: Rank = Field(..., description="Crew rank")
    age: int = Field(..., ge=18, le=80, description="Age in years (18-80)")
    specialization: str = Field(
        ..., min_length=3, max_length=30, description="Area of specialization"
    )
    years_experience: int = Field(..., ge=0, le=50,
                                  description="Years of experience (0-50)")
    is_active: bool = Field(default=True,
                            description="Whether the crew member is active")


class SpaceMission(BaseModel):
    """Model representing a space mission with a nested crew list."""

    mission_id: str = Field(..., min_length=5, max_length=15,
                            description="Mission identifier")
    mission_name: str = Field(..., min_length=3, max_length=100,
                              description="Mission name")
    destination: str = Field(..., min_length=3, max_length=50,
                             description="Mission destination")
    launch_date: datetime = Field(..., description="Planned launch "
                                  "date and time")
    duration_days: int = Field(..., ge=1, le=3650,
                               description="Duration in days (max 10 years)")
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12,
                                   description="Crew members")
    mission_status: str = Field(default="planned",
                                description="Current mission status")
    budget_millions: float = Field(
        ..., ge=1.0, le=10000.0, description="Budget in millions of dollars"
    )

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Apply safety and operational rules that span multiple fields."""

        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        senior_ranks = {Rank.commander, Rank.captain}
        has_senior = any(member.rank in senior_ranks for member in self.crew)
        if not has_senior:
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            required = len(self.crew) / 2
            if experienced < required:
                raise ValueError("Long missions (> 365 days) require at "
                                 "least 50% experienced crew (5+ years)")

        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(f"All crew members must be active. Inactive: "
                             f"{', '.join(inactive)}")

        return self


def main() -> None:
    """
    Demonstrate SpaceMission validation with
    a valid and an invalid mission.
    """

    print("Space Mission Crew Validation")
    print("=" * 41)
    crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=42,
            specialization="Mission Command",
            years_experience=18,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=10,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=29,
            specialization="Engineering",
            years_experience=6,
        ),
    ]

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 9, 1, 6, 0, 0),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(f"  - {member.name} ({member.rank.value}) "
              f"- {member.specialization}")

    print("=" * 41)

    try:
        invalid_crew = [
            CrewMember(
                member_id="CM010",
                name="Bob Lee",
                rank=Rank.cadet,
                age=22,
                specialization="Science",
                years_experience=1,
            ),
            CrewMember(
                member_id="CM011",
                name="Carol Danvers",
                rank=Rank.officer,
                age=30,
                specialization="Medicine",
                years_experience=5,
            ),
        ]

        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Doomed Mission",
            destination="Jupiter",
            launch_date=datetime(2024, 10, 1, 9, 0, 0),
            duration_days=200,
            crew=invalid_crew,
            budget_millions=500.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
