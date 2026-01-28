from moviepy.editor import *
from gtts import gTTS
import os

# Paths
SCRIPT_PATH = "input/script.txt"
AUDIO_PATH = "audio/voice.mp3"
VIDEO_PATH = "video/result.mp4"

os.makedirs("audio", exist_ok=True)
os.makedirs("video", exist_ok=True)

# Read text
with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Text to Speech
tts = gTTS(text=text, lang="ru")
tts.save(AUDIO_PATH)

# Create simple video scenes
clips = []
for i in range(3):
    clip = ColorClip(size=(1280, 720), color=(30, 30, 30), duration=4)
    clips.append(clip)

video = concatenate_videoclips(clips)
audio = AudioFileClip(AUDIO_PATH)
video = video.set_audio(audio)

video.write_videofile(VIDEO_PATH, fps=24)

print("✅ Video created:", VIDEO_PATH)
