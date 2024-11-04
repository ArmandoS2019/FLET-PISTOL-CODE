from db.my_mongodb import collection
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router_data = APIRouter()

@router_data.get("/get_data/")
async def get_data():
    try:
        # Obtiene todos los documentos de la colección
        items = list(collection.find().limit(50))
        # Convierte ObjectId a string para que sea serializable en JSON
        for item in items:
            item["_id"] = str(item["_id"])
        return {'items':items}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
