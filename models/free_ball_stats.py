from constants.action_qualities import *

class FreeBallStats:
    def __init__(self, player_free_ball_stats: list):
        self.perfect_free_balls = self._get_perfect_free_balls(player_free_ball_stats)
        self.great_free_balls = self._get_great_free_balls(player_free_ball_stats)
        self.good_free_balls = self._get_medium_free_balls(player_free_ball_stats)
        self.poor_free_balls = self._get_poor_free_balls(player_free_ball_stats)
        self.free_ball_errors = self._get_block_errors(player_free_ball_stats)
        self.total_free_balls = self._get_total_free_balls()

    def _get_perfect_free_balls(self, player_free_ball_stats: list) -> int: 
        return player_free_ball_stats[PERFECT]

    def _get_great_free_balls(self, player_free_ball_stats: list) -> int: 
        return player_free_ball_stats[GOOD]

    def _get_medium_free_balls(self, player_free_ball_stats: list) -> int: 
        return player_free_ball_stats[OK]

    def _get_poor_free_balls(self, player_free_ball_stats: list) -> int: 
        return player_free_ball_stats[POOR]

    def _get_block_errors(self, player_free_ball_stats: list) -> int: 
        return player_free_ball_stats[ERROR]
    
    def _get_total_free_balls(self) -> int:
        return self.perfect_free_balls + self.great_free_balls + self.good_free_balls + self.poor_free_balls + self.free_ball_errors
    
    def get_free_ball_average(self) -> float:
        if self.total_free_balls == 0:
            return 0.0
        
        total_weighted_free_balls = (self.perfect_free_balls * 4) + (self.great_free_balls * 3) + (self.good_free_balls * 2) + (self.poor_free_balls * 1) + (self.free_ball_errors * 0.5)
        return total_weighted_free_balls / self.total_free_balls 