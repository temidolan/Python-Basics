#Python_Challenge
import os
import csv

#set the path for file
csvpath=os.path.join("PyBank/Resources/budget_data.csv")
#list the variable I am looking for
Total_month=0
Total_Revenue=0
Monthly_Change_Revenue_List=[]
Monthly_Change=[]
Greatest_Increase=0
Greatest_Decrease=0
prev_change=0
Month_of_change=0

with open (csvpath) as BudgetData:
    csvreader=csv.reader(BudgetData, delimiter=",")
#print(csvreader)
#skip the header
    header=next(csvreader)
#list the variable I am looking for

    for i in csvreader:
        Total_month+=1
        Total_Revenue+=int(i[1])
        Monthly_Change= int(i[1])- prev_change
        prev_change=int(i[1])
        Monthly_Change_Revenue_List.append(Monthly_Change)
    print(Monthly_Change_Revenue_List)
    #Average_revenue_change= sum(Monthly_Change_Revenue_List)/len(Monthly_Change_Revenue_List)
    #print(Average_revenue_change)
    
