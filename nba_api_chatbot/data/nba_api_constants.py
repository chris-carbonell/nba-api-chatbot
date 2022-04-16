# Dependencies

# NBA API
from nba_api.stats.static import players

# Constants

PATH_OUTPUT_TXT = "nba_api_chatbot/data/questions.txt"
PATH_OUTPUT_CSV = "nba_api_chatbot/data/questions.csv"

NBA_PLAYERS = players.get_players()

MAX_LEN = 15
PAD_WORD = "[PAD]"

# individual stats linking
# link stat key (e.g., "FGM") with colloquial names for the stat (e.g., "field goals")
GP = ["GP", "games played", "games"]
GS = ["GS", "games started"]
MIN = ["MIN", "minutes played", "minutes"]
FGM = ["FGM", "FG", "field goals made", "field goals"]
FGA = ["FGA", "field goals attempted", "attempts"]
FG_PCT = [
    "FG_PCT", "FG PCT", 
    "field goal percentage", "fg percentage",
    "field goal pct", "fg pct",
    "field goal %", "fg %"
    ] 
FG3M = [
    "FG3M", "3PM", 
    "three pointers made", "three pointers made", "three-pointers made", "3-pointers made", "3-pt made", 
    "three pointers", "three-pointers", "3-pointers", "3-pt"
    ]
FG3A = [
    "FG3A", "3PA", 
    "three pointers attempts", "three pointers attempts", "three-pointers attempts", "3-pointers attempts", "3-pt attempts", 
    "three pointers attempted", "three pointers attempted", "three-pointers attempted", "3-pointers attempted", "3-pt attempted", 
    "three pointers", "three-pointers", "3-pointers", "3-pt"
    ]
FG3_PCT = [
    "FG3_PCT", "FG3 PCT", 
    "three pointers percentage", "three pointers percentage", "three-pointers percentage", "3-pointers percentage", "3-pt percentage", 
    "three pointers pct", "three pointers pct", "three-pointers pct", "3-pointers pct", "3-pt pct", 
    "three pointers %", "three pointers %", "three-pointers %", "3-pointers %", "3-pt %"
    ]
FTM = ["FTM", "free throws made", "FT made"]
FTA = [
    "FTA", 
    "free throws attempts", "FT attempts",
    "free throws attempted", "FT attempted",
    ]
FT_PCT = [
    "FT_PCT", "FT PCT",
    "free throw percentage", "ft percentage",
    "free throw pct", "ft pct",
    "free throw %", "ft %"
    ] 
OREB = ["OREB", "offensive rebounds", "o rebounds"]
DREB = ["DREB", "defensive rebounds", "d rebounds"]
REB = ["REB", "rebounds", "total rebounds"] 
AST = ["AST", "assists", "assist"]
STL = ["STL", "steals", "steal"]
BLK = ["BLK", "blocks", "block"] 
TOV = ["TOV", "turnovers", "turnover"]
PF = ["PF", "personal fouls", "fouls"]
PTS = ["PTS", "PT", "points", "point"]

# stats groups

STATS_ALL = {
    'GP': GP,
    'GS': GS,
    'MIN': MIN,
    'FGM': FGM,
    'FGA': FGA,
    'FG_PCT': FG_PCT,
    'FG3M': FG3M,
    'FG3A': FG3A,
    'FG3_PCT': FG3_PCT,
    'FTM': FTM,
    'FTA': FTA,
    'FT_PCT': FT_PCT,
    'OREB': OREB,
    'DREB': DREB,
    'REB': REB,
    'AST': AST,
    'STL': STL,
    'BLK': BLK,
    'TOV': TOV,
    'PF': PF,
    'PTS': PTS
}

# STATS_LOOKUP
STATS_LOOKUP = {}
for stat_col, stat_names in STATS_ALL.items():
    for stat_name in stat_names:
        if stat_name not in STATS_LOOKUP:
            STATS_LOOKUP[stat_name] = stat_col

# get tag groups

# pair player names with tag
_NAMES = []
for player in NBA_PLAYERS:
    beginning_of_chunk = True
    for name_part in player['full_name'].split(" "):
        if beginning_of_chunk:
            _NAMES.append((name_part, "B-PLAYER"))
            beginning_of_chunk = False
        else:
            _NAMES.append((name_part, "I-PLAYER"))
_NAMES = list(set(_NAMES))  # keep unique only

# pair stats with tag
_STATS = []
for stat_col, stat_names in STATS_ALL.items():
    for stat_name in stat_names:
        beginning_of_chunk = True
        for stat_name_part in stat_name.split(" "):
            if beginning_of_chunk:
                _STATS.append((stat_name_part, "B-STAT"))
                beginning_of_chunk = False
            else:
                _STATS.append((stat_name_part, "I-STAT"))
_STATS = list(set(_STATS))  # keep unique only

_TAG_GRPS = _NAMES + _STATS

_TAGS = [PAD_WORD, "O"] + list(set(tag_grp[1] for tag_grp in _TAG_GRPS))

# _TAGS_INDEX = {t: i for i, t in enumerate(_TAGS)}
iob_labels = ["B", "I"]
ner_labels = ["PLAYER", "STAT"]
all_labels = [(label1, label2) for label2 in ner_labels for label1 in iob_labels]
all_labels = ["-".join([a, b]) for a, b in all_labels]
all_labels = [PAD_WORD, "O"] + all_labels
_TAGS_INDEX = dict(zip(all_labels, range(0, len(all_labels) + 1)))