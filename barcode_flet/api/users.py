from db.my_mongodb import collection_users  # Tu archivo que importa la colección de MongoDB
from fastapi import APIRouter, HTTPException, status, Form
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from bson import ObjectId

router_user = APIRouter()

# Definición del Enum para el estado
class UserStatus(str, Enum):
    basic_user = "basic"
    admin_user = "admin"
    super_user = "super"
    
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    status: UserStatus = UserStatus.basic_user  # Valor predeterminado
    disabled: bool = False

class User(BaseModel):
    username: str
    password: str

@router_user.post("/login/")
async def login(user: User):
    if user.username == "a" and user.password == "1":
        return {"msg": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
      
