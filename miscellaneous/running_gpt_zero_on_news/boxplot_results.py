import os
import json
import matplotlib.pyplot as plt

def get_human_scores(directory):
    """Extract 'human' scores from JSON files in the specified directory."""
    human_scores = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            # Read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)

                # Extract the 'human' score
                human_score = data['documents'][0]['class_probabilities']['human']
                human_scores.append(human_score)

    return human_scores

def plot_boxplot(human_scores):
    """Generate a boxplot of the 'human' scores."""
    plt.figure(figsize=(10, 6))
    plt.boxplot(human_scores, vert=True, patch_artist=True)
    plt.title('Boxplot of Human Scores')
    plt.ylabel('Human Score')
    plt.show()

# Example usage
input_directory = "results"  # Directory containing the JSON files
human_scores = get_human_scores(input_directory)
plot_boxplot(human_scores)
