# Imports
import os
import csv

# Define path to source data
csvpath = os.path.join('Resources','budget_data.csv')

# Create initial counter for total # of months in file
total_months = 0
total_profit_loss = 0

# Open csv file in read mode
with open(csvpath) as csvfile:
    # Initiate csvreader object
    csvreader = csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(csvreader)
    # Iterate through csvreader data records and perform relevant calculations
    for row in csvreader:
        # total months in file
        total_months += 1
        # total profit/losses in each file
        total_profit_loss += float(row[1])

# Print output results
print("Financial Analysis\n---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${int(total_profit_loss)}")