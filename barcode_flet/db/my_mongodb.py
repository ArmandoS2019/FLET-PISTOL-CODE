from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["data_mongo_db"]
collection_doc_data = db["mongodb_data_ultitracking"]
collection_users = db["mongodb_users"]

# posts = db.posts #!name of the post
# new_post = {'title': 'Evento de detención preventiva en Ciudad Colonial', 'date': '30-07-2024 y 31-07-2024', 'case_time': '22:00 horas del 30-07-2024 y 10:00 horas del 31-07-2024', 'country_name': 'República Dominicana', 'estado': 'Detenidos mediante operativo preventivo Fase I y Fase II', 'nota_informativa': 'Sección Turística realizó operativos preventivos en diferentes sectores de Ciudad Colonial', 'numero_personas': '8', 'nombre_personas': ['VÍCTOR MATEO DÍAZ', 'DIOMEDES GERALDO', 'JIMY RAMÍREZ', 'ANGELIS GERMÁN', 'ASHLEY PÉREZ', 'ESTEPHANI MONTERO', 'FRANCISCO RAMÍREZ', 'HANSEEN CHARLES'], 'edad': 'mayores de edad', 'documentos_portados': 'no portan documentos', 'lugar_detencion': 'Destacamento Policial de San Carlos', 'fase': ['Fase I', 'Fase II'], 'tipo': 'Detención preventiva', 'agression_type': [], 'arrest_location': ['Ciudad Colonial'], 'reason_arrest': [], 'ubicacion': 'Ciudad Colonial, República Dominicana', 'resultado': 'Culminando a las 03:00 horas del día 31-07-2024 y sin novedad'}
# # post_id = posts.insert_one(new_post)
# result = collection.insert_one(new_post)


# for dat in collection.find():
#     print(dat)