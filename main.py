from fastapi import FastAPI
from stream_handler import handle_input
import uvicorn

app = FastAPI()

@app.post("/stream")
async def receive_stream(data: dict):
    return await handle_input(data)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
