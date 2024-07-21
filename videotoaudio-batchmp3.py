import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Define the input and output folder paths
input_folder = "./input"
output_folder = "./output"


# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Desired audio parameters
bitrate = "64k"  # Lower bitrate to reduce file size

# Approximate size calculation (for reference, this is not exact)
def calculate_approximate_size(duration, bitrate):
    return (duration * (int(bitrate[:-1]) * 1000) / 8) / (1024 * 1024)  # in MB

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".avi"):
        video_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")

        print(f"Processing file: {video_file}")

        try:
            # Load the video clip
            video = VideoFileClip(video_file)
            # Extract the audio from the video
            audio = video.audio
            # Write the audio to a temporary WAV file
            temp_wav_file = "temp_audio.wav"
            audio.write_audiofile(temp_wav_file)

            # Convert the WAV file to MP3 with the desired bitrate
            audio_segment = AudioSegment.from_wav(temp_wav_file)
            duration_seconds = len(audio_segment) / 1000.0
            approx_size = calculate_approximate_size(duration_seconds, bitrate)
            print(f"Approximate file size with bitrate {bitrate}: {approx_size:.2f} MB")

            audio_segment.export(output_file, format="mp3", bitrate=bitrate)
            print(f"Successfully converted {video_file} to {output_file}")

            # Remove the temporary WAV file
            os.remove(temp_wav_file)
        except Exception as e:
            print(f"Failed to convert {video_file}: {e}")

print("Processing completed.")