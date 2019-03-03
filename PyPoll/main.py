#######**PyPOLL**#######

 #Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    rowCount = 0

    for row in csvreader:
        rowCount += 1
    print(rowCount)
