# Transcribe and Summarize Script

This repository contains Python scripts and bash scripts to transcribe any audio or video file to text using OpenAI's transcription service, and then summarize the transcript using Anthropic's Claude API.

## Prerequisites

- Python 3.x
- ffmpeg
- OpenAI API Key
- Anthropic API Key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/transcribe-and-summarize.git
cd transcribe-and-summarize
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python3 -m venv transcribe_env
source transcribe_env/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg

#### On Ubuntu

```bash
sudo apt-get install ffmpeg
```

#### On macOS

```bash
brew install ffmpeg
```

### 5. Set your API keys

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
export ANTHROPIC_API_KEY="your_anthropic_api_key_here"
```

## Usage

### 1. Ensure the bash scripts are executable

```bash
chmod +x transcribe.sh summarize_transcript.sh
```

### 2. Run the transcription script with your input file

```bash
./transcribe.sh path/to/your/input_file
```

### 3. Run the summarization script with the transcribed file

```bash
./summarize_transcript.sh combined_transcriptions.txt
```

## Files

- `transcribe.py`: The main Python script that handles the conversion and transcription.
- `transcribe.sh`: A bash script to run the transcription Python script from the terminal.
- `summarize_transcript.py`: A Python script that summarizes the transcript using Claude API.
- `summarize_transcript.sh`: A bash script to run the summarization Python script from the terminal.
- `requirements.txt`: Lists the necessary dependencies for the Python scripts.
- `README.md`: This file.

## Script Details

### Transcribe Script

The `transcribe.py` script performs the following steps:

1. Converts the input file (audio or video) to MP3 format using ffmpeg.
2. Chunks the MP3 file if it is longer than 5 minutes.
3. Transcribes each chunk using OpenAI's Whisper model.
4. Combines the transcriptions and saves them to `combined_transcriptions.txt`.
5. Cleans up intermediate files.

### Summarize Script

The `summarize_transcript.py` script performs the following steps:

1. Reads the transcription file.
2. Sends the transcript to Claude API for summarization.
3. Generates a detailed summary including:
   - A comprehensive overview of the main topics discussed
   - Key points
   - Key dates and deadlines
   - Notes
   - Action items
4. Saves the summary as a Markdown file named `transcript_summary.md`.

## Notes

- Make sure to replace `"your_openai_api_key_here"` and `"your_anthropic_api_key_here"` with your actual API keys.
- The scripts assume the API keys are set as environment variables.

## License

This project is licensed under the MIT License.
