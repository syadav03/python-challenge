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
            Total_votes = Total_votes + 1 
        Total_rows += 1
        
        

    
        

            

    print (Total_votes)
   