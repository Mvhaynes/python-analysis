#import the csv file 
import os
import csv 
csv_path = os.path.join(".", "Resources", "PyPoll_Resources_election_data.csv")

with open(csv_path) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    
    #set initial values 
    row = next(csvreader)
    row_count = 1
    candidates = []
    
    
    
    for rows in csvreader:
        #count the number of total votes cast 
        row_count += 1

        #add to list of candidates 



#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.