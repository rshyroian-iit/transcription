### README.md
# Transcribe Script

This repository contains a Python script and a bash script to transcribe any audio or video file to text using OpenAI's transcription service. The audio is extracted and/or converted to MP3 format, chunked if necessary, and then transcribed.

## Prerequisites

- Python 3.x
- ffmpeg
- OpenAI API Key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/transcribe.git
cd transcribe
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

### 5. Set your OpenAI API key

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Usage

### 1. Ensure the bash script is executable

```bash
chmod +x transcribe.sh
```

### 2. Run the bash script with your input file

```bash
./transcribe.sh path/to/your/input_file
```

## Files

- `transcribe.py`: The main Python script that handles the conversion and transcription.
- `transcribe.sh`: A bash script to run the Python script from the terminal.
- `requirements.txt`: Lists the necessary dependencies for the Python script.
- `README.md`: This file.

## Script Details

The `transcribe.py` script performs the following steps:

1. Converts the input file (audio or video) to MP3 format using ffmpeg.
2. Chunks the MP3 file if it is longer than 5 minutes.
3. Transcribes each chunk using OpenAI's Whisper model.
4. Combines the transcriptions and saves them to `combined_transcriptions.txt`.
5. Cleans up intermediate files.

## Notes

- Make sure to replace `"your_api_key_here"` with your actual OpenAI API key.
- The script assumes the OpenAI API key is set as an environment variable.

## License

This project is licensed under the MIT License.

