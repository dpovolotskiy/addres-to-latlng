import time
import geocoder
import argparse

from progressbar import *


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Path to input file (full or relative)", default="input.txt")
parser.add_argument("-o", "--output", help="Path to output file (full or relative).", default="output.txt")
args = parser.parse_args()


sys.stderr = open('nul', "w")
address_list = []
with open(str(args.input), encoding="utf-8") as address_data:
    for address in address_data:
        address_list.append(address.rstrip())

open(str(args.output), 'w').close()
output = open(str(args.output), "a", encoding="utf-8")

for i in range(len(address_list)):
    progress(i, len(address_list), status='Processing')
    response = geocoder.yandex(address_list[i])
    while not response.ok:
        time.sleep(600)
        response = geocoder.yandex(address_list[i])
    output.write("{}: POINT ({} {})\n".format(address_list[i], response.lng, response.lat))
    output.flush()

output.close()
