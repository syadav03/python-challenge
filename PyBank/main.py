import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

with open(budget_csv, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    # print (csvreader)
    Total_months= 0
    Total_rows = 0
    Profit_Loss = 0 
    Difference = []
    previous_row = []
    current_change = 0 
    greatestincamount = 0
    greatestincdate = " "
    greatestdecamount =  0
    greatestdecdate =  " "

    for row in csvreader:
        # print (row)
        
        if Total_rows == 0:
            Total_rows += 1
        else:
            Total_months = Total_months + 1
            
            Profit_Loss += int(row[1])
            if Total_rows > 1:
                current_change = int(row[1])- int(previous_row[1])
                Difference.append(current_change)
                # print ("diff", max(Difference), 'cha', current_change)    
                if current_change >= max(Difference):
                    greatestincamount = current_change
                    greatestincdate = row[0]
                if current_change <= min(Difference):
                    greatestdecamount = current_change
                    greatestdecdate= row[0]
            Total_rows += 1
            
        previous_row = row                
    average= sum(Difference)/len(Difference)
    # print (Total_rows)
    # print (Total_months)
    # print (Profit_Loss)
    # print (Difference)
    # print (average)
    # print ("ginc",greatestincamount)
    # print ("Date",greatestincdate)
    # print ("Dec", greatestdecamount)
    # print ("decdate", greatestdecdate)
    output= (
        f"Financial Analysis \n"
        f"----------------------------------------\n"
        f"Total Months: {Total_months} \n"
        f"Total: $ {Profit_Loss}\n"
        f"Average Change: $ {round(average,2)} \n"
        f"Greatest Increase in Profits: {greatestincdate} (${greatestincamount})\n"
        f"Greatest Decrease in Profits: {greatestdecdate} (${greatestdecamount})\n"
    )
    print (output)

    analysis_file = open("analysis/results.txt", "w")  
    analysis_file.write(output) 
    analysis_file.close()

