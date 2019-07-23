import time
from tqdm import tqdm
import geocoder
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Path to input file (full or relative)", default="input.txt")
parser.add_argument("-o", "--output", help="Path to output file (full or relative). Must be JSON file.",
                    default="output.json")
args = parser.parse_args()

address_list = []
with open(str(args.input), encoding="utf-8") as address_data:
    for address in address_data:
        address_list.append(address.rstrip())

coordinates = {}
for i in tqdm(range(len(address_list))):
    response = geocoder.yandex(address_list[i])
    while not response.ok:
        time.sleep(600)
        response = geocoder.yandex(address_list[i])
    coordinates[address_list[i]] = response.latlng

with open(str(args.output), "w", encoding="utf-8") as output:
    output.write(json.dumps(coordinates, ensure_ascii=False, indent=4))
