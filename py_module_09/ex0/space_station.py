"""
Exercise 0: Space Station Data
Objective: Learn basic Pydantic model creation
with BaseModel and Field validation.

python3 -m venv venv
source venv/bin/activate
pip install "pydantic>=2.0"
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError # noqa f401


class SpaceStation(BaseModel):
    """Model representing a space station with validated fields."""

    station_id: str = Field(..., min_length=3, max_length=10,
                            description="Station identifier")
    name: str = Field(..., min_length=1, max_length=50,
                      description="Station name")
    crew_size: int = Field(..., ge=1, le=20,
                           description="Number of crew members (1-20)")
    power_level: float = Field(..., ge=0.0, le=100.0,
                               description="Power level percentage")
    oxygen_level: float = Field(..., ge=0.0, le=100.0,
                                description="Oxygen level percentage")
    last_maintenance: datetime = Field(..., description="Date and timeof "
                                       "last maintenance")
    is_operational: bool = Field(default=True,
                                 description="Whether the station "
                                 "is operational")
    notes: Optional[str] = Field(default=None, max_length=200,
                                 description="Optional notes")


def main() -> None:
    """Demonstrate SpaceStation model validation
    with valid and invalid instances."""

    print("Space Station Data Validation")
    print("=" * 40)

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 8, 30, 0),
        is_operational=True,
        notes="All systems nominal.",
    )

    status = "Operational" if valid_station.is_operational else "Offline"
    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    print(f"Status: {status}")
    print("=" * 40)

    try:
        SpaceStation(
            station_id="BAD001",
            name="Overcrowded Station",
            crew_size=50,
            power_level=70.0,
            oxygen_level=80.0,
            last_maintenance=datetime(2024, 1, 10, 12, 0, 0),
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
