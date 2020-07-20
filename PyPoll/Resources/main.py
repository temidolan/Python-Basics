#Python_Challenge2
import os
import csv

#set the path for the file
csvpath= os.path.join("Resources/election_data.csv")

#reading the file
with open(csvpath) as Election_data:
    csvreader=csv.reader(Election_data)
    print(csvreader)