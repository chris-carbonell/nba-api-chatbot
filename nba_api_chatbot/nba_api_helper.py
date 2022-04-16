# Dependencies

# text
import Levenshtein

# NBA API
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players

# NBA API ChatBot
from nba_api_chatbot.data import nba_api_constants as nac

# Funcs

def find_player_by_name_fuzzy(name, threshold: int = 3):
    '''
    get player ID by player name using fuzzy matching (Levenshtein distance)
    '''
        
    # find matches
    ls_matches = []
    for player in nac.NBA_PLAYERS:
        
        ld = Levenshtein.distance(name.lower(), player['full_name'].lower())
        # lr = Levenshtein.ratio(name.lower(), player['name'].lower())
        
        if ld == 0:
            return player
        
        if ld <= threshold:
            ls_matches.append((player, ld))
            
    # find smallest distance
    if len(ls_matches) > 0:
        return min(ls_matches, key = lambda i : i[1])[0]
    else:
        return None
        
    return None

def get_total_stat_for_one_player(player_name: str, stat: str):
    '''
    get sum of a stat for the entire career of a player

    Q: how many [stat] does [player name] have?
    A: [player name] has [number] [stat]

    player_name = "Tim Duncan"
    stat = "PTS"
    '''

    try:
        player = find_player_by_name_fuzzy(player_name)
        career = playercareerstats.PlayerCareerStats(player_id=player['id'])
        df_career = career.get_data_frames()[0]
        return df_career[stat].sum()
    except:
        return None