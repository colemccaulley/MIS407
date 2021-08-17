"""Example reading of a csv file."""

import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    headers = next(sampleReader)
    print("Headers are: {}".format(headers))
    sampleData = list(sampleReader)
    print("First row of data: {}".format(sampleData[0][0:]))
