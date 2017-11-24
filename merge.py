#!/usr/bin/python3
import csv
import datetime
import iso8601
import re
import sys


# Budeme pouzivat vzorkovani po 15 minutach
GRANULARITY = 60 * 15


def loadData(fName):
    fh = open(fName, newline='')
    reader = csv.DictReader(fh)

    result = []

    DEV_KEY = None
    DEV_ID = None

    for row in reader:
        if DEV_KEY is None:
            if 'DevEUI' in row:
                DEV_KEY = 'DevEUI'
            elif 'EUI' in row:
                DEV_KEY = 'EUI'
            else:
                raise ValueError(
                    "Neznamy typ vstupniho souboru. Chybi kod zarizeni.")
            DEV_ID = row[DEV_KEY]

        proc = {
            'TS': iso8601.parse_date(row['Timestamp']).timestamp()
        }
        for k, v in row.items():
            if k == DEV_KEY:
                continue
            k = re.sub(r' \[.*', '', k).strip().replace(' ', '_')
            proc[DEV_ID + "-" + k] = v

        result.append(proc)

    return result


def saveData(fName, data, columns):
    with open(fName, 'w') as csvFile:
        writer = csv.DictWriter(
            csvFile,
            fieldnames=['TS', 'TS_H'] + sorted(columns)
        )

        writer.writeheader()
        for k in sorted(data.keys()):
            writer.writerow(data[k])


combined = {}
columns = {}

for i in range(2, len(sys.argv)):
    print("Processing input file %s" % sys.argv[i], file=sys.stderr)
    single = loadData(sys.argv[i])
    rowId = 0
    for rec in single:
        # Najdi nove sloupecky
        if rowId == 0:
            for k, v in rec.items():
                columns[k] = 1

        # Zaokrouhli time stamp
        # Spoj data dohromady
        ts = int(rec['TS'] - rec['TS'] % GRANULARITY)
        if ts not in combined:
            combined[ts] = rec
            combined[ts]['TS'] = ts
            combined[ts]['TS_H'] = datetime.datetime.fromtimestamp(ts).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        else:
            for k, v in rec.items():
                combined[ts][k] = v

        rowId += 1

saveData(sys.argv[1], combined, columns.keys())
