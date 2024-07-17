import os
import sys
from openai import OpenAI
import ffmpeg
from pydub import AudioSegment

def convert_to_mp3(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file, acodec='libmp3lame', format='mp3').run()
        return True
    except ffmpeg.Error as e:
        print(f"Error converting {input_file} to MP3: {e.stderr.decode()}")
        return False

def chunk_audio(audio_path, chunk_duration_ms=5*60*1000):
    try:
        audio = AudioSegment.from_mp3(audio_path)
        chunks = []
        for i, chunk in enumerate(audio[::chunk_duration_ms]):
            chunk_path = f"chunk_{i+1}.mp3"
            chunk.export(chunk_path, format="mp3")
            chunks.append(chunk_path)
        return chunks
    except Exception as e:
        print(f"Error chunking audio {audio_path}: {str(e)}")
        return []

def transcribe_audio(client, audio_path):
    try:
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcription.text
    except Exception as e:
        print(f"Error transcribing {audio_path}: {str(e)}")
        return None

def main(input_file):
    client = OpenAI()  # Make sure to set your API key as an environment variable

    output_file = f"{os.path.splitext(input_file)[0]}.mp3"
    if convert_to_mp3(input_file, output_file):
        # Chunk audio
        audio_chunks = chunk_audio(output_file)
        
        # Transcribe chunks
        transcriptions = []
        for i, chunk in enumerate(audio_chunks):
            print(f"Transcribing chunk {i+1}...")
            transcription = transcribe_audio(client, chunk)
            if transcription:
                transcriptions.append(transcription)
            else:
                transcriptions.append(f"Transcription failed for chunk {i+1}\n\n")
            
            # Clean up audio chunk
            os.remove(chunk)
        
        # Clean up full audio file
        os.remove(output_file)
        
        # Combine transcriptions
        with open("combined_transcriptions.txt", "w") as outfile:
            outfile.write("\n".join(transcriptions))
        print("Processing complete. Results saved in 'combined_transcriptions.txt'")
    else:
        print("MP3 conversion failed. Process terminated.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <input_file>")
    else:
        main(sys.argv[1])

