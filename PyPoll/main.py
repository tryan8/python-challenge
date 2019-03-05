#######**PyPOLL**#######

 #Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Khan = str
    Correy = str
    Li = str
    totalVotes = 0
    votesKhan = 0
    percentKhan = 0
    votesCorrey = 0
    percentCorrey = 0
    votesLi = 0
    percentLi = 0
    votesTooley = 0
    percentTooley = 0
    Winner = "Khan"

    for row in csvreader:
        totalVotes += 1
        if row[2] == 'Khan':
            votesKhan += 1
        elif row[2] == 'Correy':
            votesCorrey += 1
        elif row[2] == 'Li':
            votesLi += 1
        else:
            votesTooley += 1
    
    percentKhan = (votesKhan)/(totalVotes)*100
    percentKhan = round(percentKhan, 2)
    percentCorrey = (votesCorrey)/(totalVotes)*100
    percentCorrey = round(percentCorrey, 2)
    percentLi = (votesLi)/(totalVotes)*100
    percentLi = round(percentLi, 2)
    percentTooley = (votesTooley)/(totalVotes)*100
    percentTooley = round(percentTooley, 2)

    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(totalVotes))
    print("-----------------------")
    print("Kahn: " + str(percentKhan) + "% (" + str(votesKhan) + ")")
    print("Correy: " + str(percentCorrey) + "% (" + str(votesCorrey) + ")")
    print("Li: " + str(percentLi) + "% (" + str(votesLi) + ")")
    print("O'Tooley: " + str(percentTooley) + "% (" + str(votesTooley) + ")")
    print("-----------------------")
    print("Winner: " + str(Winner))
    print("-----------------------")
    
    
