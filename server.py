from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Request(BaseModel):
    text: str

@app.post("/generate")
def generate_video(req: Request):
    with open("input/script.txt", "w", encoding="utf-8") as f:
        f.write(req.text)

    subprocess.run(["python", "main.py"])

    return {"video_url": "http://SERVER_IP/video/result.mp4"}
