from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseSettings

import json

class Settings(BaseSettings):
    counter_message: int = 0

settings = Settings()
app = FastAPI(title='Web page send JSON') #create app

html = ""
with open('index.html', 'r', encoding='utf-8') as file:
    html = file.read()


@app.get("/")
async def root():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = settings.counter_message

    while True:
        data = await websocket.receive_text()
        # print(data)
        try:

            counter = counter + 1
            send_data = json.loads(data)
            send_data['id'] = counter
            # print(send_data, type(send_data))
            await websocket.send_json(send_data)

        except Exception as e:
            print('error:', e)
            break
