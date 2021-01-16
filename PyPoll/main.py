#import the csv file 
import os
import csv 
csv_path = os.path.join(".", "Resources", "PyPoll_Resources_election_data.csv")

with open(csv_path) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    
    #set initial values 
    row_count = 0
    candidates = []
     
    for rows in csvreader:
        #count the number of total votes cast 
        row_count += 1

        #add to list of candidates
        candidates.append(rows[2])
    
    #Get unique values from candidate list and call total_votes function
    unique_candidates = sorted(set(candidates))

    #function to calculate number of votes and percentage won
    def total_votes(name):
        total = candidates.count(name)
        percent_votes = candidates.count(name) / row_count * 100
        percent_votes = round(percent_votes, 4)
        total_votes = f"{name}: {percent_votes}% ({total} votes)"
        print(total_votes)    
    
    #loop each unique candidate through the original list and counts total votes 
    vote_count = [candidates.count(candidate) for candidate in unique_candidates]
    name = unique_candidates
    winner_count = max(vote_count) #finds highest voted for candidate 
    zip_candidates = zip(name, vote_count) 
    for row in zip_candidates:
        if row[1] == winner_count:
            winner = row[0]  
    
    #Store values
    winner = f"Winner: {winner}"       
    voters = f"Total votes: {row_count}"
    line_break = "-------------------------------------"
    

    #print analysis 
    print("Election Results")
    print(line_break)
    print(voters)
    print(line_break)
    results = [total_votes(candidate) for candidate in unique_candidates]
    print(line_break)
    print(winner)
    print(line_break)

    #export a text file with the results.
    output_path = os.path.join(".", "PyPoll_results.txt")
    new = "\n"
    with open(output_path, 'w') as text: 
        text.write("Election Results" + new)
        text.write(line_break + new)
        text.write(voters + new)
        text.write(line_break + new) 
        #text.write????????
        text.write(line_break + new)
        text.write(winner + new)
        text.write(line_break)