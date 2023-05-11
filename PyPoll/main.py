import os
import csv

poll_data_csv = os.path.join("Resources", "election_data.csv")

#initializes lists to store data
voter_id = []
county = []
candidate = []

#read data to lists
with open(poll_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#total votes cast is length of voter_id minus 1 for header
total_votes = int(len(voter_id) - 1)

#initiate a null list to put the unique candidates in
unique_list = []

#find unique names of candidates
def unique(candidate):
    #go through elements in list and find unique ones; add them to the unique list
    for x in candidate:
        if x not in unique_list:
            unique_list.append(x)
    
    #remove first element from list
    del unique_list[0]

unique(candidate)


#initialize a null list to put count of each candidate into
count_candidate = []

#count instance ofeach unique candidate, ignoring first item in list, add this information to a count list
for can in unique_list: 
    count_candidate.append(candidate.count(can))
    
#change count to percentage
per_candidate = []
for can in count_candidate:
    round_num = round((can/total_votes)*100, 3)
    per_candidate.append(round_num)

#combine lists of unique_list, count_candidate, and per_candidate and print each
msg = []
for x, y, z in zip(unique_list, per_candidate, count_candidate):
    msg.append(str(x) + ": " + str(y) + "% (" + str(z) + ")")

#pick winner
high_num = max(count_candidate)
winner_index = count_candidate.index(high_num)
winner = unique_list[winner_index]

#add winner to string of what to print
msg.append("Winner: " + str(winner))

for every in msg:
    print(every)

#write output to file
winner_file = os.path.join("analysis", "winner.txt")
with open(winner_file, 'w') as f:
     f.write("\n" .join(str(item) for item in msg))

    
