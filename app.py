import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import os
from nigeria_banks.database.db import bankdb



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return bankdb()

# if __name__ == "__main__":
#     uvicorn.run("app:app", host="127.0.0.1", port=8080)


@app.get("/images")
def images():
    out = []
    for filename in os.listdir("static/images"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/images/" + filename
        })
    return out

def logo_url(host, name):
    return host + "/static/images/" + name + ".png"