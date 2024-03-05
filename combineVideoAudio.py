from moviepy.editor import VideoFileClip, AudioFileClip

def combine_video_audio(video_path, audio_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)
    
    # Load the audio file
    audio_clip = AudioFileClip(audio_path)
    
    # Set the audio of the video clip as the audio clip
    final_clip = video_clip.set_audio(audio_clip)
    
    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Replace 'path_to_video.mp4' and 'path_to_audio.mp4' with your actual file paths
video_path = './video/Video.mp4'
audio_path = './video/Audio.mp4'
output_path = './video/output_video.mp4'

combine_video_audio(video_path, audio_path, output_path)
