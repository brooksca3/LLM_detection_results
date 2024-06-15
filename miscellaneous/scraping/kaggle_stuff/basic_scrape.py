import pandas as pd
import os
import json
from datetime import datetime

# Define the directory and file names
directory = "kaggle_data"
file_names = [
    "reddit_opinion_climate_change.csv",
    "reddit_opinion_democrats.csv",
    "reddit_opinion_PSE_ISR.csv",
    "reddit_opinion_republican.csv"
]

# Number of comments to sample
n = 5

# Function to check if comment has at least 100 words
def is_long_enough(comment):
    if isinstance(comment, str):
        return len(comment.split()) >= 100
    return False

# Function to filter and sample comments based on date
def filter_and_sample(df, n, boundary_date):
    before_comments = df[df['created_time'] <= boundary_date]
    after_comments = df[df['created_time'] > boundary_date]

    print(f"Total comments before {boundary_date}: {len(before_comments)}")
    print(f"Total comments after {boundary_date}: {len(after_comments)}")

    before_sample = before_comments[before_comments['self_text'].apply(is_long_enough)]
    after_sample = after_comments[after_comments['self_text'].apply(is_long_enough)]

    print(f"Total long comments before {boundary_date}: {len(before_sample)}")
    print(f"Total long comments after {boundary_date}: {len(after_sample)}")

    if len(before_sample) > 0:
        before_sample = before_sample.sample(n=min(n, len(before_sample)), random_state=1)
    if len(after_sample) > 0:
        after_sample = after_sample.sample(n=min(n, len(after_sample)), random_state=1)

    return pd.concat([before_sample, after_sample])

# Iterate through each file and create JSON output
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    try:
        df = pd.read_csv(file_path, parse_dates=['created_time'], dtype={'comment_id': str, 'score': int, 'self_text': str,
                                                                         'subreddit': str, 'post_id': str, 'author_name': str,
                                                                         'controversiality': int, 'ups': int, 'downs': int,
                                                                         'user_is_verified': str, 'user_account_created_time': str,
                                                                         'user_awardee_karma': float, 'user_awarder_karma': float,
                                                                         'user_link_karma': float, 'user_comment_karma': float,
                                                                         'user_total_karma': float, 'post_score': float,
                                                                         'post_self_text': str, 'post_title': str,
                                                                         'post_upvote_ratio': float, 'post_thumbs_ups': float,
                                                                         'post_total_awards_received': float, 'post_created_time': str})
        df = df.dropna(subset=['self_text'])  # Drop rows where 'self_text' is NaN

        boundary_date = datetime(2022, 12, 31)
        sample_df = filter_and_sample(df, n, boundary_date)

        # Create list of dictionaries for JSON output
        comments_list = sample_df[['created_time', 'self_text']].to_dict(orient='records')

        # Define output file name
        output_file_name = file_name.replace('.csv', '_sampled_comments.json')
        output_file_path = os.path.join(directory, output_file_name)

        # Write to JSON file
        with open(output_file_path, 'w') as json_file:
            json.dump(comments_list, json_file, indent=4, default=str)

        print(f"Sampled comments saved to {output_file_path}")

    except Exception as e:
        print(f"Could not process {file_name}: {e}")
