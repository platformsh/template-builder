import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Simple HTMLResponse for root.
@app.api_route("/", response_class=HTMLResponse, status_code=200, methods=['GET', 'HEAD'])
async def load_root():
    with open("index.html", "r") as file:
        return file.read()

if __name__ == "__main__":
    port = os.getenv("PORT") or 8080
    uvicorn.run(app, host="127.0.0.1", port=int(port))
