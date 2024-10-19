from constants.action_qualities import *

class AttackStats:
    def __init__(self, player_attack_stats: list):
        self.kills = self._get_kills(player_attack_stats)
        self.great_attacks = self._get_great_attacks(player_attack_stats)
        self.good_attacks = self._get_medium_attacks(player_attack_stats)
        self.poor_attacks = self._get_poor_attacks(player_attack_stats)
        self.attacks_errors = self._get_attack_errors(player_attack_stats)
        self.total_attacks = self._get_total_attacks()
    
    def _get_kills(self, player_attack_stats: list) -> int: 
        return player_attack_stats[PERFECT]

    def _get_great_attacks(self, player_attack_stats: list) -> int: 
        return player_attack_stats[GOOD]

    def _get_medium_attacks(self, player_attack_stats: list) -> int: 
        return player_attack_stats[OK]

    def _get_poor_attacks(self, player_attack_stats: list) -> int: 
        return player_attack_stats[POOR]

    def _get_attack_errors(self, player_attack_stats: list) -> int: 
        return player_attack_stats[ERROR]
    
    def _get_total_attacks(self) -> int:
        return self.kills + self.great_attacks + self.good_attacks + self.poor_attacks + self.attacks_errors
    
    def get_hitting_percentage(self) -> float:
        kills = self.kills
        attack_errors = self.attacks_errors
        total_attacks = self.getTotalAttacks()
        return (kills - attack_errors) / total_attacks

    def get_kill_percentage(self) -> float:
        kills = self.kills
        total_attacks = self.getTotalAttacks()
        return kills / total_attacks

    def get_hitting_average(self) -> float:
        kills = self.kills
        great_attacks = self.great_attacks
        medium_attacks = self.good_attacks
        poor_attacks = self.poor_attacks
        attack_errors = self.attacks_errors

        total_weighted_attacks = (kills * 4) + (great_attacks * 3) + (medium_attacks * 2) + (poor_attacks * 1) + (attack_errors * 0.5)
        total_attacks = self.getTotalAttacks()
        return total_weighted_attacks / total_attacks 