from prompt import system_prompt__site
from prompt import system_prompt__api

from typing import Union
from fastapi.responses import HTMLResponse
from ollama import Client

from fastapi import FastAPI

app = FastAPI()

@app.get("/site/{path:path}", response_class=HTMLResponse)
def read_root(path: str):
    client = Client(host="http://localhost:11434")
    response = client.generate(
        model="qwen2.5-coder:0.5b",
        system=system_prompt__site,
        prompt=path,
        stream=False,
    )
    return response.response


@app.get("/api/{path:path}")
def read_root(path: str):
    client = Client(host="http://localhost:11434")
    response = client.generate(
        model="qwen2.5-coder:0.5b",
        system=system_prompt__api,
        prompt=path,
        stream=False,
        format="json",
    )
    return response.response
