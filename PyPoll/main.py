import os
import csv

# Define path to source data/output file
csvpath = os.path.join('Resources','election_data.csv')
outputpath = os.path.join('analysis','election_analysis.txt')

# Create initial variables
total_votes = 0

with open(csvpath) as csvfile:
    # Initiate csvreader object
    csvreader = csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(csvreader)
    # Iterate through csvreader data records and perform relevant calculations
    for row in csvreader:
        # total votes in file
        total_votes += 1

# print output results
print("Election Results\n----------------------------")
print(f"Total Votes: {total_votes}\n----------------------------")