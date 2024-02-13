import json
from Arreglo import Arreglo
import os
class Funciones(Arreglo):    
    def __init__(self, nf=None, hora_inicio=None, duracion=None, tipo_proyeccion=None, precio_entrada=None,pelicula=None):
        super().__init__()
        if nf is not None and hora_inicio is not None and duracion is not None and tipo_proyeccion is not None  and pelicula is not None:
            self.nf = nf
            self.hora_inicio = hora_inicio
            self.tipo_proyeccion = tipo_proyeccion
            self.precio_entrada = precio_entrada
            self.pelicula = pelicula
        self.data = []

    def to_dict(self):
        return {
            'numero': self.nf,
            'hora_inicio': self.hora_inicio,
            'tipo de proyeccion': self.tipo_proyeccion,
            'precion de entrada': self.precio_entrada,
            'Pelicula': self.pelicula
        }

    def to_list_of_dicts(self):
        return [item.to_dict() for item in self.lista] if isinstance(self.lista, list) else []

    def get_output(self):
        list_of_dicts = self.to_list_of_dicts()
        return list_of_dicts if list_of_dicts else self.to_dict()

    def read_json(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
            return existing_data
        except FileNotFoundError:
            return []

    def save_to_json(self, filename):
        existing_data = self.read_json(filename)
        new_data = self.get_output()
        existing_data.append(new_data)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

    def json_object_hook(self, dct):
        return Funciones(
            nombre=dct.get('numero'),
            genero=dct.get('hora_inicio'),
            director=dct.get('tipo de proyeccion'),
            año=dct.get('precion de entrad'),
            descripcion=dct.get('Pelicula')
        )

    def lista_object_hook_funcion(self, data):
        for item in data:
            if isinstance(item, dict):
                func = self.json_object_hook(item)
                self.create(func)



if __name__ == '__main__':
    funcion = Funciones()
    hola = funcion.readjson("funciones.json")
    print(hola)
    funcion.objetos(hola)
    funcion1 = Funciones(1, "18:00", "2 horas", "Digital", 10.5, "Spider-Man: No Way Home")
    funcion2 = Funciones(2, "22:30", "2.5 horas", "IMAX", 15.0, "Gwen Stacy: Into the Spider-Verse")
    funcion3 = Funciones(3, "17:30", "1.5 horas", "IMAX", 11.0, "Capitan america")
    funcion4 = Funciones(4, "20:30", "1.5 horas", "IMAX", 15.0, "Hulk")
    funcion5 = Funciones(5, "13:30", "1.5 horas", "IMAX", 17.0, "Titanic")
    arreglo_dict = funcion.to_dict()
    funcion.dictt()
    funcion.agregar(funcion1)
    funcion.agregar(funcion2)
    funcion.agregar(funcion3)
    funcion.agregar(funcion4)
    funcion.agregar(funcion5)
    funcion.writejson(funcion.dictt(), "funciones.json")
