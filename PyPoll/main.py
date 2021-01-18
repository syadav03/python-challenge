import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
with open (election_csv, encoding='utf =8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
#Total_votes = 0
    Can_List = []
    Can_name = []
    Candidate = {}
    Highest_vote = 0
    Winner = " "
    #next(csvreader)
#     for col in csvreader:
# # calculating  total votes 
#         #Total_votes += 1 
#         # pulling candidate names 
#         Can_name = col[2]
#         if Can_name not in Can_List:
#             Can_List.append(Can_name)
#             Candidate[ Can_name] = 1 
#         else:
#             Candidate[ Can_name] += 1 
#     #print (Can_List)
#     for name in Can_List:
#         Candidate_votes = Candidate.get(name)
#         Candidate_percent = (Candidate_votes/Total_votes)*100 
#         #print (Candidate_percent)
#         #print (Candidate_votes)
#         #print (f' Candidate Name: {name},Votes for each Candidate: {Candidate_votes} ,Percentage {round(Candidate_percent,2)}%')

#     for votes in Candidate.keys():
#         #print (Candidate[votes])
#         if Candidate[votes] >Highest_vote:
#             Winner = votes
#             Highest_vote = Candidate[votes]
#             #print(Winner)
        
    
        
        



        





    # ============================================================
    Total_rows = 0
    Total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    
    Winner = " "
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
    Highest_vote = max(Khan_votes,Correy_votes,Li_votes,OTooley_votes)
    if Highest_vote == Khan_votes:
         Winner = "Khan"
    elif Highest_vote == Correy_votes:
         Winner = "Correy"
    elif Highest_vote == Li_votes:
         Winner = "Li"
    elif Highest_vote == OTooley_votes:
         Winner = "O'Tooley"

    Khan_percent = (Khan_votes/Total_votes)*100
    Correy_percent = (Correy_votes/Total_votes)*100
    Li_percent = (Li_votes/Total_votes)*100
    OTooley_percent = (OTooley_votes/Total_votes)*100
    # print (Total_votes)
    # print(OTooley_votes)
    # print (Khan_votes)
    # print (Correy_votes)
    # print (Li_votes)
    # print (Khan_percent)
    # print (Winner)

    output = (f"Election Results\n"
            f"----------------------------------\n"
            f"Total Votes: {Total_votes}\n"
            f"--------------------------------------\n"
            f"Khan: {round(Khan_percent,3)}% ({Khan_votes})\n"
            f"Correy: {round(Correy_percent,3)}% ({Correy_votes})\n"
            f"Li: {round(Li_percent,3)}% ({Li_votes})\n"
            f"O'Tooley: {round(OTooley_percent,3)}% ({OTooley_votes})\n"
            f"-----------------------------------------------------\n"
            f"Winner = {Winner}"
            )
    print(output)



    election_file = open("analysis/election_results.txt", "w")  
    election_file.write(output) 
    election_file.close()