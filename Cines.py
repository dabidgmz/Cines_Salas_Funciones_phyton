
from Salas import Salas
from Funciones import Funciones
from Arreglo import Arreglo
import json

class Cines(Arreglo):
    def __init__(self, num=None, nombre=None, ubi=None, capacidad=None,numero_salas=None, clasificacion=None, salas=None):
        super().__init__()
        if num is not None and nombre is not None and ubi is not None and capacidad is not None and numero_salas is not None and clasificacion is not None and salas is not None:
            self.num = num
            self.nombre = nombre
            self.ubi = ubi
            self.capacidad = capacidad
            self.numero_salas = numero_salas
            self.clasificacion = clasificacion
            if isinstance(salas, Salas):
                self.salas = salas
            else:
                self.salas = Salas()

    def to_dict(self):
        return {
            'Numero': self.num,
            'Nombre': self.nombre,
            'Dir': self.ubi,
            'Capacidad': self.capacidad,
            'Numero de Salas': self.numero_salas,
            'Clasificacion': self.clasificacion,
            'Salas': [sala.get_output() for sala in self.salas]
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
        existing_data.extend(new_data)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

    def json_object_hook(self, dct):
        salas_instance = Salas()
        salas_data = dct.get('Salas', [])
        salas_instance.lista_object_hook_sala(salas_data)
        return Cines(
            Numero=dct.get('Numero'),
            Nombre=dct.get('Nombre'),
            dir=dct.get('Dir'),
            capacidad=dct.get('Capacidad'),
            numero_salas=dct.get('Numero de Salas'),
            clasificacion=dct.get('Clasificacion'),
            salas=salas_instance
        )

    def lista_object_hook_cine(self, data):
        for item in data:
            if isinstance(item, dict):
                func = self.json_object_hook(item)
                self.create(func)

if __name__ == '__main__':
    c = Cines()
    data = c.read_json('Cines.json')
    c.lista_object_hook_cine(data)
    for cines_instance in c.lista:
            print("Cine:", cines_instance.get_output())
            print("Tipo:", type(cines_instance))

