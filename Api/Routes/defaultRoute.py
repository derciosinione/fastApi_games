from Api.Config.settings import Settings
from Api.Routes import defaultRoute


@defaultRoute.get('/')
async def index():
    settings = Settings()
    return {'message': f'Hello this is the {settings.app_name} System Api and Notifications Service.'}
