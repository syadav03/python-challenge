import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

with open(budget_csv, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    print (csvreader)

    for row in csvreader:
        print (row)

    