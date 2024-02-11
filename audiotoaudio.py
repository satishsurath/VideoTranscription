from pydub import AudioSegment

# Path to the input M4A audio file
audio_file_m4a = "./audio/youraudio.m4a"

# Path to the output WAV file
output_file_wav = "./audio/YOURAUDIO_FILE.wav"

# Load the M4A audio file
audio = AudioSegment.from_file(audio_file_m4a, format="m4a")

# Set the desired output parameters
# Note: pydub manages audio data as milliseconds and dB, frame rate (fps) and bit depth (bitrate as 'sample_width' in bytes) can be adjusted.
# However, pydub does not directly allow setting the bitrate for output files as it focuses on sample width and frame rate.

# Convert the sample rate (fps)
audio = audio.set_frame_rate(16000)  # Set the desired sampling rate: 16000 Hz

# Convert to mono if it's not already
audio = audio.set_channels(1)

# Optionally, adjust the sample width (16 bits = 2 bytes)
audio = audio.set_sample_width(2)  # 16 bits

# Export the audio to a WAV file
audio.export(output_file_wav, format="wav", parameters=["-acodec", "pcm_s16le"])
