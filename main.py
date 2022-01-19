from fastapi import FastAPI
import uvicorn

from Api.Controllers.gamesRoutes import gamesRoutes
from Api.Controllers.defaultRoute import defaultRoute

app = FastAPI()
app.include_router(gamesRoutes)
app.include_router(defaultRoute)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


