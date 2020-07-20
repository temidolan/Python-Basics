#Python_Challenge2
import os
import csv

#set the path for the file
csvpath= os.path.join("Resources/election_data.csv")
exportpath= os.path.join("Resources","Analysis","Election_data.txt")
#setting my variables
Total_votes=0
Candidates_List=[]
Percentage_votes=0
Unique_candidate_list=[]
T_n_v_c=0

#reading the file
with open(csvpath) as Election_data:
    csvreader=csv.reader(Election_data)
    print(csvreader)
    Header=next(csvreader)
    first_candidate=next(csvreader)
    print(first_candidate)

    for i in csvreader:
        Total_votes+=1
        candidate_name=(i[2])
        Candidates_List.append(candidate_name)
    for i in Candidates_List:
        if i not in Unique_candidate_list:
            Unique_candidate_list.append(i)
print(Unique_candidate_list)
        #first_candidate=(i[2])
        #print(candidate_name)
        #if candidate_name in Candidates_List:
        #if candidate_name is not first_candidate[2]:
            #Candidates_List.append(candidate_name)
        #elif candidate_name != first_candidate[2]:
           # Candidates_List.append(candidate_name)
        #else:
           # Candidates_List.append(candidate_name)
        
        #print(Candidates_List)
#List variables for total count for candidates
correy=0
khan=0
li=0
OTooley =0

for i in Candidates_List:
    if Unique_candidate_list[0]==i:
        correy+=1
    elif Unique_candidate_list[1]==i:
        khan+=1
    elif Unique_candidate_list[2]==i:
        li+=1
    elif Unique_candidate_list[3]==i:
        OTooley+=1
print(correy,khan,li,OTooley)



    