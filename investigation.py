
class Investigation:
    def __init__(self, case):
        self.case = case
        self.discovered_evidence = []
        self.case_notes = []


    def discover_evidence(self, evidence_id):
        for evidence in self.case.evidence:
            if evidence["id"] == evidence_id:
                if evidence not in self.discovered_evidence:
                    self.discovered_evidence.append(evidence)
                return
    def investigate_location(self, location_id):
        found_evidence = []

        for evidence in self.case.evidence:
            if evidence["location"] == location_id:
                if evidence not in self.discovered_evidence:
                    self.discovered_evidence.append(evidence)
                    found_evidence.append(evidence)

        return found_evidence