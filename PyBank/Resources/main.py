import os
import csv
#set the path for file
#csvpath=os.path.join("PyBank/Resources/budget_data.csv")
csvpath= os.path.join("Resources", "budget_data.csv")
exportpath= os.path.join("Resources","Analysis","BudgetData.txt")

#list the variables I am looking for
Total_month=0
Total_pl=0
Monthly_Change_pl_List=[]
Greatest_Increase=0
Greatest_Increase_month=0
Greatest_Decrease=0
Greatest_Decrease_month=0
prev_pl=0
change_in_pl=0
#reading the file
with open (csvpath) as BudgetData:
        csvreader=csv.reader(BudgetData)
         #print(csvreader)
         #skip the header
        header=next(csvreader)
        first_row = next(csvreader)
        Total_month+=1
        Total_pl += int(first_row[1])
        prev_pl = int(first_row[1])
#Looping through the file to find variables
        for i in csvreader:
            Total_month+=1
            Total_pl+=int(i[1])
            Monthly_Change= int(i[1])- prev_pl
            prev_pl=int(i[1])
            Monthly_Change_pl_List.append(Monthly_Change)

            if Monthly_Change>Greatest_Increase:
                Greatest_Increase= Monthly_Change
                Greatest_Increase_month= (i[0])
            if Monthly_Change<Greatest_Decrease:
                Greatest_Decrease= Monthly_Change
                Greatest_Decrease_month=(i[0])
#Calculate average change 
Average_pl_change= sum(Monthly_Change_pl_List)/len(Monthly_Change_pl_List)

#print financial analysis
FinancialAnalysis = (
   f"Total Months:{Total_month}\n"
   f"Total Net Profitloss: {Total_pl}\n"
   f"Average Change:{Average_pl_change}\n"
   f"Greatest Increase:{Greatest_Increase_month, Greatest_Increase,}\n"
   f"Greatest Decrease:{Greatest_Decrease_month, Greatest_Decrease,}\n"
)
print(FinancialAnalysis)    

#exporting file
with open(exportpath, "w",) as txt_file:
    txt_file.write(FinancialAnalysis)