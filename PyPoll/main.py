import os
import csv

# Define path to source data/output file
csvpath = os.path.join('Resources','election_data.csv')
outputpath = os.path.join('analysis','election_analysis.txt')

# Create initial variables
total_votes = 0
candidates = []
candidate_number_votes = []
candidate_percent_votes = []

with open(csvpath) as csvfile:
    # Initiate csvreader object
    csvreader = csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(csvreader)
    # Iterate through csvreader data records and perform relevant calculations
    for row in csvreader:
        # total votes in file
        total_votes += 1
        # obtain unique list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])

# Now, iterate through each unique candidate, loop through the CSV file again and count the number of votes for each candidate
# Append this result into its own list
# Also, calculate the percentage votes for each candidate
for candidate in candidates:
    candidate_vote_count = 0
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        next(csvreader)
        for row in csvreader:
            if row[2] == candidate:
                candidate_vote_count += 1
    # Append number of votes for each candidate to list
    candidate_number_votes.append(candidate_vote_count)
    # Append percent votes formatted to 3 decimal places to list
    candidate_percent_votes.append("{:.3%}".format((candidate_vote_count / total_votes)))

# print output results
print("Election Results\n----------------------------")
print(f"Total Votes: {total_votes}\n----------------------------")

# Iterate through number of candidates and print out #/% of votes
for i in range(0,len(candidates)):
    print(f"{candidates[i]}: {candidate_percent_votes[i]} ({candidate_number_votes[i]})")

print("\n----------------------------")

