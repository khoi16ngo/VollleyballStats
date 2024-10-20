from models.player_stat import PlayerStat

def get_serve_stats_headers() -> list:
    return [
        'Aces',
        'Great Serves',
        'Good Serves',
        'Poor Serves',
        'Serve Errors',
        'Total Serves',
        'Serve Average',
        'Opponent Out of System %',
    ]

def collect_serve_stats(player_stats: PlayerStat) -> list:
    serve_stats = []

    serve_stats.append(player_stats.serve_stats.aces)
    serve_stats.append(player_stats.serve_stats.great_serves)
    serve_stats.append(player_stats.serve_stats.good_serves)
    serve_stats.append(player_stats.serve_stats.poor_serves)
    serve_stats.append(player_stats.serve_stats.serve_errors)
    serve_stats.append(player_stats.serve_stats.total_serves)
    
    serve_stats.append(player_stats.serve_stats.get_serve_average())
    serve_stats.append(player_stats.serve_stats.get_opponent_out_of_system_percentage())

    return serve_stats
