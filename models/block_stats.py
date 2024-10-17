class BlockStats:
    def __init__(self):
        self.perfect_blocks = 0
        self.great_blocks = 0
        self.good_blocks = 0
        self.poor_blocks = 0
        self.blocks_errors = 0

    def getTotalBlocks(self) -> int:
        return self.perfect_blocks + self.great_blocks + self.good_blocks + self.poor_blocks + self.blocks_errors