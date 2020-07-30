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

# 1. Load the data election_results.csv and read the file
with open(file_to_load) as election_data:

    # 2. Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # 3. Print each row in the CSV file
    for row in file_reader:
        print(row)


# 3. Export results to file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello World\nHiLove,HeyThere")
    # Display the number of votes casted
    # Display a complete list of candidates who recieved votes
    # Display the total number of votes recieved per candidate
    # Display the percentage of votes each candidate won
    # Display the winner of the election by popular vote
