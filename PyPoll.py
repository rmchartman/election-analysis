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
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

# 2. Export results to file
with open(file_to_save, "w") as txt_file:
    # Display the number of votes casted
    election_results = (
        f"Election Analysis\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")
    # Save the final count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        # Print out each candidate's name, vote count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Display a complete list of candidates who recieved votes
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(
            f"Candidates, Voter Percentage & Votes Per Candidate\n"
            f"\n"
            f"{candidate_results}\n"
            f"------------------------------\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


    # Display the winner of the election by popular vote
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

