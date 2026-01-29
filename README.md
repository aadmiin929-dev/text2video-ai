# 🎬 Text2Video AI (Simple)

⚠️ Проект запускается на ПК или сервере.
Android-приложение подключается к нему через API.

Простой open-source проект:
**превращает текст в видео с озвучкой**.

## 🚀 Как запустить (очень просто)

### 1. Установи Python
https://www.python.org/downloads/  
(поставь галочку **Add Python to PATH**)

### 2. Скачай проект
На GitHub нажми:
`Code → Download ZIP`

### 3. Установи зависимости
```bash
pip install -r requirements.txt


## 🖥 Запуск сервера (для Android / Web)

```bash
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000

http://localhost:8000/generate

{
  "text": "Текст для видео"
}
http://localhost:8000/video/result.mp4












