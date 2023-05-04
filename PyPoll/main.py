#Import modules
import os
import csv 

csvpath = os.path.join('..','..', 'Starter_Code', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #print(csvreader)

    #Read and store the header row 
    header = next(csvreader)
    #print(f"Header:{header}")

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
    print("Election Results")
    print("-------------------")
    print(f"Total Votes:{row_count}")
    print("-------------------")
    print(f"Charles Casper Stockham: {vote_breakdown['Charles Casper Stockham']}")
    print(f"Diana DeGette: {vote_breakdown['Diana DeGette']}")
    print(f"Raymon Anthony Doane: {vote_breakdown['Raymon Anthony Doane']}")
    print("-------------------")
    print(f"Winner: {winner}")
    print("-------------------")
    #print(candidate_count)
    #print(vote)
    #print (percentage)
    #print(total_candidates)
    #print(f'{vote_breakdown["Candidates"]} : {vote_breakdown["Votes"]} ({vote_breakdown["Percent"]})')


'''
 "Candidates": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"],
        "Votes": [85213, 272892, 11606],
        "Percent":['23.049%', '73.812%', '3.139%']
        }


    #Read through  each row after header row
    for row in csvreader:
        votes = [row[0]]
        total_votes.append(votes)
        candidates = [row[2]]
        
        
        
        #Gather unique candidate names
        for name in candidates:
            if name not in total_candidates:
               total_candidates.append(name)
            #Stockham_votes = candidates.count('Charles Casper Stockham')
   
     
            for candidate_name in total_candidates:
                if candidate_name.index("Charles Casper Stockham"):
                    Stockham_index = (candidate_name[index])
                        
          
        Stockham_index.append()
            candidate_name.
                Stockham_index.append(votes)
        #for can_name in total_candidates:
                    #if can_name 
                #dictionary practice
                    #Can_dict = {
                    #   "Name": [total_candidates] or ["Charles Casper Stockham", "Diana" etc]
                    #   "Votes": }
               

        Gather vote data for each candidate
        for vote in votes:
            if total_candidates.index('Charles Casper Stockham'):
                Stockham_votes.append(votes)
        '''

        #candidate_set = set(candidates)
        #candidate_list = (list(candidate_set))
        
        #charles_votes= total_candidates.index('Charles Casper Stockham')
        #Stockham_votes.append(votes)
        
        #candidates = sorted(row[2])
        #can = (candidates) 
        #for x in candidates:
            #print(x)
        #if (row[3]) != (row[3]):
            #print(candidates)
        


    
