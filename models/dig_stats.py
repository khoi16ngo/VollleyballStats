from constants.action_qualities import *

class DigStats:
    def __init__(self, player_dig_stats: list):
        self.perfect_digs = self._get_perfect_digs(player_dig_stats)
        self.great_digs = self._get_great_digs(player_dig_stats)
        self.good_digs = self._get_medium_digs(player_dig_stats)
        self.poor_digs = self._get_poor_digs(player_dig_stats)
        self.dig_errors = self._get_dig_errors(player_dig_stats)
        self.total_digs = self._get_total_digs()

    def _get_perfect_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[PERFECT]

    def _get_great_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[GOOD]

    def _get_medium_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[OK]

    def _get_poor_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[POOR]

    def _get_dig_errors(self, player_dig_stats: list) -> int: 
        return player_dig_stats[ERROR]
    
    def _get_total_digs(self) -> int:
        return self.perfect_digs + self.great_digs + self.good_digs + self.poor_digs + self.dig_errors

    def get_dig_average(self) -> float:
        if self.total_digs == 0:
            return 0.0
        
        total_weighted_digs = (self.perfect_digs * 4) + (self.great_digs * 3) + (self.good_digs * 2) + (self.poor_digs * 1) + (self.dig_errors * 0.5)
        return total_weighted_digs / self.total_digs 