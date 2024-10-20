from models.player_stat import PlayerStat

def get_serve_receive_stats_headers() -> list:
    return [
        'Perfect Serve Receive Passes',
        'Great Serve Receive Passes',
        'Good Serve Receive Passes',
        'Poor Serve Receive Passes',
        'Serve Receive Pass Errors',
        'Total Serve Receive Passes',
        'Serve Receive Pass Average',
        'In System %',
        'Out of System %',
    ]

def collect_serve_receive_stats(player_stats: PlayerStat) -> list:
    serve_receive_stats = []

    serve_receive_stats.append(player_stats.serve_receive_stats.perfect_passes)
    serve_receive_stats.append(player_stats.serve_receive_stats.great_passes)
    serve_receive_stats.append(player_stats.serve_receive_stats.good_passes)
    serve_receive_stats.append(player_stats.serve_receive_stats.poor_passes)
    serve_receive_stats.append(player_stats.serve_receive_stats.pass_errors)
    serve_receive_stats.append(player_stats.serve_receive_stats.total_passes)

    serve_receive_stats.append(player_stats.serve_receive_stats.get_pass_average())
    serve_receive_stats.append(player_stats.serve_receive_stats.get_in_system_percentage())
    serve_receive_stats.append(player_stats.serve_receive_stats.get_out_of_system_percentage())
    
    return serve_receive_stats
