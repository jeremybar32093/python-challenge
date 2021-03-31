# python-challenge

This repo contains 4 main folders, each of which include separate python scripts and outputs given certain data/folder structures structures as input. The individual folders are as follows:
* PyBank
* PyBoss
* PyParagraph
* PyPoll

Details of each folders' purpose is as follows:

## PyBank

This script will read in a dataset called **budget_data.csv** containing 2 columns: **Date** and **Profit/Losses**. The **main.py** file within the **PyBank** folder will calculate the following, both printing the result to the terminal as well as to a separate output .txt file:

* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period

As an example, the output will look something like the following:
  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
  
  ## PyBoss
  This script will read in a dataset called **employee_data.csv** with the following format:
  ```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```
The **main.py** file within the **PyBoss** folder will then parse through this file and output into a separate file with a new format as follows:
```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

## PyParagraph
The **main.py** file within this folder will take in a paragraph as input in the **paragraph** variable. The script will then parse through this input and print a summary analysis table containing the following:
* Approximate word count
* Approximate sentence count
* Approximate letters per word
* Apprixmate words per sentence

As an example, the output will look something like the following:
```output
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
```
This output will be both printed to the terminal as well as output to a separate .txt file.

## PyPoll
This script will read in a dataset called **election_data.csv** containing 3 columns: **Voter ID**, **County** and **Candidate**. The **main.py** file within the **PyPoll** folder will calculate the following, both printing the result to the terminal as well as to a separate output .txt file:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

As an example, the output will look something like the following:
  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------

