# Election Audit
# Renata Hartman
# 2020/07/28

# 0. Prep Work
# Add dependencies
import csv
import os
# Assign a variable to load a file from a location
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to a location
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Assign a variable to track total count of votes
total_votes = 0
# Assign a list of the candidates names
candidate_options = []
# Declare a dictionary to capture votes per candidate
candidate_votes = {}
# Assign variable for winning candidate
winning_candidate = ""

# 1. Load the data election_results.csv and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        # add to the total voter count
        total_votes += 1
        # print the candidate name for each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidates
        if candidate_name not in candidate_options:
            # add candidate names to candidate list
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
    # Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")


# Print the total votes
print(total_votes)
print(candidate_options)
print(candidate_votes)


# 2. Export results to file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Election Analysis\n------------------------------")
    # Display the number of votes casted
    print(total_votes)
    # Display a complete list of candidates who recieved votes
    print(candidate_options)
    # Display the total number of votes recieved per candidate
    txt_file.write(f"{candidate_name}: received {votes} votes.")
    # Display the percentage of votes each candidate won
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        # Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Display the winner of the election by popular vote
