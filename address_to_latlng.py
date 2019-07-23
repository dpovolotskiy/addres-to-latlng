import geocoder
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Path to input file (full or relative)", default="input.txt")
parser.add_argument("-o", "--output", help="Path to output file (full or relative). Must be JSON file.",
                    default="output.json")
args = parser.parse_args()

geo_list = []
with open(str(args.input), encoding="utf-8") as geo_data:
    for line in geo_data:
        geo_list.append(line.rstrip())

result = {}
for address in geo_list:
    g = geocoder.yandex(address)
    result[address] = g.latlng
with open(str(args.output), "w", encoding="utf-8") as output:
    output.write(json.dumps(result, ensure_ascii=False, indent=4))

print("Works done!")
