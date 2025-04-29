from typing import Union
from fastapi.responses import HTMLResponse
from ollama import Client

from fastapi import FastAPI

app = FastAPI()


@app.get("/{path:path}", response_class=HTMLResponse)
def read_root(path: str):
    client = Client(host="http://localhost:11434")
    response = client.generate(
        model="llama3.2",
        system="You are a mock web server that only returns a single html file. Your prompt will contain just an api path that the user is trying to access. Your task is to simulate the web server and return a single HTML file. This HTML fill may contain HTML, CSS and JS but you can only generate one valid HTML file in response to any prompt. Do no provide any explanation. Do not provide any text that is not the HTML file itsef. Make the HTML file relavant to the path provided in the prompt. Example: *PROMPT*: '/hello' *RESPONSE: <h1>Hello</h1>*",
        prompt=path,
        stream=False,
    )
    return response.response
