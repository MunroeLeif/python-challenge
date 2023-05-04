#Import modules
import os
import csv 

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #print(csvreader)

    #Read and store the header row 
    header = next(csvreader)
    #print(f"Header:{header}")

    #
    data = list(csvreader)
    row_count = len(data)
    #Set variable to hold total votes
    total_votes = []
    total_candidates = []
    tally = []
    #data = range(0,369711)
    #candidate_votes = {}
    #Stockham_index = []
    #Stockham_votes = str
    
    #Get candidates and votes
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in total_candidates:
            total_candidates.append(candidate)
    candidate_count = len(total_candidates)
    #Total votes for each candidate
    vote = []
    percentage = []
    for j in range(0, candidate_count):
        name = total_candidates[j]
        vote.append(tally.count(name))
        vprct = vote[j]/row_count
        percentage.append(vprct)
    
    
    
    #Dictionary
    won = max(vote)
    vote_breakdown = {}
    for x in range(len(total_candidates)):
        vote_breakdown[total_candidates[x]] = (format(percentage[x], '%'), vote[x])
        if vote[x] == won :
            winner = total_candidates[x]


    #Winner
    
            
    #Print the final message
    print(f'''
          Election Results
          -------------------
          Total Votes:{row_count}
          -------------------
          Charles Casper Stockham: {vote_breakdown['Charles Casper Stockham']}
          Diana DeGette: {vote_breakdown['Diana DeGette']}
          Raymon Anthony Doane: {vote_breakdown['Raymon Anthony Doane']}
          -------------------
          Winner: {winner}
          -------------------
          ''')
#Specify output path
txt_output_path = os.path.join("analysis", "analysis_pypoll.txt")

#write analysis file
f = open(txt_output_path, "w")
f.write(f'''
        Election Results
        -------------------
        Total Votes:{row_count}
        -------------------
        Charles Casper Stockham: {vote_breakdown['Charles Casper Stockham']}
        Diana DeGette: {vote_breakdown['Diana DeGette']}
        Raymon Anthony Doane: {vote_breakdown['Raymon Anthony Doane']}
        -------------------
        Winner: {winner}
        -------------------
        ''')
f.close()