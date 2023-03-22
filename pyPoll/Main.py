import os
import csv
#imports
total = 0
candidates = []
cand_1 = 0
cand_2 = 0
cand_3 = 0
votes = []
#creating variables

file_path = "Resources/election_data.csv"
#reads file and opens
with open(file_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #skips first line 

    for row in csvreader:
        total += 1
        #each row has one vote so total increments by one

        if row[2] not in candidates:
            candidates.append(row[2])
        votes.append(row[2])

    #creates a list of candidates by adding their name if it already not present
    #creates a list of all votes as well

for i in votes:
    if(i == candidates[0]):
        cand_1 += 1
    elif(i == candidates[1]):
        cand_2 += 1
    else:
        cand_3 += 1
#if the persons vote matches with the peoples name in the candidate list, then it adds one to their votes

cand_1_percent = round((cand_1/total) * 100,3) 
cand_2_percent = round((cand_2/total) * 100,3)
cand_3_percent = round((cand_3/total) * 100,3)
#finds percentages by dividing persons votes by total votes

#print statements to terminal
print("election results")
print("-----------------------------------------")
print("Total votes: " + str(total))
print("-----------------------------------------")
print(candidates[0]+ ": " + str(cand_1_percent) + " (" + str(cand_1) + ")")
print(candidates[1]+ ": " + str(cand_2_percent) + " (" + str(cand_2) + ")")
print(candidates[2]+ ": " + str(cand_3_percent) + " (" + str(cand_3) + ")")
print("-----------------------------------------")
if(cand_1 > cand_2 and cand_3):
    print("Winner: " + candidates[0])
elif(cand_2 > cand_1 and cand_3):
    print("Winner: " + candidates[1])
else:
    print("Winner: " + candidates[2])
print("-----------------------------------------")

output_file =  "analysis/results.txt"
#print statement to output file
with open(output_file, "w") as datafile:
    datafile.write
    datafile.write("election results" + "\n")
    datafile.write("-----------------------------------------" + "\n")
    datafile.write("Total votes: " + str(total) + "\n") 
    datafile.write("-----------------------------------------" + "\n")
    datafile.write(candidates[0]+ ": " + str(cand_1_percent) + " (" + str(cand_1) + ")"+ "\n")
    datafile.write(candidates[1]+ ": " + str(cand_2_percent) + " (" + str(cand_2) + ")"+ "\n")
    datafile.write(candidates[2]+ ": " + str(cand_3_percent) + " (" + str(cand_3) + ")"+ "\n")
    datafile.write("-----------------------------------------"+ "\n")
    if(cand_1 > cand_2 and cand_3):
        datafile.write("Winner: " + candidates[0]+ "\n")
    elif(cand_2 > cand_1 and cand_3):
        datafile.write("Winner: " + candidates[1]+ "\n")
    else:
        datafile.write("Winner: " + candidates[2]+ "\n")
    datafile.write("-----------------------------------------"+ "\n")





