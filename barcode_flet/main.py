from contextlib import asynccontextmanager

import flet as ft
from login.login import Login
import flet.fastapi as flet_fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi import HTTPException
import os
from routers import router_image

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

def main(page: ft.Page):
    Login(page)
     
app.include_router(router_image, 
                   prefix="/images", 
                   tags=["Images"]) #This routes get FROM FAST API other API folder

app.include_router(router_image, 
                   prefix="/read_qr", 
                   tags=["Images"]) #This routes get FROM FAST API other API folder


app.mount("/",flet_fastapi.app(main, 
                            assets_dir='assets',
                            web_renderer=ft.WebRenderer.CANVAS_KIT))
