import pandas as pd

def print_first_two_rows(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Use the option context to display all columns
    with pd.option_context('display.max_columns', None):
        print(df.head(2))

csv_file = 'amazon_data/train.csv'  # Replace with the actual path to your file
print_first_two_rows(csv_file)
