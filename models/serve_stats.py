class ServeStats:
    def __init__(self):
        self.perfect_serves = 0
        self.great_serves = 0
        self.good_serves = 0
        self.poor_serves = 0
        self.serves_errors = 0
        
    def getTotalServes(self) -> int:
        return self.perfect_serves + self.great_serves + self.good_serves + self.poor_serves + self.serves_errors