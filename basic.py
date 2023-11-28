# Functions for importing, fully explained in basic.ipynb

import re
import json

def fetchData(path):
    with open(path, "r", encoding="utf8") as f:
        raw = f.read()
        data = json.loads(raw)

    return data

def cleanData(data):
    colorDict = {
        'W': [], # white
        'U': [], # blue
        'B': [], # black
        'R': [], # red
        'G': [], # green
        'colorless': [] # everything else
    }

    for i in data:

        # Skip joke cards
        if i['set_type'] == 'funny':
            pass

        # Clean \n and sub out cardname 
        if 'oracle_text' in i.keys():
            text = i['oracle_text'] 
            text = re.sub("\n", "", text)
            text = re.sub(re.escape(i['name']), "CARDNAME", text)
            i['oracle_text'] = text
        else:
            pass 

        # Put into color buckets
        colors = i['color_identity']
        if [] == colors:
            colorless.append(i)
            pass
        
        for color in colors:
            colorDict[color].append(i)
        
    return colorDict