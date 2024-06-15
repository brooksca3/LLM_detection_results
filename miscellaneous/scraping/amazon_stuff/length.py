import pandas as pd
import matplotlib.pyplot as plt

def create_description_length_histogram(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Fill NaN descriptions with an empty string to avoid errors
    df['DESCRIPTION'] = df['DESCRIPTION'].fillna('')

    # Calculate the length of each description
    df['DESCRIPTION_LENGTH'] = df['DESCRIPTION'].apply(len)

    # Define the bin edges for increments of 100 up to 2000
    bins = list(range(0, 2100, 100))

    # Create a histogram of the description lengths
    plt.figure(figsize=(10, 6))
    plt.hist(df['DESCRIPTION_LENGTH'], bins=bins, edgecolor='k')
    plt.xlabel('Description Length')
    plt.ylabel('Frequency')
    plt.title('Histogram of Description Lengths in train.csv')
    plt.xticks(bins, rotation=45)
    plt.show()

csv_file = 'amazon_data/train.csv'  # Replace with the actual path to your file
create_description_length_histogram(csv_file)
