from fastapi import FastAPI
import uvicorn

from Api.Config.settings import Settings
from Api.Controllers.gamesController import games

app = FastAPI()
app.include_router(games)

settings = Settings()

@app.get('/')
async def index():
    return {'message': f'Hello this is the {settings.app_name} System Api and Notifications Service.', 'db': settings.mongo_url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


