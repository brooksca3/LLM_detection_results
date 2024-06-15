import pandas as pd
import matplotlib.pyplot as plt
import os
import json

# Load the sampled comments JSON file
directory = "kaggle_data"
file_name = "sampled_comments.json"
file_path = os.path.join(directory, file_name)

with open(file_path, 'r') as json_file:
    comments_list = json.load(json_file)

# Convert to DataFrame
df = pd.DataFrame(comments_list)
df['created_time'] = pd.to_datetime(df['created_time'])

# Plot histograms for each source
sources = df['source'].unique()

for source in sources:
    source_df = df[df['source'] == source]
    plt.figure(figsize=(10, 6))
    plt.hist(source_df['created_time'], bins=30, edgecolor='black')
    plt.title(f"Histogram of Comment Dates for {source}")
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plot_file_name = source.replace('.csv', '_histogram.png')
    plot_file_path = os.path.join(directory, plot_file_name)
    plt.savefig(plot_file_path)
    plt.close()

    print(f"Histogram saved to {plot_file_path}")
