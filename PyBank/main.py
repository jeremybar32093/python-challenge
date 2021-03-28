#NOTE: Used https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
# for reference in developing logic for this HW

# Imports
import os
import csv

# Define path to source data/output file
csvpath = os.path.join('Resources','budget_data.csv')
outputpath = os.path.join('analysis','financial_analysis.txt')

# Create initial counter for total # of months in file
total_months = 0
total_profit_loss = 0

# Create empty list to store revenue and revenue change values
# Will be used to calculate average/min/max change 
revenue_values = []
revenue_change_values = []
# Create empty list to store dates 
# Will be used to calculated average/min/max change dates
date_values = []

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
        # create 2 lists containing revenue and dates
        # Then can calculate averages in separate loop and also use indices to find min/max dates
        revenue_values.append(float(row[1]))
        date_values.append(row[0])

# Loop through revenue values and calculate change month over month
# Exclude last month from this calculation since there is no subsequent month to compare to
for i in range(0,len(revenue_values)-1):
    monthly_change = revenue_values[i+1] - revenue_values[i]
    revenue_change_values.append(monthly_change)

# Calculate average change
average_revenue_change = sum(revenue_change_values) / len(revenue_change_values)
average_revenue_change_format = "{:.2f}".format(average_revenue_change)

# Calculate maximum change
max_change = max(revenue_change_values)
# To get the date, reference the date list created in csvreader loop
# Based on how the monthly changes were calculated, the changes tied to each row correspond to the subsequent month
# Thus, the max change date is the index in the date list of the max_change + 1
max_change_date = date_values[(revenue_change_values.index(max_change))+1]
# reformat max_change_date to "Mmm-YYYY" instead of "Mmm-YY" using list properties of string
max_change_date_format = max_change_date[:4] + "20" + max_change_date[-2:]

# Calculate minimum change
min_change = min(revenue_change_values)
# To get the date, reference the date list created in csvreader loop
# Based on how the monthly changes were calculated, the changes tied to each row correspond to the subsequent month
# Thus, the max change date is the index in the date list of the max_change + 1
min_change_date = date_values[(revenue_change_values.index(min_change))+1]
# reformat min_change_date to "Mmm-YYYY" instead of "Mmm-YY" using list properties of string
min_change_date_format = min_change_date[:4] + "20" + min_change_date[-2:]

# Print output results
print("Financial Analysis\n---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${int(total_profit_loss)}")
print(f"Average Change: ${average_revenue_change_format}")
print(f"Greatest Increase in Profits: {max_change_date_format} (${int(max_change)})")
print(f"Greatest Decrease in Profits: {min_change_date_format} (${int(min_change)})")


# Output analysis results to text file
with open(outputpath, 'w', newline='') as text_file:
    text_file.write("Financial Analysis\n---------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${int(total_profit_loss)}\n")
    text_file.write(f"Average Change: ${average_revenue_change_format}\n")
    text_file.write(f"Greatest Increase in Profits: {max_change_date_format} (${int(max_change)})\n")
    text_file.write(f"Greatest Decrease in Profits: {min_change_date_format} (${int(min_change)})")
    