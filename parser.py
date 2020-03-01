
import csv

with open('eggs.csv', newline='') as csvfile:
    cases_reader = csv.reader(csvfile, delimiter=',')

    for row in cases_reader:
        print(row)
