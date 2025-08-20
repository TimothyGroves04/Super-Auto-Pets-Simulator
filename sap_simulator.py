from dataclasses import dataclass
from typing import List, Tuple
import argparse

@dataclass
class Pet:
    attack: int
    health: int

    def is_alive(self) -> bool:
        return self.health > 0

def simulate_battle(team1: List[Pet], team2: List[Pet]) -> Tuple[str, List[str]]:
    """Simulate a basic battle between two teams of pets.

    Args:
        team1: List of five pets for team 1.
        team2: List of five pets for team 2.

    Returns:
        A tuple containing the outcome string and the battle log.
    """
    log = []
    idx1 = idx2 = 0
    while idx1 < len(team1) and idx2 < len(team2):
        pet1 = team1[idx1]
        pet2 = team2[idx2]
        log.append(
            f"Team 1 Pet {idx1 + 1} ({pet1.attack}/{pet1.health}) vs Team 2 Pet {idx2 + 1} ({pet2.attack}/{pet2.health})"
        )
        # Simultaneous damage
        pet1.health -= pet2.attack
        pet2.health -= pet1.attack
        log.append(
            f" -> After attack: Team 1 Pet {idx1 + 1} ({max(pet1.health, 0)} hp), Team 2 Pet {idx2 + 1} ({max(pet2.health, 0)} hp)"
        )
        if not pet1.is_alive():
            log.append(f"Team 1 Pet {idx1 + 1} faints")
            idx1 += 1
        if not pet2.is_alive():
            log.append(f"Team 2 Pet {idx2 + 1} faints")
            idx2 += 1
    if idx1 >= len(team1) and idx2 >= len(team2):
        outcome = "Draw"
    elif idx1 >= len(team1):
        outcome = "Team 2 wins"
    elif idx2 >= len(team2):
        outcome = "Team 1 wins"
    else:
        outcome = "Unknown"  # Shouldn't occur
    log.append(outcome)
    return outcome, log

def get_team_input(team_number: int) -> List[Pet]:
    team = []
    for i in range(5):
        attack, health = map(
            int,
            input(
                f"Enter Team {team_number} Pet {i + 1} attack and health (e.g., 5 3): "
            ).split(),
        )
        team.append(Pet(attack, health))
    return team

def main():
    parser = argparse.ArgumentParser(description="Basic Super Auto Pets battle simulator")
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run a demo battle with sample teams instead of interactive input",
    )
    args = parser.parse_args()

    if args.demo:
        team1 = [Pet(5, 5), Pet(2, 3), Pet(4, 1), Pet(3, 2), Pet(1, 1)]
        team2 = [Pet(4, 5), Pet(3, 3), Pet(2, 2), Pet(5, 1), Pet(1, 3)]
    else:
        print("Enter stats for 5 pets on each team.")
        team1 = get_team_input(1)
        team2 = get_team_input(2)

    outcome, log = simulate_battle(team1, team2)
    print("Battle Log:")
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()
