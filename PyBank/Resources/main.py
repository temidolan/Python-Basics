#Python_Challenge
import os
import csv

#set the path for file
csvpath=os.path.join("PyBank/Resources/budget_data.csv")
#list the variable I am looking for
Total_month=0
Total_pl=0
Monthly_Change_pl_List=[]
Greatest_Increase=0
Greatest_Monthly_Increase=0
Greatest_Decrease=0
Greatest_Monthly_Decrease=0
prev_pl=0
Month_of_change=[]
change_in_pl=0

with open (csvpath) as BudgetData:
    csvreader=csv.reader(BudgetData, delimiter=",")
#print(csvreader)
#skip the header
    header=next(csvreader)
#list the variable I am looking for

    for i in csvreader:
        Total_month+=1
        Total_pl+=int(i[1])
        Monthly_Change= int(i[1])- prev_pl
        prev_pl=int(i[1])
        #Month_of_change+=(i[0])
        Monthly_Change_pl_List.append(Monthly_Change)
        if int(i[1])>Greatest_Increase:
            Greatest_Increase= int(i[1])
            Greatest_Monthly_Increase= (i[0])
        if int(i[1])<Greatest_Decrease:
            Greatest_Decrease= int(i[1])
            Greatest_Monthly_Decrease=(i[0])
Average_pl_change= sum(Monthly_Change_pl_List)/Total_month
#print(Average_pl_change)
#Print Financial Analysis
FinancialAnalysis = (
    f"Total Months:{Total_month}\n"
    f"Total Net Profitloss: {Total_pl}\n"
    f"Average Change:{Average_pl_change}\n"
    f"Greatest Increase:{Greatest_Increase, Greatest_Monthly_Increase}\n"
    f"Greatest Decrease:{Greatest_Decrease,Greatest_Monthly_Decrease}\n"
)
print(FinancialAnalysis)