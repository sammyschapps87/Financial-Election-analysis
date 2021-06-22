import os
import csv


election_path = os.path.join('election_data.csv')
total_votes = 0 
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # header = next(csvreader)

    for row in csvreader:

        total_votes += 1 

        if row[2] == "Khan":
            votes_khan += 1

        elif row[2] == "Correy":
            votes_correy += 1 

        elif row[2] == "Li":
            votes_li += 1

        elif row[2] == "O'Tooley":
            votes_otooley += 1 

    percent_khan = (votes_khan/total_votes)*100
    percent_correy = (votes_correy/total_votes)*100
    percent_Li = (votes_li/total_votes)*100
    percent_otooley = (votes_otooley/total_votes)*100
    

# print(f"Khan: {votes_khan}")
# print(percent_khan)
# print("")
# print(f"Correy: {votes_correy}")
# print(percent_correy)
# print("")
# print(f"Li: {votes_li}")
# print(percent_Li)
# print("")
# print(f"O'tooley {votes_otooley}")
# print(percent_otooley)
# print("")
# print(total_votes)

election_dictionary = {
    "Khan": votes_khan,
    "Correy": votes_correy, 
    "Li": votes_li,
    "otooley": votes_otooley
}
max_votes = (max(list(election_dictionary.values())))
# print(list(election_dictionary.values()).index(max_votes))
winner = (list(election_dictionary.keys())[list(election_dictionary.values()).index(max_votes)])
election_results = f"""Election Results

-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {round(percent_khan, 1)}% ({votes_khan})
Correy: {round(percent_correy, 1)}% ({votes_correy})
Li: {round(percent_Li, 1)}% ({votes_li})
O'Tooley: {round(percent_otooley, 1)}% ({votes_otooley})
-------------------------
Winner: {winner}
-------------------------"""
print(election_results)
# csv.write("Election Results")
# csv.write('\n')