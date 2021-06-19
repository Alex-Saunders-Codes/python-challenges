import os
import csv
#initialize a variable to store my csv data in
raw_data = []
#Store the filepath to be opened
file = "Resources/election_data.csv"

#I create a string to add as I go along that will be added to a txt doc at the end.
final_report = []

#I initialize this list so that I can calculate a winner at the end of the script.
winner_calc = []

#This Function will both print to the console, and add variables to my final report as I go along.
#I use .join(\n) to put a new line on the end of an f string.
def printGroup(fString):
    print(fString)
    final_report.append(fString)


#This function will calculate candidate statistics, and call printGroup to output them
def candidateFormat(name, list_object):
    #Here I use list comprehension to filter down to only the specified candidates votes.
    relevant_votes = [vote for vote in list_object if name in vote]
    #I take the length of the list to find how many votes were cast for this candidate.
    vote_number = len(relevant_votes)
    vote_percent = (vote_number / len(list_object)) * 100
    winner_calc.append([name, vote_number])
    printGroup(f"{name}: {vote_percent}% ({vote_number})")

#standard code to open a file and store it in our initialized variable.
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    for row in csvreader:
        raw_data.append(row)

printGroup("Election Results \n_______________________")
#Each row in our csv contains one vote, so we can just measure the length of our list of lists in raw data.
total_votes = len(raw_data)

#I use the printGroup function from last challenge throughout this challenge, for outputting data.
printGroup(f"Total Votes: {total_votes}")
#These are printed periodically for formatting.
printGroup("_______________________")

#I will use a slightly different method than I used in bankdata to find unique candidates.
#I did this differently because I realized that, if I iterated to the length of the list, but removed items as I went along like in pybank, I would go massively over my index.
voter_id, counties, candidates = zip(*raw_data)

unique_candidates = []
#Now I will iterate across my candidate array by index number.
for candidate in candidates:
    #Here I check if a candidate has already been found.
    if candidate not in unique_candidates:
        #If they have not, I add them to the list of unique candidates.
        unique_candidates.append(candidate)

#Now I will get statistics for each unique candidate.
for candidate in unique_candidates:
    candidateFormat(candidate, candidates)

printGroup("_______________________")

#This line calculates a winner.
#In order to do this, it calls "sorted" on my array of nested lists, and tells it that given an item in the list, sort upon the index 1 subitem.
#Finally, I calculate the winner by taking the first item in the returned list of lists.
winner = sorted(winner_calc, key = lambda x: x[1], reverse=True)

#I take the 0th item of winner because that is where the name is stored in the name/vote list.
printGroup(f"Winner: {winner[0][0]}")

printGroup("_______________________")

#Here, I write the final_report list to a new file. I use join to connect each part of the string, with \n as the seperator to create new lines.
with open("analysis/analysis.txt", "w") as analysis:
    analysis.write("\n".join(final_report))

