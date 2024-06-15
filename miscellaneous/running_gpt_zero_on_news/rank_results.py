import os
import json

def get_human_scores_with_filenames(directory):
    """Extract 'human' scores and filenames from JSON files in the specified directory."""
    human_scores_with_filenames = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            # Read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)

                # Extract the 'human' score
                human_score = data['documents'][0]['class_probabilities']['human']
                human_scores_with_filenames.append((filename, human_score))

    return human_scores_with_filenames

def rank_human_scores(human_scores_with_filenames):
    """Rank the human scores from lowest to highest."""
    ranked_scores = sorted(human_scores_with_filenames, key=lambda x: x[1])

    # Print the ranked scores with filenames
    for rank, (filename, score) in enumerate(ranked_scores, start=1):
        print(f"Rank {rank}: {filename} - Human Score: {score}")

# Example usage
input_directory = "results"  # Directory containing the JSON files
human_scores_with_filenames = get_human_scores_with_filenames(input_directory)
rank_human_scores(human_scores_with_filenames)
