import csv
import os

# NOTE: referenced following link for logic/approach
# https://www.geeksforgeeks.org/python-save-list-to-csv/

# Define path to source data/output file
csvpath = os.path.join('Resources','employee_data.csv')
outputpath = os.path.join('analysis','employee_converted_output.txt')

# Create list of output fields
output_fields = ['Emp ID','First Name','Last Name','DOB','SSN','State']

# Create empty list to store each row
output_rows = []

# Dictionary for state abbreviations
# Pulled from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open csv file in read mode
with open(csvpath) as csvfile:
    # Initiate csvreader object
    csvreader = csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(csvreader)
    for row in csvreader:
        # Create empty list to house individual record information after all transformations are performed
        record = []
        # Employee ID
        record.append(row[0])
        # First and last name - split the employee name using space as the split character
        name_split = row[1].split()
        first_name = name_split[0]
        last_name = name_split[1]
        # add first and last name to individual record list object
        record.append(first_name)
        record.append(last_name)
        # Parse the DOB to reformat into necessary output format
        dob_year = row[2][:4]
        dob_month = row[2][5:7]
        dob_day = row[2][-2:]
        # Reformat after extracting individual year, month, and day
        dob_new = f"{dob_month}/{dob_day}/{dob_year}"
        # add DOB to the individual record list object
        record.append(dob_new)
        # Parse the SSN to get last 4 digits, then obfuscate the rest
        last4_SSN = row[3][-4:]
        SSN_new = f"***-**-{last4_SSN}"
        # Add updated SSN format to individual list object
        record.append(SSN_new)
        # Use the state abbreviation dictionary to pull the state abbreviation based on state name
        state_new = us_state_abbrev[row[4]]
        # Add update state to the individual list object
        record.append(state_new)
        # Lastly, add individual record list to output list - to be used to write new reformatted file
        output_rows.append(record)

# List of output rows is created
# Now, write the reformatted list to an updated output file
# File called 'employee_converted_output.txt' and located in analysis folder
with open(outputpath,'w',newline='') as csvfile:
    # Initiate csvwriter object
    csvwriter = csv.writer(csvfile)
    # Write header rows
    csvwriter.writerow(output_fields)
    # Write data
    csvwriter.writerows(output_rows)