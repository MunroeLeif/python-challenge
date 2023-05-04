#Import modules
import os
import csv 

csvpath = os.path.join('..', 'PyBank', 'Resource', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read and store the header row 
    header = next(csvreader)

    #save total months in a list
    total_months = []
    #save net total in a list
    net_total = 0
    #defining previous profit
    previous_profit = 1088983
    #list to hold the montly changes in the profit column
    monthly_change = []

    #Read through  each row after header row
    for row in csvreader:
        #save row 1 in a tuple () and converting to an integer
        current_profit = int((row[1]))
        #populating the total_months list
        total_months.append(row[0])
        #calculating net_total
        net_total = (net_total + int(row[1]))
        #defining change 
        change = current_profit - previous_profit
        previous_profit = current_profit
        #populating the monthly change list with the values in change
        monthly_change.append(change)
        
    

    #Greatest increase
    Max = max(monthly_change)
    index_max = monthly_change.index(Max)
    max_month = (total_months[index_max])
    
     #average change
    average = round(sum(monthly_change) / (len(monthly_change)-1),2)
    
    #Greatest decrease
    Min = min(monthly_change)
    index_min = monthly_change.index(Min)
    min_month = (total_months[index_min])
    


    #print out message
    print(f'''
        Financial Analysis
        ---------------------------------
        Total Months: {len(total_months)}
        Total: ${net_total}
        Average Change: ${average}
        Greatest Increase in Profits: {max_month} (${Max})
        Greatest Decrease in Profits: {min_month} (${Min})
    ''')
    
 #Specify output path
txt_output_path = os.path.join("analysis", "analysis.txt")

 #open file
f = open(txt_output_path, "w")
f.write(f'''
        Financial Analysis
        ---------------------------------
        Total Months: {len(total_months)}
        Total: ${net_total}
        Average Change: ${average}
        Greatest Increase in Profits: {max_month} (${Max})
        Greatest Decrease in Profits: {min_month} (${Min})
    ''')
f.close()        
    
    