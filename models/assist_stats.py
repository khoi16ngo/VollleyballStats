class AssistStats:
    def __init__(self):
        self.perfect_assists = 0
        self.great_assists = 0
        self.good_assists = 0
        self.poor_assists = 0
        self.assists_errors = 0
    
    def getTotalAssists(self) -> int:
        return self.perfect_assists + self.great_assists + self.good_assists + self.poor_assists + self.assists_errors