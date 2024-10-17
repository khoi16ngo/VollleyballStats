from models.assist_stats import AssistStats
from models.block_stats import BlockStats
from models.dig_stats import DigStats
from models.free_ball_stats import FreeBallStats
from models.attack_stats import AttackStats
from models.serve_receive_stats import ServeReceiveStats
from models.serve_stats import ServeStats


class PlayerStat:
    def __init__(self, name: str, player_number: str):
        self.name = name
        self.player_number = name

        self.assist_stats = AssistStats()
        self.attack_stats = AttackStats()
        self.block_stats = BlockStats()
        self.dig_stats = DigStats()
        self.free_ball_stats = FreeBallStats()
        self.serve_receive_stats = ServeReceiveStats()
        self.serve_stats = ServeStats()