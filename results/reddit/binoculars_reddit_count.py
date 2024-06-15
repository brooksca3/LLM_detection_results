import re
from collections import defaultdict

# Initialize data structures
year_data = defaultdict(lambda: {'total_lines': 0, 'low_score_lines': 0})

# Read and process the file
file_path = "sorted_binoculars_reddit_comments_scores.txt"

with open(file_path, "r") as file:
    for line in file:
        # Extract the date and score using regex
        match = re.match(r'(\d{4})-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, (\d\.\d+)', line)
        if match:
            year = match.group(1)
            score = float(match.group(2))
            year_data[year]['total_lines'] += 1
            if score < 0.901:
                year_data[year]['low_score_lines'] += 1

# Generate and print the output
for year, counts in sorted(year_data.items()):
    total_lines = counts['total_lines']
    low_score_lines = counts['low_score_lines']
    percentage = (low_score_lines / total_lines) * 100 if total_lines > 0 else 0
    print(f"Year: {year}, Total lines: {total_lines}, AI detected lines: {low_score_lines}, Percentage: {percentage:.2f}%")
