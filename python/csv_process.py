#!/usr/bin/env python3
import csv
import sys

csvname = sys.argv[1]
delim   = sys.argv[2]

def printrow(row):
    quoted = []
    for item in row:
        quoted.append('"' + item + '"')
    print(delim.join(quoted))

with open(csvname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delim)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            printrow(row)
            line_count += 1

