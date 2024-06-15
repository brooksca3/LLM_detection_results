import re
from collections import defaultdict

# Initialize data structures
year_data = defaultdict(lambda: {'total_lines': 0, 'high_score_lines': 0})

# Read and process the file
file_path = "sorted_wiki_gptzero_results.txt"

with open(file_path, "r") as file:
    for line in file:
        # Extract the score and determine the year from the context
        match = re.match(r'.*?, (\d\.\d+), .*', line)
        if match:
            score = float(match.group(1))
            # Assume we are categorizing based on the current year since the year is not provided in the text.
            # Modify this to extract the year if that information is available in your context.
            year = "2023"  # Default year assumption
            year_data[year]['total_lines'] += 1
            if score > 0.5:
                year_data[year]['high_score_lines'] += 1

# Generate and print the output
for year, counts in sorted(year_data.items()):
    total_lines = counts['total_lines']
    high_score_lines = counts['high_score_lines']
    percentage = (high_score_lines / total_lines) * 100 if total_lines > 0 else 0
    print(f"Year: {year}, Total lines: {total_lines}, AI detected lines: {high_score_lines}, Percentage: {percentage:.2f}%")
