import pandas as pd
import os

# Define the directory and file names
directory = "kaggle_data"
file_names = [
    "reddit_opinion_climate_change.csv",
    "reddit_opinion_democrats.csv",
    "reddit_opinion_PSE_ISR.csv",
    "reddit_opinion_republican.csv"
]

# Iterate through each file and print the column names and first two rows
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    try:
        df = pd.read_csv(file_path, nrows=2)
        print(f"File: {file_name}")
        print("Columns:", df.columns.tolist())
        print("First two rows:")
        print(df.to_string(index=False), "\n")
    except Exception as e:
        print(f"Could not read {file_name}: {e}")
