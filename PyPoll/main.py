# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources','election_data.csv')

# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Initialize variables

# Stores the total number of votes cast in the election. It is initialized to 0
total_votes = 0
# Empty dictionary that will store the vote count for each candidate.
candidate_votes = {}

# Open and read the CSV file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        
        # Count the total number of votes
        total_votes += 1

        # Extract the candidate name from the third column of the current row
        candidate = row[2]

        # Check if the candidate already exists in the candidate_votes dictionary
        if candidate in candidate_votes:
            # If the candidate already exists, increment their vote count by 1
            candidate_votes[candidate] += 1
        else:
            # If candidate's name does not exist, add the candidate to the candidate_votes dictionary with an initial vote count of 1
            candidate_votes[candidate] = 1

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")


# Calculate and show the percentage of votes each candidate won, as well as their total votes
# Loop iterates over each key-value pair in the candidate_votes dictionary
# The 'candidate' variable stores the key (candidate name)
# The 'votes' variable stores the corresponding value (vote count)
for candidate, votes in candidate_votes.items():
   
    # calculates percentage of votes for each candidate by dividing their vote count by the total number of votes * 100
    percentage = (votes / total_votes) * 100
   
    # Displays candidate name, percentage of votes, and their total number of votes
    # Format specifier ':.3f' used to be formatted three decimal places
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

# Finds the winner based on most votes
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")

print("-------------------------")

# Save the analysis results to a text file
output_file = "election_analysis.txt"

# Open file in write mode
with open(output_file, "w") as txtfile:
    
    # Write header and separators
    # Whenever '/n' is used, it instructs the program to move over to the next line after that point
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    
    # Write total number of votes
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    
    # Write percentage of votes for each candidate
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        # Write name of candidate, percentage of votes, and total amount of their votes 
        # Format specifier ':.3f' used to be formatted three decimal places
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    # Loop ends
    
    # Write name of the winner with most votes
    # Whenever '/n' is used, it instructs the program to move over to the next line after that point
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
