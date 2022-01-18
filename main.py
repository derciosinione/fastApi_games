from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug=True)


@app.get('/')
async def root():
    return {'message': 'Hello FastApi'}

