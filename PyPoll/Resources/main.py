#Python_Challenge2
import os
import csv
#set the path for the file
csvpath= os.path.join("Resources/election_data.csv")
#setting my variables
Total_votes=0
Candidates_List=[]
Percentage_votes=[]
Unique_candidate_list=[]
candidates_dict = {}
candidate=[]
#Total_votes_0f_candidates=[]
#reading the file
with open(csvpath) as Election_data:
    csvreader=csv.reader(Election_data)
    print(csvreader)
    header=next(csvreader)
    for i in csvreader:
        Total_votes+=1
        candidate.append(i[2])
        candidate_name= i[2]
        if candidate_name not in Unique_candidate_list:
            Unique_candidate_list.append(i[2])
            candidates_dict[i[2]]= 1
            #add new candidate to dictionary and give them a value of 1
        else:
            candidates_dict[i[2]]=candidates_dict[i[2]] + 1
            # else if the candidate is already in the candiate list, 
            #just add one to their value
#print(candidates_dict)
winning=list(set(candidate))
winning.sort()
voters=[]
for i in winning:
    voters.append(candidate.count(i))
        
for candidate_name in candidates_dict:
    votes = candidates_dict.get(candidate_name)
    Percentage_votes=(votes/Total_votes)*100
    #print(Percentage_votes)
winner=winning[voters.index(max(voters))]
print("winner: ",winner)

# #for candidate_name in candidates_dict:
#     #print(candidate_name + )

# #exportingprintstatement
# #analysis =print(
# #f"Election Results\n"
# #f"--------------------\n"
# #f"Total Votes: {total_votes}\n"
# #f"{}\n"
# #f"-------------------------\n"
# f"winner:{winner}\n"
# f"------------------------"
# )
