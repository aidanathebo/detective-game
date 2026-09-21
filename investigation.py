
class Investigation:
    def __init__(self, case):
        self.case = case
        self.discovered_evidence = []
        self.discovered_clues = []
        self.case_notes = []


    def discover_evidence(self, evidence_id):
        for evidence in self.case.evidence:
            if evidence["id"] == evidence_id:
                if evidence not in self.discovered_evidence:
                    self.discovered_evidence.append(evidence)
                return
            
    def investigate_area(self, location_id, area_id):
        found_evidence = []

        for evidence in self.case.evidence:
            if (
                evidence["location"] == location_id
                and evidence.get("area") == area_id
            ):
                if evidence not in self.discovered_evidence:
                    self.discovered_evidence.append(evidence)
                    found_evidence.append(evidence)

        return found_evidence

    def find_clue (self, clue_id): 
        for clue in self.case.clues: 
            if clue["id"] == clue_id:
                return clue 

        return None

    def examine_evidence (self, evidence_id): 
        for evidence in self.discovered_evidence: 
            if evidence["id"] == evidence_id: 
                new_clues = []
                for clue_id in evidence.get("discoveries", []): 
                    clue = self.find_clue(clue_id)
                    if clue and clue not in self.discovered_clues: 
                        self.discovered_clues.append(clue)
                        new_clues.append(clue)
                return new_clues
        return []

    def discover_clue(self, clue_id):
        clue = self.find_clue(clue_id)

        if clue and clue not in self.discovered_clues:
            self.discovered_clues.append(clue)
            return clue

        return None

    def has_clue(self, clue_id):
        for clue in self.discovered_clues:
            if clue["id"] == clue_id:
                return True

        return False


    def has_evidence(self, evidence_id):
        for evidence in self.discovered_evidence:
            if evidence["id"] == evidence_id:
                return True

        return False


    def topic_is_available(self, topic):
        required_clues = topic.get("requires_clues", [])
        required_evidence = topic.get("requires_evidence", [])

        for clue_id in required_clues:
            if not self.has_clue(clue_id):
                return False

        for evidence_id in required_evidence:
            if not self.has_evidence(evidence_id):
                return False

        return True