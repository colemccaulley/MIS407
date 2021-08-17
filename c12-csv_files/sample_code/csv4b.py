"""Example reading of a csv file."""

import csv
with open('sample3.csv') as csvFile:
    sampleReader = csv.reader(csvFile)
    headers = next(sampleReader)
    total_due = 0
    for row in sampleReader:
        print('Row #' + str(sampleReader.line_num) + ": " + row[3])
        total_due += float(row[3])
    print("Total due: {}".format(total_due))
