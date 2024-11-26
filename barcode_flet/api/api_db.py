from db.my_mongodb import collection_doc_data
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId

router_data = APIRouter()

# Helper para convertir ObjectId a string
def item_serializer(item):
    item["_id"] = str(item["_id"])
    return item

# Esquema de respuesta usando Pydantic
class ItemModel(BaseModel):
    id: str = Field(..., alias="_id")  # Mapea _id a id para la respuesta
    name: str
    description: str

    class Config:
        # Permitir alias en la respuesta
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

@router_data.get("/get_data/", response_model=List[ItemModel])
async def get_data():
    try:
        # Obtener documentos de la colección con un límite de 50
        items = collection_doc_data.find()
        
        # Convertir cada documento para que el ObjectId sea serializable
        serialized_items = [item_serializer(item) for item in items]

        return JSONResponse(content={"items": serialized_items})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al obtener los datos de la base de datos")

