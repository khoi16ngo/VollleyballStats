from models.player_stat import PlayerStat

def get_block_stats_headers() -> list:
    return [
        'Perfect Blocks',
        'Great Blocks',
        'Good Blocks',
        'Poor Blocks',
        'Block Errors', 
        'Total Blocks',
        'Block Average',
    ]

def collect_block_stats(player_stats: PlayerStat) -> list:
    block_stats = []

    block_stats.append(player_stats.block_stats.perfect_blocks)
    block_stats.append(player_stats.block_stats.great_blocks)
    block_stats.append(player_stats.block_stats.good_blocks)
    block_stats.append(player_stats.block_stats.poor_blocks)
    block_stats.append(player_stats.block_stats.blocks_errors)
    block_stats.append(player_stats.block_stats.total_blocks)

    block_stats.append(player_stats.block_stats.get_block_average())

    return block_stats