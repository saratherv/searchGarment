from typing import Optional
import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_items():
    return {"message": "Hello World from garment"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')