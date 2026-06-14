from datetime import datetime, timezone
from pydantic import Field, BaseModel, model_validator, ValidationError
from enum import Enum


class RankEnum(str, Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            m.rank in (RankEnum.commander, RankEnum.captain)
            for m in self.crew
        )
        if not has_leader:
            raise ValueError(
                    "Mission must have at least one Commander or Captain"
                    )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    member1 = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=RankEnum.commander,
        age=30,
        specialization="Mission Commander",
        years_experience=10,
        is_active=True,
            )
    member2 = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=RankEnum.lieutenant,
        age=30,
        specialization="Navigation",
        years_experience=10,
        is_active=True,
            )
    member3 = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=RankEnum.officer,
        age=40,
        specialization="Engineering",
        years_experience=15,
        is_active=True,
            )
    mission1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 1, 1, 1, 1, 1, tzinfo=timezone.utc),
        duration_days=900,
        crew=[member1, member2, member3],
        mission_status="planned",
        budget_millions=2500,
            )

    print(f"Mission: {mission1.mission_name}")
    print(f"ID: {mission1.mission_id}")
    print(f"Destination: {mission1.destination}")
    print(f"Duration: {mission1.duration_days} days")
    print(f"Budget: ${mission1.budget_millions}M")
    print(f"Crew size: {len(mission1.crew)}")
    print("Crew Members: ")
    for member in mission1.crew:
        print(
                f"- {member.name} ({member.rank.value}) -"
                f"{member.specialization}"
                )
    print()
    print("=========================================")

    try:
        _ = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 1, 1, 1, tzinfo=timezone.utc),
            duration_days=900,
            crew=[member2, member3],
            mission_status="planned",
            budget_millions=2500,
                )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
