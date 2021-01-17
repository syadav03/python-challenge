import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
with open (election_csv, encoding='utf =8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    Total_rows = 0
    Total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for row in csvreader:
        if Total_rows == 0:
            Total_rows += 1
        else:
            Total_votes += 1 
        Total_rows += 1
        if row[2] == "Khan":
            Khan_votes +=1
        elif row[2] == "Correy":
            Correy_votes +=1
        elif row[2] == "Li":
            Li_votes +=1
        elif row [2] == "O'Tooley":
            OTooley_votes +=1
    
    Khan_percent = (Khan_votes/Total_votes)*100
    print (Total_votes)
    print(OTooley_votes)
    print (Khan_votes)
    print (Correy_votes)
    print (Li_votes)
    print (Khan_percent)
   