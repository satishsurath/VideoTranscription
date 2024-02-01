import azure.cognitiveservices.speech as speechsdk
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
print("Environment variables loaded.")

# Set up the Azure Speech configuration with variables from .env file
speech_key = os.getenv("SPEECH_KEY")
service_region = os.getenv("SERVICE_REGION")

# Ensure keys are loaded properly
if not speech_key or not service_region:
    raise ValueError("Azure Speech service credentials not found in .env file")
print("Azure Speech service configuration set up with provided credentials.")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the audio file path
audio_file = "./audio/YOURMOVIE_FILE.wav"
print(f"Audio file set to {audio_file}.")

# Set up the audio configuration
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
print("Audio configuration set up.")

# Create a speech recognizer object
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
print("Speech recognizer object created.")

# Create an empty list to store the transcription results
transcriptions = []

# Define an event handler for continuous recognition
def continuous_recognition_handler(evt):
    print(f"Processing transcription: {evt.result.text}")
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        transcriptions.append(evt.result.text)

# Start continuous recognition
speech_recognizer.recognized.connect(continuous_recognition_handler)
print("Starting continuous recognition...")
speech_recognizer.start_continuous_recognition()

# Wait for the recognition to complete
timeout_seconds = 600  # Set a timeout value (in seconds) based on your audio file length
timeout_expiration = time.time() + timeout_seconds

while time.time() < timeout_expiration:
    time.sleep(1)  # Adjust the sleep duration as needed

# Stop continuous recognition
speech_recognizer.stop_continuous_recognition()
print("Continuous recognition stopped.")

# Combine transcriptions into a single string
transcription = ' '.join(transcriptions)

# Write the transcription to a file
output_file = "./transcription/transcription.txt"
with open(output_file, "w") as file:
    file.write(transcription)

print(f"Transcription saved to: {output_file}")
