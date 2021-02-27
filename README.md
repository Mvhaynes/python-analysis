# python-analysis

Scripts for analyzing election data and financial records. 

## PyBank 

This script analyzes financial records from the data set [PyBank_Resources_budget_data.csv]. 

The script loops through rows of data to collect the total number of records and calculates the net revenue over the entire period and add those values to a final analysis summary. The final analysis summary includes the average net change in revenue and the greatest changes to profits and losses and their corresponding dates. 

Final Analysis Summary: 

    Financial Analysis
    -------------------------------------------------------------------
    Total Months: 86
    Total: $38382578
    Average change: $-2315.12
    Greatest Increase in Profits: Feb-2012 $1926159
    Greates Decrease in Profits: Sep-2013 $-2196167

## PyPoll

This script analyzes a large data set [PyPoll_Resources_election_data.csv] to create a summary analysis table that includes the total number of votes, a list of candidates and their outcomes, and the final winner based on popular votes. 

    Election Results
    -------------------------------------
    Total votes: 3521001
    -------------------------------------
    Correy: 20.0% (704200 votes)
    Khan: 63.0% (2218231 votes)
    Li: 14.0% (492940 votes)
    O'Tooley: 3.0% (105630 votes)
    -------------------------------------
    Winner: Khan
-------------------------------------
