from typing import Optional
from api import appointment_api

import fastapi
import uvicorn

api = fastapi.FastAPI()


def configure_routing():
    api.include_router(appointment_api.router)


def configure():
    configure_routing()
    
if __name__ == '__main__':
    configure()
    uvicorn.run(api)





'''
@api.get('/api/calculate')
def calculate(x : int, y:int, z:Optional[int]=None):
    if z==0:
        return fastapi.responses.JSONResponse(content={"error":"value of z cannot be Zero"}, status_code=400)
    if z is None:
        value=x+y
    else:
        value=(x+y)/z


    return {
        "x": x,
        "y":y,
        "z":z,
        "value": value
    }


'''
