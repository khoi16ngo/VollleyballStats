import sys
sys.dont_write_bytecode = True

from utilities.util_file import get_last_n_file_path, remove_file_extension
from services.data.data_writer import print_stats_csv
from services.stats.assist_stat_collector import collect_assist_stats, get_assist_stats_headers
from services.stats.attack_stat_collector import collect_attack_stats, get_attack_stats_headers
from services.stats.block_stat_collector import collect_block_stats, get_block_stats_headers
from services.stats.dig_stat_collector import collect_dig_stats, get_dig_stats_headers
from services.stats.free_ball_stats import collect_free_ball_stats, get_free_ball_stats_headers
from services.stats.serve_receive_stat_collector import collect_serve_receive_stats, get_serve_receive_stats_headers
from services.stats.serve_stat_collector import collect_serve_stats, get_serve_stats_headers
from services.data.data_reader import read_data_file
from constants.action_qualities import *
from constants.action_types import *
from constants.players import *
from models.player_stat import PlayerStat
from services.data.data_cleaner import clean_text_file
from services.stats.stat_builder import calculate_raw_player_stats

def clean_files():
    file_paths = [
        './raw_stats/day_1/chicago_united_773_set_1.txt',
        './raw_stats/day_1/chicago_united_773_set_2.txt',
        './raw_stats/day_1/ngun_lam_white_set_1.txt',
        './raw_stats/day_1/ngun_lam_white_set_2.txt',
        './raw_stats/day_1/sf_dragons_og_set_1.txt',
        './raw_stats/day_1/sf_dragons_og_set_2.txt',
        './raw_stats/day_2/montreal_freemason_m2_set_1.txt',
        './raw_stats/day_2/montreal_freemason_m2_set_2.txt',
        './raw_stats/day_2/ny_vikings_red_set_1.txt',
        './raw_stats/day_2/ny_vikings_red_set_2.txt',
        './raw_stats/day_2/ny_vikings_red_set_3.txt',
        './raw_stats/day_2/phi_cia_c_set_1.txt',
        './raw_stats/day_2/phi_cia_c_set_2.txt',
        './raw_stats/day_2/phi_cia_c_set_3.txt',
        './raw_stats/day_2/sf_dragon_og_set_1.txt',
        './raw_stats/day_2/sf_dynasty_daddies_set_1.txt',
        './raw_stats/day_2/sf_dynasty_daddies_set_2.txt',
        './raw_stats/day_2/sf_dynasty_daddies_set_3.txt',
        './raw_stats/day_3/sf_dynasty_impact_set_1.txt',
        './raw_stats/day_3/sf_dynasty_impact_set_2.txt',
    ]

    for file_path in file_paths:
        clean_text_file(file_path)

def calculate_set_stats(file_paths: list):
    headers = ['Player Name']
    headers += get_attack_stats_headers()
    headers += get_block_stats_headers()
    headers += get_assist_stats_headers()
    headers += get_free_ball_stats_headers()
    headers += get_dig_stats_headers()
    headers += get_serve_receive_stats_headers()
    headers += get_serve_stats_headers()

    for file_path in file_paths:
        raw_player_stats = read_data_file(file_path)
        calculated_player_stats = calculate_raw_player_stats(raw_player_stats)

        total_player_stats = []
        for player in ALL_PLAYERS:
            player_stat = PlayerStat(player, calculated_player_stats)
            
            total_player_stat = [player_stat.name]
            total_player_stat += collect_attack_stats(player_stat)
            total_player_stat += collect_block_stats(player_stat)
            total_player_stat += collect_assist_stats(player_stat)
            total_player_stat += collect_free_ball_stats(player_stat)
            total_player_stat += collect_dig_stats(player_stat)
            total_player_stat += collect_serve_receive_stats(player_stat)
            total_player_stat += collect_serve_stats(player_stat)

            total_player_stats.append(total_player_stat)

        all_stats = [headers] + total_player_stats
        file_path = get_last_n_file_path(file_path, 2)
        new_cleaned_file_name = "./results/" + remove_file_extension(file_path) + "_stats.txt"
        print_stats_csv(new_cleaned_file_name, all_stats)

def calculate_total_stats(file_paths: list):
    raw_player_stats = []
    for file_path in file_paths:
        raw_player_stats += read_data_file(file_path)

    calculated_player_stats = calculate_raw_player_stats(raw_player_stats)

    headers = ['Player Name']
    headers += get_attack_stats_headers()
    headers += get_block_stats_headers()
    headers += get_assist_stats_headers()
    headers += get_free_ball_stats_headers()
    headers += get_dig_stats_headers()
    headers += get_serve_receive_stats_headers()
    headers += get_serve_stats_headers()

    total_player_stats = []
    for player in ALL_PLAYERS:
        player_stat = PlayerStat(player, calculated_player_stats)
        
        total_player_stat = [player_stat.name]
        total_player_stat += collect_attack_stats(player_stat)
        total_player_stat += collect_block_stats(player_stat)
        total_player_stat += collect_assist_stats(player_stat)
        total_player_stat += collect_free_ball_stats(player_stat)
        total_player_stat += collect_dig_stats(player_stat)
        total_player_stat += collect_serve_receive_stats(player_stat)
        total_player_stat += collect_serve_stats(player_stat)

        total_player_stats.append(total_player_stat)

    all_stats = [headers] + total_player_stats
    print_stats_csv('./results/total_stats.csv', all_stats)

if __name__ == "__main__":
    cleaned_file_paths = [
        './results/day_1/chicago_united_773_set_1_cleaned.txt',
        './results/day_1/chicago_united_773_set_2_cleaned.txt',
        './results/day_1/ngun_lam_white_set_1_cleaned.txt',
        './results/day_1/ngun_lam_white_set_2_cleaned.txt',
        './results/day_1/sf_dragons_og_set_1_cleaned.txt',
        './results/day_1/sf_dragons_og_set_2_cleaned.txt',
        './results/day_1/sams_club_set_1_cleaned.txt',
        './results/day_1/sams_club_set_2_cleaned.txt',
        './results/day_2/montreal_freemason_m2_set_1_cleaned.txt',
        './results/day_2/montreal_freemason_m2_set_2_cleaned.txt',
        './results/day_2/ny_vikings_red_set_1_cleaned.txt',
        './results/day_2/ny_vikings_red_set_2_cleaned.txt',
        './results/day_2/ny_vikings_red_set_3_cleaned.txt',
        './results/day_2/phi_cia_c_set_1_cleaned.txt',
        './results/day_2/phi_cia_c_set_2_cleaned.txt',
        './results/day_2/phi_cia_c_set_3_cleaned.txt',
        './results/day_2/sf_dragon_og_set_1_cleaned.txt',
        './results/day_2/sf_dynasty_daddies_set_1_cleaned.txt',
        './results/day_2/sf_dynasty_daddies_set_2_cleaned.txt',
        './results/day_2/sf_dynasty_daddies_set_3_cleaned.txt',
        './results/day_3/sf_dynasty_impact_set_1_cleaned.txt',
        './results/day_3/sf_dynasty_impact_set_2_cleaned.txt',
    ]
    sams_club_file_paths = [
        './results/day_1/sams_club_set_1_cleaned.txt',
        './results/day_1/sams_club_set_2_cleaned.txt',
    ]
    calculate_set_stats(sams_club_file_paths)
    calculate_total_stats(cleaned_file_paths)