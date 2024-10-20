from constants.action_qualities import *

class AssistStats:
    def __init__(self, player_assist_stats: list):
        self.perfect_assists = self._get_perfect_assists(player_assist_stats)
        self.great_assists = self._get_great_assists(player_assist_stats)
        self.good_assists = self._get_medium_assists(player_assist_stats)
        self.poor_assists = self._get_poor_assists(player_assist_stats)
        self.assists_errors = self._get_assist_errors(player_assist_stats)
        self.total_assists = self._get_total_assists()

    def _get_perfect_assists(self, player_assist_stats: list) -> int: 
        return player_assist_stats[PERFECT]

    def _get_great_assists(self, player_assist_stats: list) -> int: 
        return player_assist_stats[GOOD]

    def _get_medium_assists(self, player_assist_stats: list) -> int: 
        return player_assist_stats[OK]

    def _get_poor_assists(self, player_assist_stats: list) -> int: 
        return player_assist_stats[POOR]

    def _get_assist_errors(self, player_assist_stats: list) -> int: 
        return player_assist_stats[ERROR]
    
    def _get_total_assists(self) -> int:
        return self.perfect_assists + self.great_assists + self.good_assists + self.poor_assists + self.assists_errors

    def get_assist_average(self) -> float:
        if self.total_assists == 0:
            return 0.0
        
        total_weighted_assists = (self.perfect_assists * 4) + (self.great_assists * 3) + (self.good_assists * 2) + (self.poor_assists * 1) + (self.assists_errors * 0.5)
        return total_weighted_assists / self.total_assists 
    
