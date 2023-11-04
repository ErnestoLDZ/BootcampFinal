from proyecto_final import api
from proyecto_final.controlador import manager
 
api.add_resource(manager.prueba ,"/api/ucamp/prueba")
api.add_resource(manager.prueba2 ,"/api/ucamp/prueba2")