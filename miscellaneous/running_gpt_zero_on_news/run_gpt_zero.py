import os
import requests
import json

def analyze_text(document_text):
    """Send text to the GPTZero API and get analysis results."""
    # API endpoint
    url = "https://api.gptzero.me/v2/predict/text"

    # Headers
    headers = {
        'Content-Type': 'application/json',
        # REMOVED API KEY FROM CODE
        'x-api-key': 'removed'
    }

    # Data payload
    data = {
        "document": document_text,
        "version": "2024-01-09",
        "multilingual": False
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=data)

    # Check for successful request and return the JSON response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def process_text_files(directory, output_folder):
    """Process text files in the specified directory and save results to the output folder."""
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all text files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)

            # Read the text file
            with open(file_path, 'r') as file:
                text = file.read()

            # Analyze the text
            result = analyze_text(text)

            # Add the filename to the result
            result['filename'] = filename

            # Save the result to a file
            output_file_path = os.path.join(output_folder, f"{filename.replace('.txt', '')}_result.json")
            with open(output_file_path, 'w') as output_file:
                json.dump(result, output_file, indent=2)

            # Print the filename of the saved result
            print(f"Saved: {output_file_path}")

# Example usage
input_directory = "news"  # Directory containing the text files
output_directory = "results"  # Directory to save the result files
process_text_files(input_directory, output_directory)
