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
    while True:
        print("\nEVIDENCE")
        print("-" * 50)

        if not investigation.discovered_evidence:
            print("\nYou haven't discovered any evidence yet.")
            return

        for index, evidence in enumerate(
            investigation.discovered_evidence,
            start=1
        ):
            print(f"{index}. {evidence['name']}")

        print(
            f"{len(investigation.discovered_evidence) + 1}. Return"
        )

        choice = input(
            "\nSelect evidence to examine:\n> "
        )

        if not choice.isdigit():
            print("\nPlease enter a number.")
            continue

        choice = int(choice)

        if choice == len(investigation.discovered_evidence) + 1:
            return

        if choice < 1 or choice > len(
            investigation.discovered_evidence
        ):
            print("\nInvalid choice.")
            continue

        evidence = investigation.discovered_evidence[
            choice - 1
        ]

        print(f"\n{evidence['name'].upper()}")
        print("-" * 50)
        print(evidence["description"])

        new_clues = investigation.examine_evidence(
            evidence["id"]
        )

        if new_clues:
            print("\nNEW INFORMATION")

            for clue in new_clues:
                print(f"\n- {clue['name']}")
                print(f"  {clue['description']}")

        else:
            print("\nYou learn nothing new.")

def display_case_notes(investigation):
    print("\nCASE NOTES")
    print("-" * 50)

    if not investigation.discovered_clues:
        print("\nYou haven't learned anything significant yet.")
        return

    for clue in investigation.discovered_clues:
        print(f"\n{clue['name']}")
        print(clue["description"])

def investigate_location(location, investigation):
    print(f"\n{location['name'].upper()}")
    print("-" * 50)
    print(location["description"])

    areas = location.get("areas", [])

    if not areas:
        print("\nThere is nothing specific to examine here yet.")
        return

    while True:
        print("\nWhat would you like to examine?")

        for index, area in enumerate(areas, start=1):
            print(f"{index}. {area['name']}")

        print(f"{len(areas) + 1}. Return")

        choice = input("\n> ")

        if not choice.isdigit():
            print("\nPlease enter a number.")
            continue

        choice = int(choice)

        if choice == len(areas) + 1:
            return

        if choice < 1 or choice > len(areas):
            print("\nInvalid choice.")
            continue

        area = areas[choice - 1]

        print(f"\n{area['name'].upper()}")
        print("-" * 50)
        print(area["description"])

        found_evidence = investigation.investigate_area(
            location["id"],
            area["id"]
        )

        if found_evidence:
            print("\nNEW EVIDENCE DISCOVERED")

            for evidence in found_evidence:
                print(f"\n- {evidence['name']}")
                print(f"  {evidence['description']}")
        else:
            print("\nYou find nothing new.")

def investigate(case, investigation):
    while True:
        print("\nLOCATIONS")
        print("-" * 50)

        for index, location in enumerate(case.locations, start=1):
            print(f"{index}. {location['name']}")

        print(f"{len(case.locations) + 1}. Return")

        choice = input("\nWhere would you like to investigate?\n> ")

        if not choice.isdigit():
            print("\nPlease enter a number.")
            continue

        choice = int(choice)

        if choice == len(case.locations) + 1:
            return

        if choice < 1 or choice > len(case.locations):
            print("\nInvalid location.")
            continue

        location = case.locations[choice - 1]

        investigate_location(location, investigation)

def interview_person(person, investigation):
    topics = person.get("topics", [])

    if not topics:
        print(f"\n{person['name']} has nothing to say right now.")
        return

    while True:
        available_topics = []

        for topic in topics:
            if investigation.topic_is_available(topic):
                available_topics.append(topic)

        print(f"\nINTERVIEW: {person['name'].upper()}")
        print("-" * 50)

        for index, topic in enumerate(available_topics, start=1):
            print(f"{index}. {topic['question']}")

        print(f"{len(available_topics) + 1}. Return")

        choice = input("\nWhat would you like to ask?\n> ")

        if not choice.isdigit():
            print("\nPlease enter a number.")
            continue

        choice = int(choice)

        if choice == len(available_topics) + 1:
            return

        if choice < 1 or choice > len(available_topics):
            print("\nInvalid choice.")
            continue

        topic = available_topics[choice - 1]

        print(f"\n{person['name']}:")
        print(topic["answer"])

        new_clues = []

        for clue_id in topic.get("clues", []):
            clue = investigation.discover_clue(clue_id)

            if clue:
                new_clues.append(clue)

        if new_clues:
            print("\nNEW INFORMATION")

            for clue in new_clues:
                print(f"\n- {clue['name']}")
                print(f"  {clue['description']}")

def interview(case, investigation):
    while True:
        people = case.suspects + case.other_people

        print("\nPEOPLE")
        print("-" * 50)

        for index, person in enumerate(people, start=1):
            print(f"{index}. {person['name']}")

        print(f"{len(people) + 1}. Return")

        choice = input("\nWho would you like to interview?\n> ")

        if not choice.isdigit():
            print("\nPlease enter a number.")
            continue

        choice = int(choice)

        if choice == len(people) + 1:
            return

        if choice < 1 or choice > len(people):
            print("\nInvalid choice.")
            continue

        person = people[choice - 1]

        interview_person(person, investigation)


def main():
    case = load_case("data/case_01.json")
    investigation = Investigation(case)

    display_intro(case)

    while True:
        print("\n" + "=" * 50)
        print("What would you like to do?")
        print("1. View suspects")
        print("2. Investigate")
        print("3. Interview")
        print("4. Review evidence")
        print("5. Review case notes")
        print("6. Make an accusation")
        print("7. Exit")

        choice = input("\n> ")

        if choice == "1":
            display_suspects(case)

        elif choice == "2":
            investigate(case, investigation)

        elif choice == "3":
            interview(case, investigation)

        elif choice == "4":
            display_evidence(investigation)

        elif choice == "5":
            display_case_notes(investigation)

        elif choice == "6":
            print("\nAccusation system coming soon.")

        elif choice == "7":
            print("\nInvestigation ended.")
            break

        else:
            print("\nPlease enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
