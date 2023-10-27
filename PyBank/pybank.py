import os
import csv
pathtocsv = os.path.join("./Resources", "budget_data.csv")
#here I am setting up my varaibles
tmonths = []
tprofits = []
total_changes = 0
monthly_changes = []
previous_value = None
month_change = 0
with open(pathtocsv) as path_to_csv:
    reader = csv.reader(path_to_csv, delimiter= ",") #reader will read everything at once, delimeter "," means comma seperated value
    header_to_csv = next(reader) #telling the reader you are going to skip the first line.  not needed.  Also saving the names to header csv. This is creating a value for the name
    greatest_increase_month = None #Keeps track of the greatest change from month to month / None means nothing.  None does not give it a specfic data type meaning you can use it for whatevr data type you want
    greatest_decrease_month = None #Keeps track of the greatest decrease from month to month
    count_of_changes = 0 #keep track of how many changes have been done
    greatest_increase = 0 # Greatest overall increase
    greatest_decrease = 0 #greatest overall decrease
    for y in reader: #going over the reader line by line
        #print(y)
        profit_changes = float(y[1]) #y is the line by line reader that will have values in a list form.  float(y[1]) means profit/change losses y[0] would be the dates
        if previous_value is not None: #this logic will start from the second iteration and will hold as true
            month_change = profit_changes - previous_value #subtracting profit and loss changes from this month from the previous month that will give me a months change
            if month_change > greatest_increase: #the first loop through this logic will hold as true.
                greatest_increase = month_change
            if month_change < greatest_decrease:
                greatest_decrease = month_change
            if month_change == greatest_increase:#checking if they are the same
                greatest_increase_month = y[0] #save this to the greatest increase month
            if month_change == greatest_decrease:
                greatest_decrease_month = y[0] #save this variable to the greatest decrease month
            total_changes += month_change #whatever change is happeneing in each month you're adding.  This is checking the overall change
            count_of_changes += 1 #counting how many changes have been done.  will be one less than the number on lines
        previous_value = profit_changes
        #The total number of months included in the dataset
        tmonths.append(y[0]) #adding a month to a list of months
        tprofits.append(int(y[1])) #as you created the list of profits, you add the profits to a list of profits.  Have to turn this to an integer or it will stay a string
    #print(len(tmonths))
  #The net total amount of "Profit/Losses" over the entire period
tprofits = (sum(tprofits)) #adding all the values within the list.  Takes all the values and adds them together and it will be saved to tprofits
average_month_change = total_changes / count_of_changes
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(tmonths)} ")
print(f"Total: ${tprofits}")
print(f"Average Change: ${round(average_month_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease)})")
    

    
     
     

