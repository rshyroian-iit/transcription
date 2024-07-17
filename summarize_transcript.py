import os
import sys
from anthropic import Anthropic

MODEL_NAME = "claude-3-opus-20240229"

def read_transcript(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_completion(client, prompt):
    return client.messages.create(
        model=MODEL_NAME,
        max_tokens=4000,
        messages=[{
            "role": 'user', 
            "content": prompt
        }]
    ).content

def summarize_with_claude(client, transcript):
    prompt = f"""Here is a transcript: <transcript>{transcript}</transcript>
Please provide a detailed summary of the transcript. Include these sections:
1. Summary: A comprehensive overview of the main topics discussed.
2. Key Points: Bullet points of the most important information.
3. Key Dates and Deadlines: Any mentioned dates or deadlines, with context.
4. Notes: Any additional important information that doesn't fit into the other categories.
5. Action Items: Any tasks or follow-up actions mentioned or implied in the transcript.
Please format your response in Markdown."""

    try:
        return get_completion(client, prompt)
    except Exception as e:
        print(f"Error summarizing transcript: {str(e)}")
        return None

def main(transcript_file):
    client = Anthropic()  # Make sure to set your API key as an environment variable
    transcript = read_transcript(transcript_file)
    summary = summarize_with_claude(client, transcript)
    
    if summary:
        output_file = "transcript_summary.md"
        with open(output_file, "w") as outfile:
            outfile.write(summary)
        print(f"Summary created and saved as '{output_file}'")
    else:
        print("Failed to create summary.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarize_transcript.py <transcript_file>")
    else:
        main(sys.argv[1])
