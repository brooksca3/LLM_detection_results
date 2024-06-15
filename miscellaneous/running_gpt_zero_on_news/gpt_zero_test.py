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

def test_single_file(file_path, output_folder):
    """Test the analysis on a single text file and save the result to a file."""
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Analyze the text
    result = analyze_text(text)

    # Add the filename to the result
    filename = os.path.basename(file_path)
    result['filename'] = filename

    # Save the result to a file
    output_file_path = os.path.join(output_folder, f"{filename.replace('.txt', '')}_result.json")
    with open(output_file_path, 'w') as output_file:
        json.dump(result, output_file, indent=2)

    # Print the filename of the saved result
    print(f"Saved: {output_file_path}")

# Example usage
file_path = "news/1_1.txt"  # Path to your single text file
output_folder = "test_results"  # Directory to save the result file
test_single_file(file_path, output_folder)
