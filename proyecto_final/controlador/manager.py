from flask_restful import Resource
class prueba(Resource):
    def get(self):
        try:
            return "prueba exitosa"
        except Exception as e:
            return str("Error interno")
        
class prueba2(Resource):
    def get(self):
        try:
            return "prueba exitosa2"
        except Exception as e:
            return str("Error interno")