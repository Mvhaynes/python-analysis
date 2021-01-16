#import the resource
import os
import csv 
csv_path = os.path.join(".", "Resources", "PyBank_Resources_budget_data.csv")

#open the csv file and skip the header
with open(csv_path) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #set initial values from first row 
    row = next(csvreader)
    row_count = 1
    net_total = int(row[1])
    monthly_return = int(row[1])
    previous_return = monthly_return
    changes = []
    months = [row[0]]

    #loop through rows 
    for rows in csvreader:
        
        #count number of rows 
        row_count += 1

        #add up net total profits/losses
        net_total = int(rows[1]) + net_total

        #calculate monthly change and add to changes list
        monthly_return = int(rows[1])    
        monthly_change = monthly_return - previous_return 
        changes.append(monthly_change) 
        
        #Reset value for previous_return 
        previous_return = monthly_return 

        #add date to months list 
        months.append(rows[0])

#find greatest increase and decrease and corresponding month
greatest_increase = max(changes) 
greatest_inc_index = int(changes.index(greatest_increase)) + 1 

greatest_decrease = min(changes)
greatest_dec_index = int(changes.index(greatest_decrease)) + 1
    
    
#calculate average change and store value 
avg_change = sum(changes) / len(changes)
avg_change = round(avg_change,2)
    
#store the values 
total_months = f"Total Months: {row_count}"
net_total = f"Total: ${net_total}"
avg_change = f"Average change: ${avg_change}"
greatest_inc = f"Greatest Increase in Profits: {months[greatest_inc_index]} ${greatest_increase}"
greatest_dec = f"Greates Decrease in Profits: {months[greatest_dec_index]} ${greatest_decrease}"
line_break = "-------------------------------------------------------------------"     

#Print analysis 
print("Financial Analysis")
print(line_break)
print(total_months)
print(net_total)
print(avg_change)
print(greatest_inc)
print(greatest_dec)
    
#export a text file with the results.
output_path = os.path.join(".", "PyBank_Analysis.txt")
new = "\n"
with open(output_path, 'w') as text: 
    text.write("Financial Analysis" + new)
    text.write(line_break + new)
    text.write(total_months + new)
    text.write(net_total + new)
    text.write(avg_change + new)
    text.write(greatest_inc + new)
    text.write(greatest_dec)
       



