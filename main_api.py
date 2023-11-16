import os
from typing import Dict, List
from fastapi import FastAPI, Request
from presenters.api_presenter import ApiPresenter
from agents.ansari import Ansari
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "https://beta.ansari.chat",
    "http://beta.ansari.chat",
    "https://ansari.chat",
    "http://ansari.chat",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


ansari = Ansari()

port = int(os.getenv('API_SERVER_PORT',8000))


presenter = ApiPresenter(app, ansari)
presenter.present()

@app.post("/api/v1/complete")
async def complete(request: Request):
    body = await request.json()
    print(f'Request received > {body}.')
    #messages = [
    #    {"role:": "user", "text": "Hello, Ansari!"},
    #]
    return presenter.complete(body)
   