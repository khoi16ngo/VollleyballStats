class AttackStats:
    def __init__(self):
        self.perfect_attacks = 0
        self.great_attacks = 0
        self.good_attacks = 0
        self.poor_attacks = 0
        self.attacks_errors = 0
    
    def getTotalAttacks(self) -> int:
        return self.perfect_attacks + self.great_attacks + self.good_attacks + self.poor_attacks + self.attacks_errors