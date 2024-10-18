from constants.action_qualities import *

class DigStats:
    def __init__(self, player_dig_stats: list):
        self.perfect_digs = self._get_perfect_digs(player_dig_stats)
        self.great_digs = self._get_great_digs(player_dig_stats)
        self.good_digs = self._get_medium_digs(player_dig_stats)
        self.poor_digs = self._get_poor_digs(player_dig_stats)
        self.dig_errors = self._get_block_errors(player_dig_stats)
        self.total_digs = self._get_total_digs()

    def _get_perfect_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[PERFECT]

    def _get_great_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[GOOD]

    def _get_medium_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[OK]

    def _get_poor_digs(self, player_dig_stats: list) -> int: 
        return player_dig_stats[POOR]

    def _get_block_errors(self, player_dig_stats: list) -> int: 
        return player_dig_stats[ERROR]
    
    def _get_total_digs(self) -> int:
        return self.perfect_digs + self.great_digs + self.good_digs + self.poor_digs + self.dig_errors
