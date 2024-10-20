from models.player import Player
from services.stats.stat_builder import *

class PlayerStat:
    def __init__(self, player: Player, calculated_player_stats: list):
        self.name = player.name

        self.assist_stats = build_player_assist_stats(player.number, calculated_player_stats)
        self.attack_stats = build_player_attack_stats(player.number, calculated_player_stats)
        self.block_stats = build_player_block_stats(player.number, calculated_player_stats)
        self.dig_stats = build_player_dig_stats(player.number, calculated_player_stats)
        self.free_ball_stats = build_player_free_ball_stats(player.number, calculated_player_stats)
        self.serve_receive_stats = build_player_serve_receive_stats(player.number, calculated_player_stats)
        self.serve_stats = build_player_serve_stats(player.number, calculated_player_stats)

    def get_points(self):
        kills = self.attack_stats.kills
        aces = self.serve_stats.aces
        blocks = self.block_stats.perfect_blocks
        return kills + aces + blocks