from typing import Optional
import uvicorn
from fastapi import FastAPI
from db_querries import search_data
from bson.json_util import dumps
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/search/{searchValue}")
async def read_items(searchValue: str):
    data = search_data(searchValue)
    if data:
        return {"code":200, "success" : True, "data" : json.loads(dumps(data))}
    else:
        return {"code":500, "success" : False, "message" : "unable to fetch data"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')