import os
from pydub import AudioSegment

# Define the input and output folder paths
input_folder = "./audios"
output_folder = "./chunkedAudios"
# ChunkedAudios

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Target chunk size in bytes (20 MB)
target_chunk_size = 20 * 1024 * 1024

# Bitrate of the MP3 files (in kbps)
bitrate_kbps = 64

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        input_file = os.path.join(input_folder, filename)
        
        print(f"Processing file: {input_file}")

        try:
            # Load the audio file
            audio = AudioSegment.from_mp3(input_file)
            
            # Calculate the chunk duration in milliseconds
            bytes_per_second = (bitrate_kbps * 1000) // 8
            chunk_duration_ms = (target_chunk_size // bytes_per_second) * 1000

            # Split the audio into chunks
            for i, chunk_start in enumerate(range(0, len(audio), chunk_duration_ms)):
                chunk = audio[chunk_start:chunk_start + chunk_duration_ms]
                chunk_output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_part{i + 1}.mp3")
                chunk.export(chunk_output_file, format="mp3", bitrate=f"{bitrate_kbps}k")

                print(f"Created chunk: {chunk_output_file}")

        except Exception as e:
            print(f"Failed to chunk {input_file}: {e}")

print("Chunking completed.")
