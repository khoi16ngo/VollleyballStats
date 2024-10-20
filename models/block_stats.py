from constants.action_qualities import *

class BlockStats:
    def __init__(self, player_block_stats: list):
        self.perfect_blocks = self._get_perfect_blocks(player_block_stats)
        self.great_blocks = self._get_great_blocks(player_block_stats)
        self.good_blocks = self._get_medium_blocks(player_block_stats)
        self.poor_blocks = self._get_poor_blocks(player_block_stats)
        self.blocks_errors = self._get_block_errors(player_block_stats)
        self.total_blocks = self._get_total_blocks()

    def _get_perfect_blocks(self, player_block_stats: list) -> int: 
        return player_block_stats[PERFECT]

    def _get_great_blocks(self, player_block_stats: list) -> int: 
        return player_block_stats[GOOD]

    def _get_medium_blocks(self, player_block_stats: list) -> int: 
        return player_block_stats[OK]

    def _get_poor_blocks(self, player_block_stats: list) -> int: 
        return player_block_stats[POOR]

    def _get_block_errors(self, player_block_stats: list) -> int: 
        return player_block_stats[ERROR]
    
    def _get_total_blocks(self) -> int:
        return self.perfect_blocks + self.great_blocks + self.good_blocks + self.poor_blocks + self.blocks_errors

    def get_block_average(self) -> float:
        if self.total_blocks == 0:
            return 0.0
        
        total_weighted_blocks = (self.perfect_blocks * 4) + (self.great_blocks * 3) + (self.good_blocks * 2) + (self.poor_blocks * 1) + (self.blocks_errors * 0.5)
        return total_weighted_blocks / self.total_blocks 