class ServeReceiveStats:
    def __init__(self):
        self.perfect_passes = 0
        self.great_passes = 0
        self.good_passes = 0
        self.poor_passes = 0
        self.passes_errors = 0

    def getTotalPasses(self) -> int:
        return self.perfect_passes + self.great_passes + self.good_passes + self.poor_passes + self.passes_errors