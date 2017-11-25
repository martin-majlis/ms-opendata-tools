#!/usr/bin/python3

# 0004A30B001EDCA9_json_v2.csv
# 0004A30B001F558A_json_v2.csv
# 0004A30B001F3844_json_v2.csv
# 0004A30B001EFCBB_json_v2.csv
# 0004A30B001EFC94_json_v2.csv
# 0004A30B001F04F9_json_v2.csv

"""

./rip_sensor.py data/0004A30B001EDCA9_json_v2.csv 0004A30B001EDCA9_sensor.csv
./rip_sensor.py data/0004A30B001F558A_json_v2.csv 0004A30B001F558A_sensor.csv
./rip_sensor.py data/0004A30B001F3844_json_v2.csv 0004A30B001F3844_sensor.csv
./rip_sensor.py data/0004A30B001EFCBB_json_v2.csv 0004A30B001EFCBB_sensor.csv
./rip_sensor.py data/0004A30B001EFC94_json_v2.csv 0004A30B001EFC94_sensor.csv
./rip_sensor.py data/0004A30B001F04F9_json_v2.csv 0004A30B001F04F9_sensor.csv


"""


import sys
import csv

inpF = sys.argv[1]
outF = sys.argv[2]

print("Input: %s; Out: %s" % (inpF, outF))


inpFH = open(inpF, newline='')

reader = csv.DictReader(inpFH)

data = []
for row in reader:
	proc = row
	# print(proc['data'])
	S_ID = int(proc['data'][0:2], 16)
	RSSI = int(proc['data'][2:4], 16)
	SNR = 128 - int(proc['data'][4:6], 16)
	BATERY = int(proc['data'][6:10], 16) / 1000.
	STATE = int(proc['data'][10:12], 16)
	COUNTER = int(proc['data'][12:14], 16)
	# print("%s - %s - %d" % (S_ID, STATE, COUNTER))

	proc['S_ID'] = S_ID
	proc['RSSI'] = RSSI
	proc['SNR'] = SNR
	proc['BATERY'] = BATERY
	proc['STATE'] = STATE
	proc['COUNTER'] = COUNTER

	data.append(proc)

keys = list(data[0].keys())
# data.remove('Timestamp')
keys = ['Timestamp'] + keys

with open(outF, 'w') as outFH:
    writer = csv.DictWriter(
        outFH,
        fieldnames=keys
    )

    writer.writeheader()
    for row in data:
        writer.writerow(row)


