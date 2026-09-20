import json


class Case:
    def __init__(self, case_data):
        self.id = case_data["id"]
        self.title = case_data["title"]
        self.victim = case_data["victim"]
        self.opening = case_data["opening"]
        self.suspects = case_data["suspects"]
        self.other_people = case_data["other_people"]
        self.evidence = case_data["evidence"]
        self.locations = case_data["locations"]

def load_case(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        case_data = json.load(file)

    return Case(case_data)
