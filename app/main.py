from fastapi import FastAPI

from app.routes.chat_routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"message": "¡Visita la ruta de chat!"}