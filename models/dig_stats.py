class DigStats:
    def __init__(self):
        self.perfect_digs = 0
        self.great_digs = 0
        self.good_digs = 0
        self.poor_digs = 0
        self.digs_errors = 0

    def getTotalDigs(self) -> int:
        return self.perfect_digs + self.great_digs + self.good_digs + self.poor_digs + self.digs_errors