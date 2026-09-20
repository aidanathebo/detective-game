from case import load_case
from investigation import Investigation



def display_intro(case):
    print("=" * 50)
    print(case.title.upper())
    print("=" * 50)

    print(f"\nVictim: {case.victim['name']}")
    print(f"\n{case.opening}")


def display_suspects(case):
    print("\nSUSPECTS")
    print("-" * 50)

    for suspect in case.suspects:
        print(f"\n{suspect['name']}")
        print(suspect["occupation"])
        print(suspect["description"])

def display_evidence(investigation):
    print("\nEVIDENCE")
    print("-" * 50)

    if not investigation.discovered_evidence:
        print("\nYou haven't discovered any evidence yet.")
        return

    for evidence in investigation.discovered_evidence:
        print(f"\n{evidence['name']}")
        print(evidence["description"])

def investigate(case, investigation):
    print("\nLOCATIONS")
    print("-" * 50)

    for index, location in enumerate(case.locations, start=1):
        print(f"{index}. {location['name']}")

    print(f"{len(case.locations) + 1}. Return")

    choice = input("\nWhere would you like to investigate?\n> ")

    if not choice.isdigit():
        print("\nPlease enter a number.")
        return

    choice = int(choice)

    if choice == len(case.locations) + 1:
        return

    if choice < 1 or choice > len(case.locations):
        print("\nInvalid location.")
        return

    location = case.locations[choice - 1]

    print(f"\n{location['name'].upper()}")
    print("-" * 50)
    print(location["description"])

    found_evidence = investigation.investigate_location(location["id"])

    if found_evidence:
        print("\nNEW EVIDENCE DISCOVERED")

        for evidence in found_evidence:
            print(f"\n- {evidence['name']}")
            print(f"  {evidence['description']}")
    else:
        print("\nYou find nothing new.")


def main():
    case = load_case("data/case_01.json")
    investigation = Investigation(case)

    display_intro(case)

    while True:
        print("\n" + "=" * 50)
        print("What would you like to do?")
        print("1. View suspects")
        print("2. Investigate")
        print("3. Review evidence")
        print("4. Review case notes")
        print("5. Make an accusation")
        print("6. Exit")

        choice = input("\n> ")

        if choice == "1":
            display_suspects(case)

        elif choice == "2":
            investigate(case, investigation)

        elif choice == "3":
            display_evidence(investigation)

        elif choice == "4":
            print("\nCase notes coming soon.")

        elif choice == "5":
            print("\nAccusation system coming soon.")

        elif choice == "6":
            print("\nInvestigation suspended.")
            break

        else:
            print("\nPlease enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
