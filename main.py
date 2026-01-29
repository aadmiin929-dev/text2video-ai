from ai import inspire_me, improve_script, split_into_scenes, generate_image
from moviepy.editor import *
from gtts import gTTS
import os

SCRIPT_PATH = "input/script.txt"
AUDIO_PATH = "audio/voice.mp3"
VIDEO_PATH = "video/result.mp4"

os.makedirs("audio", exist_ok=True)
os.makedirs("video", exist_ok=True)

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

print("1 - Вдохнови меня (ИИ)")
print("2 - Улучшить текст")
choice = input("Выбери (Enter — пропустить): ")

if choice == "1":
    text = inspire_me()
elif choice == "2":
    text = improve_script(text)

print("🎬 Сценарий:\n", text)

# Озвучка
tts = gTTS(text=text, lang="ru")
tts.save(AUDIO_PATH)

# Сцены
scenes = split_into_scenes(text)

clips = []
for i, scene in enumerate(scenes):
    print(f"🖼 Генерация сцены {i+1}")
    image_path = generate_image(scene, i)
    clip = ImageClip(image_path).set_duration(4)
    clips.append(clip)

video = concatenate_videoclips(clips)
audio = AudioFileClip(AUDIO_PATH)
video = video.set_audio(audio)

video.write_videofile(VIDEO_PATH, fps=24)

print("✅ Видео создано:", VIDEO_PATH)
