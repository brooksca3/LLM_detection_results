import pandas as pd

def count_long_reviews(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Fill NaN descriptions with an empty string to avoid errors
    df['DESCRIPTION'] = df['DESCRIPTION'].fillna('')

    # Function to count words in a string
    def word_count(description):
        return len(description.split())

    # Calculate the word count for each description
    df['WORD_COUNT'] = df['DESCRIPTION'].apply(word_count)

    # Filter out reviews shorter than 100 words
    long_reviews = df[df['WORD_COUNT'] >= 100]

    # Count the number of long reviews
    num_long_reviews = len(long_reviews)

    print(f'There are {num_long_reviews} reviews longer than 100 words.')

csv_file = 'amazon_data/train.csv'  # Replace with the actual path to your file
count_long_reviews(csv_file)
