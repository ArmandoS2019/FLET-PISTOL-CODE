from contextlib import asynccontextmanager
from config.config import BASE_URL  # Import BASE_URL from config.py

import flet as ft
from login.login import Login
import flet.fastapi as flet_fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi import HTTPException
import os
import requests 
from api import router_image, router_data, router_user

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

def main(page: ft.Page):
    Login(page)
     
# API_URL = f"http://10.0.0.54:5000/login/" 
API_URL = "http://10.0.0.54:5000/login/"


def main_user(page: ft.Page):
    Login(page)
    # home_page = Login2()
    # about_page = HomePage()

    # # Función para manejar los cambios de ruta
    # def on_route_change(e):
    #     page.controls.clear()
    #     if page.route == "/":
    #         home_page.build(page)  # Llama al método `build` de la clase `HomePage`
    #     elif page.route == "/about":
    #         about_page.build(page)  # Llama al método `build` de la clase `AboutPage`
    #     else:
    #         page.add(ft.Text("404: Página no encontrada"))
    #     page.update()

    # # Configuración para el cambio de rutas
    # page.on_route_change = on_route_change

    # # Ruta inicial
    # page.go("/")
  
    
app.include_router(router_image, 
                   prefix="/images", 
                   tags=["Images"]) #This routes get FROM FAST API other API folder

app.include_router(router_image, 
                   prefix="/read_qr", 
                   tags=["Images"]) #This routes get FROM FAST API other API folder


app.include_router(router_data,
                   tags=["Data"]) #This routes get FROM FAST API other API folder

app.include_router(router_user,
                   tags=["Login"]) #This routes FOR register and work user login

# app.mount("/",flet_fastapi.app(main_user, 
#                             assets_dir='/assets',
#                             web_renderer=ft.WebRenderer.CANVAS_KIT))


app.mount("/",flet_fastapi.app(main, 
                            assets_dir='/assets', 
                            upload_dir="assets/uploads", 
                            secret_key="mi_clave_secreta",
                            web_renderer=ft.WebRenderer.CANVAS_KIT))
