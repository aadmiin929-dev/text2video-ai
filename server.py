from fastapi.responses import FileResponse
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import subprocess
import uuid
import os

app = FastAPI()

app.mount("/video", StaticFiles(directory="video"), name="video")

class VideoRequest(BaseModel):
    text: str

@app.post("/generate")
def generate_video(req: VideoRequest):
    video_id = str(uuid.uuid4())

    os.makedirs("input", exist_ok=True)
    with open("input/script.txt", "w", encoding="utf-8") as f:
        f.write(req.text)

    subprocess.run(["python", "main.py"], check=True)

    return {
        "video_url": f"/video/result.mp4",
        "video_id": video_id
    }

@app.get("/")
def index():
    return FileResponse("web/index.html")











