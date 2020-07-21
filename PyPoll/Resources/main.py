#Python_Challenge2
import os
import csv
#set the path for the file
csvpath= os.path.join("Resources/election_data.csv")
exportpath=os.path.join("Resources/Analysis/Election_result.txt")
#setting my variables
Total_votes=0
Candidates_List=[]
Percentage_list=[]
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
Output1= (f"Election Results\n" + f"-------------------------\n" + f"Total Votes: {Total_votes}\n" + f"-------------------------\n")
      
winning=list(set(candidate))
winning.sort()
voters=[]
for i in winning:
    voters.append(candidate.count(i))
        
for candidate_name in candidates_dict:
    votes = candidates_dict.get(candidate_name)
    Percentage_votes="{0:.00%}".format(votes/Total_votes)
    #print(Percentage_votes)
    Percentage_list.append(Percentage_votes)
    #print(Percentage_list)
winner=winning[voters.index(max(voters))]
Election_Results=""
count=0
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")
for i,x in candidates_dict.items():
    print (f"{i}: {Percentage_list[count]}   ({x})")
    Results = (f"{i}: {Percentage_list[count]}   ({x})\n")
    count+=1
    Election_Results+=Results
print("-------------------------")
print("winner: ",winner)
print("-------------------------")

Output2=(f"-------------------------\n" + f"winner:  {winner}\n" + f"-------------------------\n")
FinalAnalysis= (Output1 + Election_Results + Output2)
with open(exportpath, "w",) as txt_file:
        txt_file.write(FinalAnalysis)

