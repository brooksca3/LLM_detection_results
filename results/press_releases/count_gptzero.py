import os
import json
from collections import defaultdict

# Define the parent directory containing country directories
parent_directory = 'gptzero_scores'

# Define the score threshold
score_threshold = 0.5

# Initialize a dictionary to hold counts of total files and low score files per year
yearly_counts = defaultdict(lambda: {'total': 0, 'low_score': 0})

# Iterate through all country directories in the parent directory
for country_dir in os.listdir(parent_directory):
    country_path = os.path.join(parent_directory, country_dir)
    if os.path.isdir(country_path):
        # Iterate through all JSON files in the country directory
        for filename in os.listdir(country_path):
            if filename.endswith(".json"):
                file_path = os.path.join(country_path, filename)

                # Extract the year from the file name
                try:
                    date_str = filename.split('_')[1].split('.')[0]
                    year = date_str.split()[-1]
                except IndexError:
                    continue

                # Read the JSON file
                with open(file_path, 'r') as file:
                    data = json.load(file)

                    # Get the "human" score from the JSON data
                    try:
                        human_score = data["documents"][0]["class_probabilities"]["human"]
                    except (KeyError, IndexError):
                        continue

                    # Update total file count for the year
                    yearly_counts[year]['total'] += 1

                    # Update low score file count for the year if score is 0.5 or lower
                    if human_score <= score_threshold:
                        yearly_counts[year]['low_score'] += 1

# Calculate and print the percentage of low score files per year
for year in sorted(yearly_counts.keys()):
    counts = yearly_counts[year]
    total_files = counts['total']
    low_score_files = counts['low_score']
    percentage = (low_score_files / total_files) * 100 if total_files > 0 else 0
    print(f"Year: {year}, Total files: {total_files}, Low score files: {low_score_files}, Percentage: {percentage:.2f}%")
