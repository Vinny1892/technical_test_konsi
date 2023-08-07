from fastapi import FastAPI

from api_konsi.infrastructure.router import health_check_route, benefits_route

app = FastAPI()
app.include_router(health_check_route.router)
app.include_router(benefits_route.router)
