
# pull wikidata ids from enries and combine into single data payload.

import json
import pandas
import pathlib
import requests
import time
import tqdm

wikidata_json = pathlib.Path.cwd() / 'wikidata.json'
if not wikidata_json.exists():

    wikidata_array = list()
    df = pandas.read_csv(pathlib.Path.cwd() / 'entries.csv')
    for x in tqdm.tqdm([x for x in df.wikidata.unique() if 'Q' in str(x)]):

        time.sleep(4)

        r = requests.get(f'https://www.wikidata.org/wiki/Special:EntityData/{x}.json')
        if r.status_code != 200:
            raise Exception('Wikidata query failure.')
        wikidata_array.append(json.loads(r.text))

    with open(wikidata_json, 'w', encoding="utf-8") as export:
        json.dump(wikidata_array, export, indent=4, ensure_ascii=False)
