import csv

# defining initial values for the variables 

items = []
vote_list = []
final_vote = []
final_rate = []
max_vote = 0

# Assuming there is no specific info about how many nominates were participated in the voting. As well as the name of them. So in a comparing loop, it will be obtained: 
filepath = "Resources/election_data.csv"
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
# thus, in the vote_list all the nominations are listed
    for row in csvreader:
        if row[2] not in items:
            items.append(row[2])
        vote_list.append(row[2])

total_votes = len(vote_list)

# good practice to not forget the functions :)
def votecounting(vote, nominate):
    nominate_count = vote.count(nominate)
    return (nominate_count)

# the result will be written in a text file located in "analysis" folder and will not be shown in cmd, so its better to address it via a message!
print("The file runs successfully. Please find the results in 'analysis/output_file.txt' ")

with open('analysis/output_file.txt', 'w') as outfile:
    outfile.write(f"Election Results\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Total Votes: {len(vote_list)}\n")
    outfile.write(f"-------------------------\n")

    final_vote = [0] * len(items)
    final_rate = [0] * len(items)
# in a for loop , all votes for a specific nomination is counted and the max-number of votes which belongs to the winner is obtained  
    for item in items:
        index = items.index(item)
        final_vote[index] = votecounting(vote_list, str(item))
        final_rate[index]=100*final_vote[index]/len(vote_list)
        outfile.write(f"{item}: {final_rate[index]:.3f}% ({final_vote[index]})\n")
        if max_vote < final_vote[int(index)]:
            winner = str(item)
            max_vote = final_vote[int(index)]

    outfile.write(f"-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write(f"-------------------------\n")
