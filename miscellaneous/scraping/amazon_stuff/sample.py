import pandas as pd
import json

def sample_long_reviews(csv_file, output_file, sample_size=10000):
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

    # Sample 10,000 long reviews
    sample_reviews = long_reviews.sample(n=sample_size, random_state=42)

    # Convert the sample to a list of dictionaries
    reviews_list = sample_reviews[['PRODUCT_ID', 'TITLE', 'DESCRIPTION', 'PRODUCT_TYPE_ID', 'PRODUCT_LENGTH']].to_dict(orient='records')

    # Save the list to a JSON file
    with open(output_file, 'w') as f:
        json.dump(reviews_list, f, indent=4)

    print(f'Sample of {sample_size} reviews saved to {output_file}')

csv_file = 'amazon_data/train.csv'  # Replace with the actual path to your file
output_file = 'sampled_reviews.json'  # Output JSON file name
sample_long_reviews(csv_file, output_file)
