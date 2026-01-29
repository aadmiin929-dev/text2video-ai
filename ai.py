import os
from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def inspire_me():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": "Придумай короткий сценарий для видео из 3 сцен."
        }]
    )
    return response.choices[0].message.content.strip()

def improve_script(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"Улучши текст для видео:\n{text}"
        }]
    )
    return response.choices[0].message.content.strip()

def split_into_scenes(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"Разбей текст на 3 сцены, каждая сцена — одно предложение:\n{text}"
        }]
    )
    return response.choices[0].message.content.split("\n")

def generate_image(prompt: str, index: int):
    img = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1280x720"
    )

    url = img.data[0].url
    img_data = requests.get(url).content

    os.makedirs("images", exist_ok=True)
    path = f"images/scene_{index}.png"

    with open(path, "wb") as f:
        f.write(img_data)

    return path
