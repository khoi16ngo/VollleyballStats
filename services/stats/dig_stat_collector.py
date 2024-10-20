from models.player_stat import PlayerStat

def get_dig_stats_headers() -> list:
    return [
        'Perfect Digs',
        'Great Digs',
        'Good Digs',
        'Poor Digs',
        'Dig Errors',
        'Total Digs',
        'Dig Average',
    ]

def collect_dig_stats(player_stats: PlayerStat) -> list:
    dig_stats = []

    dig_stats.append(player_stats.dig_stats.perfect_digs)
    dig_stats.append(player_stats.dig_stats.great_digs)
    dig_stats.append(player_stats.dig_stats.good_digs)
    dig_stats.append(player_stats.dig_stats.poor_digs)
    dig_stats.append(player_stats.dig_stats.dig_errors)
    dig_stats.append(player_stats.dig_stats.total_digs)

    dig_stats.append(player_stats.dig_stats.get_dig_average())

    return dig_stats
