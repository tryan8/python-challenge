#######**PyBANK**#######

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read total number of months included in the dataset
    #Calculate the net total amount of "Profit/Losses" over the entire period
    rowCount = 0
    profit = []
    date = []
    profitChange = []
    averageProfitChange = 0
    for row in csvreader:
        rowCount += 1
        profit.append(float(row[1]))
        date.append(row[0])
        totalProfit = sum(profit)
    
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months: " + str(rowCount))
    print("Total: $" + str(totalProfit))

    for i in range(1,rowCount):
        profitChange.append(profit[i] - profit[i-1])
    
    averageProfitChange = sum(profitChange)/(rowCount-1)
    print("Average Change: " + "$" + str(round(averageProfitChange, 2)))
    maxProfitChange = max(profitChange)
    minProfitChange = min(profitChange)
    maxIndex = profitChange.index(maxProfitChange)
    minIndex = profitChange.index(minProfitChange)
    

    
    print("Greatest Increase in Profits: " + str(date[maxIndex+1]) + " ($" + str(maxProfitChange) + ")")
    print("Greatest Decrease in Profits: " + str(date[minIndex+1]) + " ($" + str(minProfitChange) + ")")
    
    

    

    

        
    