from typing import Optional
import uvicorn
from fastapi import FastAPI
from db_querries import search_data
from bson.json_util import dumps
import json


app = FastAPI()


@app.get("/{param}")
async def read_items(param: str):
    data = search_data(param)
    if data:
        return {"code":200, "success" : True, "data" : json.loads(dumps(data))}
    else:
        return {"code":500, "success" : False, "message" : "unable to fetch data"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')