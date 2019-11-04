import csv
import sys

tsvname = sys.argv[1]

def printrow(row):
    quoted = []
    for item in row:
        quoted.append('"' + item + '"')
    print '\t'.join(quoted)

with open(tsvname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            printrow(row)
            line_count += 1

