from models.player_stat import PlayerStat

def get_assist_stats_headers() -> list:
    return [
        'Perfect Assists',
        'Great Assists',
        'Good Assists',
        'Poor Assists', 
        'Assist Errors',
        'Total Assists',
        'Assist Average',
    ]

def collect_assist_stats(player_stats: PlayerStat) -> list:
    assist_stats = []

    assist_stats.append(player_stats.assist_stats.perfect_assists)
    assist_stats.append(player_stats.assist_stats.great_assists)
    assist_stats.append(player_stats.assist_stats.good_assists)
    assist_stats.append(player_stats.assist_stats.poor_assists)
    assist_stats.append(player_stats.assist_stats.assists_errors)
    assist_stats.append(player_stats.assist_stats.total_assists)

    assist_stats.append(player_stats.assist_stats.get_assist_average())

    return assist_stats