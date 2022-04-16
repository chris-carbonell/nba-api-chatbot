# Dependencies

# general
import csv
import logging

# NBA API ChatBot
from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))  # https://stackoverflow.com/questions/6323860/sibling-package-imports
import nba_api_chatbot.data.nba_api_constants as nac

# Logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":

    with open(nac.PATH_OUTPUT_TXT, "w") as f_txt, open(nac.PATH_OUTPUT_CSV, "w") as f_csv:

    	# get writer
        writer = csv.writer(f_csv, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        
        # Q: how many [stat] does [player name] have?
        # A: [player name] has [number] [stat]

        i = 0
        for player in nac.NBA_PLAYERS:
            for stat_id, stat_names in nac.STATS_ALL.items():
                for stat in stat_names:
                    for verb in ["did", "does"]:

                        query = f"how many {stat} {verb} {player['full_name']} have"

                        tokens = query.split(" ")

                        ner_tags = [nac._TAGS_INDEX['O']] * 2 + \
                            [nac._TAGS_INDEX['B-STAT']] + [nac._TAGS_INDEX['I-STAT'] for stat_part in stat.split(" ")[1:]] + \
                            [nac._TAGS_INDEX['O']] + \
                            [nac._TAGS_INDEX['B-PLAYER']] + [nac._TAGS_INDEX['I-PLAYER'] for name_part in player['full_name'].split(" ")[1:]] + \
                            [nac._TAGS_INDEX['O']]

                        logging.debug(f"{str(i).zfill(7)}, {query}")

                        # CSV
                        writer.writerow(
                            [
                                query,
                                player['full_name'],
                                stat_id,
                                tokens,
                                ner_tags
                            ] 
                        )

                        # TXT
                        f_txt.write(
                            str(len(tokens))
                            + "\t"
                            + "\t".join(tokens)
                            + "\t"
                            + "\t".join(map(str, ner_tags))
                            + "\n"
                        )

                        i += 1