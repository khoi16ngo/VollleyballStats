class FreeBallStats:
    def __init__(self):
        self.perfect_free_balls = 0
        self.great_free_balls = 0
        self.good_free_balls = 0
        self.poor_free_balls = 0
        self.free_balls_errors = 0

    def getTotalFreeBalls(self) -> int:
        return self.perfect_free_balls + self.great_free_balls + self.good_free_balls + self.poor_free_balls + self.free_balls_errors