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
        try:
            data = await websocket.receive_text()
            counter = counter + 1
            print(data)
            counter : settings.counter_message + 1
            test = json.loads(data)
            # print(test)
            await websocket.send_json(f" {counter} {test} {type(test)}")
        except Exception as e:
            print('error:', e)
            break
