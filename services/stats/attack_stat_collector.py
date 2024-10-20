from models.player_stat import PlayerStat

def get_attack_stats_headers() -> list:
    return [
        'Kills',
        'Great Attacks',
        'Good Attacks',
        'Poor Attacks',
        'Attack Errors',
        'Total Attacks',
        'Hitting Average', 
        'Kill %',
        'Hitting %',
    ]

def collect_attack_stats(player_stats: PlayerStat) -> list:
    attack_stats = []

    attack_stats.append(player_stats.attack_stats.kills)
    attack_stats.append(player_stats.attack_stats.great_attacks)
    attack_stats.append(player_stats.attack_stats.good_attacks)
    attack_stats.append(player_stats.attack_stats.poor_attacks)
    attack_stats.append(player_stats.attack_stats.attack_errors)
    attack_stats.append(player_stats.attack_stats.total_attacks)

    attack_stats.append(player_stats.attack_stats.get_hitting_average())
    attack_stats.append(player_stats.attack_stats.get_kill_percentage())
    attack_stats.append(player_stats.attack_stats.get_hitting_percentage())

    return attack_stats
