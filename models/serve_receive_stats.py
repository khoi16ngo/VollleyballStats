from constants.action_qualities import *

class ServeReceiveStats:
    def __init__(self, player_serve_receive_stats: list):
        self.perfect_passes = self._get_perfect_pass(player_serve_receive_stats)
        self.great_passes = self._get_great_pass(player_serve_receive_stats)
        self.good_passes = self._get_medium_pass(player_serve_receive_stats)
        self.poor_passes = self._get_poor_pass(player_serve_receive_stats)
        self.pass_errors = self._get_block_errors(player_serve_receive_stats)
        self.total_passes = self._get_total_passes()

    def _get_perfect_pass(self, player_serve_receive_stats: list) -> int: 
        return player_serve_receive_stats[PERFECT]

    def _get_great_pass(self, player_serve_receive_stats: list) -> int: 
        return player_serve_receive_stats[GOOD]

    def _get_medium_pass(self, player_serve_receive_stats: list) -> int: 
        return player_serve_receive_stats[OK]

    def _get_poor_pass(self, player_serve_receive_stats: list) -> int: 
        return player_serve_receive_stats[POOR]

    def _get_block_errors(self, player_serve_receive_stats: list) -> int: 
        return player_serve_receive_stats[ERROR]

    def _get_total_passes(self) -> int:
        return self.perfect_passes + self.great_passes + self.good_passes + self.poor_passes + self.pass_errors

    def get_in_system_percentage(self):
        if self.total_passes == 0:
            return 0.0
        
        return (self.perfect_passes + self.great_passes + self.good_passes) / self.total_passes

    def get_out_of_system_percentage(self):
        if self.total_passes == 0:
            return 0.0
        
        return self.pass_errors / self.total_passes
    
    def get_pass_average(self):
        if self.total_passes == 0:
            return 0.0
        
        total_weighted_passes = (self.perfect_passes * 4) + (self.great_passes * 3) + (self.good_passes * 2) + (self.poor_passes * 1) + (self.pass_errors * 0.5)
        return total_weighted_passes / self.total_passes 