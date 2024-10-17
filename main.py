from constants.action_qualities import *
from constants.action_types import *
from constants.players import *
from models.player_stat import PlayerStat
from models.assist_stats import AssistStats
from models.block_stats import BlockStats
from models.dig_stats import DigStats
from models.free_ball_stats import FreeBallStats
from models.attack_stats import AttackStats
from models.serve_receive_stats import ServeReceiveStats
from models.serve_stats import ServeStats

def main():
    ALL_ACTIONS = [
        SERVE,
        SERVE_RECEIVE_PASS,
        FREE_BALL,
        DIG,
        SET,
        ATTACK,
        BLOCK,
    ]

    ALL_QUALITIES = [
        PERFECT,
        GOOD,
        OK,
        POOR,
        ERROR,
    ]


    jeff_stats = PlayerStat("Jeff Cao", JEFF_CAO)
    khoi_stats = PlayerStat("Khoi Ngo", KHOI_NGO)
    tony_stats = PlayerStat("Tony Zhou", TONY_ZHOU)
    nate_stats = PlayerStat("Nate Dang", NATE_DANG)
    samson_stats = PlayerStat("Samson Ly", SAMSON_LY)
    johnny_stats = PlayerStat("Johnny Wong", JOHNNY_WONG)
    jay_stats = PlayerStat("Jay Cool", JEFF_CAO)
    brandon_stats = PlayerStat("Brandon Lee", BRANDON_LEE)
    gordon_stats = PlayerStat("Gordon Cheung", GORDON_CHEUNG)
    corry_stats = PlayerStat("Corry Phu", CORRY_PHU)
    mike_stats = PlayerStat("Mike Sun", MIKE_SUN)
    jorald_stats = PlayerStat("Jorald Joaquin", JORALD_JOAQUIN)
    wei_stats = PlayerStat("Wei Zhang", WEI_ZHANG)

    player_stats = [
        jeff_stats,
        khoi_stats, 
        tony_stats, 
        nate_stats, 
        samson_stats, 
        johnny_stats, 
        jay_stats,
        brandon_stats,
        gordon_stats,
        corry_stats,
        mike_stats,
        jorald_stats,
        wei_stats
    ]

    # TODO: fetch raw stats from file
    raw_player_stats = []

    calculated_player_stats = {}
    for raw_player_stat in raw_player_stats:
        # split each line into format "<play_number> <action> <quality>"
        player_number, action, quality = raw_player_stat.strip().split()
        player_number = int(player_number)
        quality = int(quality)

        # initialize player if player not in stat dict
        if player_number not in calculated_player_stats:
            calculated_player_stats[player_number] = {
                "actions": {action: {"qualities": {q: 0 for q in ALL_QUALITIES}} for action in ALL_ACTIONS}
            }

        # increase count by one if action and quality performed for player
        calculated_player_stats[player_number]["actions"][action]["qualities"][quality] += 1

    for player_stat in player_stats:
        player_stat.assist_stats = AssistStats()
        player_stat.attack_stats = AttackStats()
        player_stat.block_stats = BlockStats()
        player_stat.dig_stats = DigStats()
        player_stat.free_ball_stats = FreeBallStats()
        player_stat.serve_receive_stats = ServeReceiveStats()
        player_stat.serve_stats = ServeStats()
        
    
if __name__ == "__main__":
    main()