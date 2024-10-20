from models.player_stat import PlayerStat

def get_free_ball_stats_headers() -> list:
    return [
        'Perfect Free Balls',
        'Great Free Balls',
        'Good Free Balls',
        'Poor Free Balls',
        'Free Ball Errors',
        'Total Free Balls',
        'Free Ball Average',
    ]

def collect_free_ball_stats(player_stats: PlayerStat) -> list:
    free_ball_stats = []

    free_ball_stats.append(player_stats.free_ball_stats.perfect_free_balls)
    free_ball_stats.append(player_stats.free_ball_stats.great_free_balls)
    free_ball_stats.append(player_stats.free_ball_stats.good_free_balls)
    free_ball_stats.append(player_stats.free_ball_stats.poor_free_balls)
    free_ball_stats.append(player_stats.free_ball_stats.free_ball_errors)
    free_ball_stats.append(player_stats.free_ball_stats.total_free_balls)

    free_ball_stats.append(player_stats.free_ball_stats.get_free_ball_average())

    return free_ball_stats
