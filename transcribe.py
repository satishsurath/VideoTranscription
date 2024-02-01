import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import time
from dotenv import load_dotenv
import os
import tempfile

# Load environment variables
load_dotenv()
print("Environment variables loaded.")

# Set up the Azure Speech configuration
speech_key = os.getenv("SPEECH_KEY")
service_region = os.getenv("SERVICE_REGION")
if not speech_key or not service_region:
    raise ValueError("Azure Speech service credentials not found in .env file")
print("Azure Speech service configuration set up with provided credentials.")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Path to the original audio file
audio_file_path = "./audio/YOURMOVIE_FILE.wav"
print(f"Processing audio file: {audio_file_path}")

# Load and chunk the audio file into 10-minute segments
audio = AudioSegment.from_wav(audio_file_path)
chunk_length_ms = 600000  # 10 minutes in milliseconds
chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

transcriptions = []

for i, chunk in enumerate(chunks):
    # Use a temporary file to avoid saving many large files
    with tempfile.NamedTemporaryFile(delete=True, suffix='.wav') as temp_file:
        chunk.export(temp_file.name, format="wav")
        print(f"Processing chunk {i+1}/{len(chunks)}")

        # Set up the audio configuration for this chunk
        audio_config = speechsdk.audio.AudioConfig(filename=temp_file.name)

        # Create a speech recognizer for the chunk
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # Synchronous single-shot recognition for simplicity
        result = speech_recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            transcriptions.append(result.text)
            print(f"Chunk {i+1} transcribed.")
        else:
            print(f"Chunk {i+1} could not be transcribed: {result.reason}")

# Combine transcriptions into a single string
transcription = ' '.join(transcriptions)

# Output file for the transcription
output_file = "./transcription/transcription.txt"
with open(output_file, "w") as file:
    file.write(transcription)

print(f"Transcription saved to: {output_file}")
