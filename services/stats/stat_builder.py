from constants.action_qualities import ALL_QUALITIES
from constants.action_types import *
from models.assist_stats import AssistStats
from models.block_stats import BlockStats
from models.dig_stats import DigStats
from models.free_ball_stats import FreeBallStats
from models.attack_stats import AttackStats
from models.serve_receive_stats import ServeReceiveStats
from models.serve_stats import ServeStats

def calculate_raw_player_stats(raw_player_stats: list):
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
        
    return calculated_player_stats

def build_player_assist_stats(player_number: int, calculated_player_stats: list) -> AssistStats: 
    player_assist_stats = calculated_player_stats[player_number]["actions"][SET]["qualities"]
    return AssistStats(player_assist_stats)

def build_player_attack_stats(player_number: int, calculated_player_stats: list) -> AttackStats:
    player_attack_stats = calculated_player_stats[player_number]["actions"][ATTACK]["qualities"]
    return AttackStats(player_attack_stats) 

def build_player_block_stats(player_number: int, calculated_player_stats: list) -> BlockStats:
    player_block_stats = calculated_player_stats[player_number]["actions"][BLOCK]["qualities"]
    return BlockStats(player_block_stats) 
    
def build_player_dig_stats(player_number: int, calculated_player_stats: list):
    player_dig_stats = calculated_player_stats[player_number]["actions"][DIG]["qualities"]
    return DigStats(player_dig_stats) 

def build_player_free_ball_stats(player_number: int, calculated_player_stats: list):
    player_freeBall_stats = calculated_player_stats[player_number]["actions"][FREE_BALL]["qualities"]
    return FreeBallStats(player_freeBall_stats) 

def build_player_serve_receive_stats(player_number: int, calculated_player_stats: list):
    player_serve_receive_stats = calculated_player_stats[player_number]["actions"][SERVE_RECEIVE_PASS]["qualities"]
    return ServeReceiveStats(player_serve_receive_stats) 
    
def build_player_serve_stats(player_number: int, calculated_player_stats: list):
    player_serve_stats = calculated_player_stats[player_number]["actions"][SERVE]["qualities"]
    return ServeStats(player_serve_stats) 