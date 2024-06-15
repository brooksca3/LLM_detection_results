import json
from openai import OpenAI
from gpt_key import gpt_key

# Set up the OpenAI client xwith the API key
# Sam - I put my key in gpt_key.py as a variable
client = OpenAI(api_key=gpt_key)

def remove_last_ratio_words(text, ratio):
    words = text.split()
    cutoff_index = int(len(words) * (1 - ratio))
    truncated_text = ' '.join(words[:cutoff_index])
    removed_text = ' '.join(words[cutoff_index:])
    return truncated_text, removed_text

def complete_press_release(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content.strip()

def generate_press_release_with_ratios(initial_text):
    ratios = [0, 1/3, 2/3, 1]
    results = {}
    for ratio in ratios:
        if ratio == 0:
            result = initial_text
        elif ratio == 1:
            # Summarize the article
            summary_prompt = f"Summarize the following press release in a single line:\n\n{initial_text}"
            summary = complete_press_release(summary_prompt)

            # Rewrite the article based on the summary
            word_count = len(initial_text.split())
            rewrite_prompt = f"Here is a summary of a {word_count}-word press release: {summary}\n\nRewrite the press release based on this summary."
            result = complete_press_release(rewrite_prompt)
        else:
            truncated_text, removed_text = remove_last_ratio_words(initial_text, ratio)
            prompt = f"{truncated_text}\n\nThis is the first {1-ratio:.2f} portion of the press release. Complete this press release with approximately {len(removed_text.split())} words."
            completion = complete_press_release(prompt)
            result = f"{truncated_text} {completion}"

        results[f"ratio_{int(ratio*3)}/3"] = result.strip()

    return results

def main():
    input_file = "sample_50.txt"
    output_file = "completed_press_releases.json"

    with open(input_file, "r") as file:
        press_releases = file.readlines()

    all_results = []
    for index, press_release in enumerate(press_releases):
        press_release = press_release.strip()
        if not press_release:
            continue
        print(f"Processing press release {index + 1}/{len(press_releases)}...")
        results = generate_press_release_with_ratios(press_release)
        all_results.append({"original": press_release, "results": results})

    with open(output_file, "w") as file:
        json.dump(all_results, file, indent=4)
    print(f"Saved all completed press releases to {output_file}")

if __name__ == "__main__":
    main()
