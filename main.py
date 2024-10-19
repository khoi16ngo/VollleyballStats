import sys

sys.dont_write_bytecode = True

from constants.action_qualities import *
from constants.action_types import *
from constants.players import *
from models.player_stat import PlayerStat
from services.data_cleaner import clean_text_file
from services.stats.stat_builder import calculate_raw_player_stats

def clean_files():
    file_paths = [
        './rawStats/day_1/chicago_united_773_set_1.txt',
        './rawStats/day_1/chicago_united_773_set_2.txt',
        './rawStats/day_1/ngun_lam_white_set_1.txt',
        './rawStats/day_1/ngun_lam_white_set_2.txt',
        './rawStats/day_1/sf_dragons_og_set_1.txt',
        './rawStats/day_1/sf_dragons_og_set_2.txt',
        './rawStats/day_2/montreal_freemason_m2_set_1.txt',
        './rawStats/day_2/montreal_freemason_m2_set_2.txt',
        './rawStats/day_2/ny_vikings_red_set_1.txt',
        './rawStats/day_2/ny_vikings_red_set_2.txt',
        './rawStats/day_2/ny_vikings_red_set_3.txt',
        './rawStats/day_2/phi_cia_c_set_1.txt',
        './rawStats/day_2/phi_cia_c_set_2.txt',
        './rawStats/day_2/phi_cia_c_set_3.txt',
        './rawStats/day_2/sf_dragon_og_set_1.txt',
        './rawStats/day_2/sf_dynasty_daddies_set_1.txt',
        './rawStats/day_2/sf_dynasty_daddies_set_2.txt',
        './rawStats/day_2/sf_dynasty_daddies_set_3.txt',
        './rawStats/day_3/sf_dynasty_impact_set_1.txt',
        './rawStats/day_3/sf_dynasty_impact_set_2.txt',
    ]

    for file_path in file_paths:
        clean_text_file(file_path)

def calculate_stats():
    raw_player_stats= {}
    calculated_player_stats = calculate_raw_player_stats(raw_player_stats)
    
    jeff_stats = PlayerStat(JEFF_CAO, calculated_player_stats)
    khoi_stats = PlayerStat(KHOI_NGO, calculated_player_stats)
    tony_stats = PlayerStat(TONY_ZHOU, calculated_player_stats)
    nate_stats = PlayerStat(NATE_DANG, calculated_player_stats)
    samson_stats = PlayerStat(SAMSON_LY, calculated_player_stats)
    johnny_stats = PlayerStat(JOHNNY_WONG, calculated_player_stats)
    jay_stats = PlayerStat(JEFF_CAO, calculated_player_stats)
    brandon_stats = PlayerStat(BRANDON_LEE, calculated_player_stats)
    gordon_stats = PlayerStat(GORDON_CHEUNG, calculated_player_stats)
    corry_stats = PlayerStat(CORRY_PHU, calculated_player_stats)
    mike_stats = PlayerStat(MIKE_SUN, calculated_player_stats)
    jorald_stats = PlayerStat(JORALD_JOAQUIN, calculated_player_stats)
    wei_stats = PlayerStat(WEI_ZHANG, calculated_player_stats)

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
    
    #TODO - print out player stats
    
if __name__ == "__main__":
    clean_files()