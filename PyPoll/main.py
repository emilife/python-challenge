import os
import csv
infile = os.path.join("Resources", "election_data.csv")
percentage = []
total_votes = 0
winner_votes = 0
winner = " "
candidates = {}
with open(infile) as in_file:
    reader = csv.reader(in_file)
    header = next(reader) #so that when the for looop is reading the data it doesnt include the head as a value
    for x in reader: # this allows me to go line by line # this is the loop for the total number of votes for each candidate
        voter_id, county, candidate = x
        total_votes = total_votes + 1
        if candidate in candidates: #checking if i already added that condidate to the dictionary or not
            candidates [candidate] += 1 #whatever the value is here, just add 1
        else:
            candidates [candidate] = 1
for c,v in candidates.items(): #if you put candidtes without out items, it will over the keys
    percentage.append( (v / total_votes) * 100)
    if v > winner_votes:
        winner = c
        winner_votes = v
candidates_names = list(candidates.keys())   #the keys of candidates is the names of the candidates.  Taking the keys out of candidates and storing them into list
print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
i = 0
for c, v in candidates.items():
    print(f"{c}: {round(percentage[i],3)}% ({v})")
    i += 1
print("-------------------------")
print("Winner:", winner) #we have this variable winner in which we stored the name of the winner
print("-------------------------")