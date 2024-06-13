import os
import re
from collections import defaultdict

# Define the directory containing the text files
directory = 'binoculars_scores'

# Define the score threshold
score_threshold = 0.901

# Initialize a dictionary to hold counts of total lines and low score lines per year
yearly_counts = defaultdict(lambda: {'total': 0, 'low_score': 0})

# Define a regular expression pattern to extract the date and score from each line
pattern = re.compile(r'\("(.*?)", ([0-9.]+)\)')

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)

        with open(filepath, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    date_str = match.group(1)
                    score = float(match.group(2))

                    # Extract the year from the date string using regex
                    year_match = re.search(r'\b(\d{4})\b', date_str)
                    if year_match:
                        year = year_match.group(1)

                        # Update total line count for the year
                        yearly_counts[year]['total'] += 1

                        # Update low score line count for the year if score is 0.901 or lower
                        if score <= score_threshold:
                            yearly_counts[year]['low_score'] += 1

# Sort years and calculate the percentage of low score lines per year
sorted_years = sorted(yearly_counts.keys())

# Print results in order by year
for year in sorted_years:
    counts = yearly_counts[year]
    total_lines = counts['total']
    low_score_lines = counts['low_score']
    percentage = (low_score_lines / total_lines) * 100 if total_lines > 0 else 0
    print(f"Year: {year}, Total lines: {total_lines}, Low score lines: {low_score_lines}, Percentage: {percentage:.2f}%")
