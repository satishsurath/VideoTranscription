import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Define the input and output folder paths
input_folder = "./input"
output_folder = "./output"


# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Set the desired audio parameters
audio_params = {
    "codec": "pcm_s16le",
    "fps": 16000,  # Set the desired sampling rate: 16000 Hz
    "nchannels": 1,  # Mono audio
    "bitrate": "16k"  # Set the desired bitrate
}

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".avi"):
        video_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".wav")
        
        print(f"Processing file: {video_file}")
        
        try:
            # Load the video clip
            video = VideoFileClip(video_file)
            
            # Extract the audio from the video
            audio = video.audio
            
            # Write the audio to a file
            audio.write_audiofile(output_file, codec=audio_params['codec'], fps=audio_params['fps'], bitrate=audio_params['bitrate'])
            
            print(f"Successfully converted {video_file} to {output_file}")
        except Exception as e:
            print(f"Failed to convert {video_file}: {e}")

print("Processing completed.")