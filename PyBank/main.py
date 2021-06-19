import os
import csv
#initialize a variable to store my cvs data in
raw_data = []
#Store the filepath to be opened
file = "Resources/budget_data.csv"

#I create a string to add as I go along that will be added to a txt doc at the end.
final_report = ["Financial Analysis \n_______________________"]

#This Function will both print to the console, and add variables to my final report as I go along.
#I use .join(\n) to put a new line on the end of an f string.
def printGroup(fString):
    print(fString)
    final_report.append(fString)


#standard code to open a file and store it in our initialized variable.
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    for row in csvreader:
        raw_data.append(row)
#________________________________________________________
#MONTH NUMBER
#________________________________________________________
#This block aims to find the number of months in the dataset.
#With a brief visual inspection, I can see that in this case, there is only one instance of each month. 
#That means that I can measure the number of months by taking the overall length of the data like so.
month_number = len(raw_data)

#I dislike the specificity of this solution, and the assumption of only having unique months. 
#This is one way I might try to solve it more generally. 

#Create a list with only the months stored in it. 
#I first explode the raw data, and then zip it into two lists (technically still zips).
#Then, I store those two lists into two variables for later use.
months, returnString = zip(*raw_data)

returns = [float(entry) for entry in returnString]

#Now I will iterate across that array by index number.
for i in range(len(months)):
    #Here I check if a month occurs in the array that follows it.
    if months[i] in months[i+1:]:
        #If a month does occur again, I remove the instance I have found.
        months.pop(i)
#Then I check how many unique months there are.
unique_month_number = len(raw_data)


printGroup(f"Total Months: {month_number}")

#This block can verify that the numbers returned by both methods are the same, 86.
#print(unique_month_number)

#____________________________________________
#Total Net Profit
#____________________________________________


#initialize a variable for total profit
total_profit = 0

#now I iterate over the seperate list of just money, and get the total profit.
for money in returns:
    total_profit += money

#If I hadn't created the earlier returns list, I would access the list of lists by adding [1] to the end of money.

printGroup(f"Total: ${total_profit}")

#______________________________________________
#Average Change
#______________________________________________
#First, I am going to create a list which holds the deltas between each value in the returns.
delta_return = []

#I need to truncate the range by 1, so that it does not try to find the delta for a future value.
for i in range(0, len(returns)-1):
    delta_return.append(returns[i + 1] - returns[i])

#Average Change should be very simple over the entire period - it is just the total change divided by the number of months.
average_change = (sum(delta_return))/len(delta_return)

printGroup(f"Average Change: ${average_change}")

#______________________________________________
#Increases and Decreases
#______________________________________________


#now I create a zipped object tieing dates back into the returns.
#Since I measured the change between month 1 and 0, and stored it in 0, I need to remove the first month from this.
#This makes sense, since the first month could not have had the greatest increase or decrease over the previous month.
delta_dates = list(zip(months[1:], delta_return))
#Maximum return can be found with .max() on the delta list.
#In this code block, I return the date - delta combo with the index number corresponding to the maximum entry in delta_return.
printGroup(f"Greatest Increase in Profits: {delta_dates[delta_return.index(max(delta_return))]}")

#In this code block, I return the date - delta combo with the index number corresponding to the maximum entry in delta_return.
printGroup(f"Greatest Increase in Profits: {delta_dates[delta_return.index(min(delta_return))]}")

#Here, I write the final_report list to a new file. I use join to connect each part of the string, with \n as the seperator to create new lines.
with open("analysis/analysis.txt", "w") as analysis:
    analysis.write("\n".join(final_report))






