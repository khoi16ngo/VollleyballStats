from constants.action_qualities import *

class ServeStats:
    def __init__(self, player_serve_stats: list):
        self.aces = self._get_aces(player_serve_stats)
        self.great_serves = self._get_great_serves(player_serve_stats)
        self.good_serves = self._get_medium_serves(player_serve_stats)
        self.poor_serves = self._get_poor_serves(player_serve_stats)
        self.serve_errors = self._get_serve_errors(player_serve_stats)
        self.total_serves = self._get_total_serves()

    def _get_aces(self, player_serve_stats: list) -> int: 
        return player_serve_stats[PERFECT]

    def _get_great_serves(self, player_serve_stats: list) -> int: 
        return player_serve_stats[GOOD]

    def _get_medium_serves(self, player_serve_stats: list) -> int: 
        return player_serve_stats[OK]

    def _get_poor_serves(self, player_serve_stats: list) -> int: 
        return player_serve_stats[POOR]

    def _get_serve_errors(self, player_serve_stats: list) -> int: 
        return player_serve_stats[ERROR]
        
    def _get_total_serves(self) -> int:
        return self.aces + self.great_serves + self.good_serves + self.poor_serves + self.serve_errors
    
    def getOpponentOutOfSystemPercentage(self) -> float:
        return (self.aces + self.great_serves + self.good_serves) / self.total_serves
    
    def getServerAverage(self) -> float:
        total_weighted_serves = (self.aces * 4) + (self.great_serves * 3) + (self.good_serves * 2) + (self.poor_serves * 1) + (self.serve_errors * 0.5)
        return total_weighted_serves / self.total_serves
        
    