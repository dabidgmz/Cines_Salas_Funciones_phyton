import json
from Funciones import Funciones
from Arreglo import Arreglo

class Salas(Arreglo):
    def __init__(self, Numero_sala=None, capacidad=None, formato_pantalla=None, sonido=None, tipo=None, funciones=None):
        super().__init__()
        if Numero_sala is not None and capacidad is not None and formato_pantalla is not None and sonido is not None and tipo is not None:
            self.Numero_sala = Numero_sala
            self.capacidad = capacidad
            self.formato_pantalla = formato_pantalla
            self.sonido = sonido
            self.tipo = tipo
            if isinstance(funciones, Funciones):
                self.funciones = funciones
            else:
                self.funciones = Funciones()

    def to_dict(self):
        return {
            'Num': self.Numero_sala,
            'Capacidad': self.capacidad,
            'Formato de la pantalla': self.formato_pantalla,
            'sonido': self.sonido,
            'tipo': self.tipo,
            'funciones': [func.get_output() for func in self.funciones]
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
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

    def json_object_hook(self, dct):
        func_instances = Funciones()
        funciones_data = dct.get('funciones', [])
        func_instances.lista_object_hook_funcion(funciones_data)
        
        return Salas(
            Numero_sala=dct.get('Numero de Sala'),
            capacidad=dct.get('Capacidad'),
            Asientos=dct.get('Asientos'),
            sonido=dct.get('sonido'),
            tipo=dct.get('tipo'),
            funciones=func_instances
        )

    def lista_object_hook_sala(self, data):
        for item in data:
            if isinstance(item, dict):
                func = self.json_object_hook(item)
                self.create(func)


if __name__ == '__main__':
    sala1 = Salas(1, 50, '3D', 'Dolby Atmos', 'VIP')
    sala2 = Salas(2, 40, '2D', 'DTS', 'VIPV')

    funcion1 = Funciones(1, "18:00", "2 horas", "Digital", 10.5, "Spider-Man: No Way Home")
    funcion2 = Funciones(2, "20:30", "2.5 horas", "IMAX", 15.0, "Gwen Stacy: Into the Spider-Verse")
    funcion3 = Funciones(3, "17:30", "1.5 horas", "IMAX", 11.0, "Capitan america")
    funcion4 = Funciones(4, "20:30", "1.5 horas", "IMAX", 15.0, "Hulk")
    funcion5 = Funciones(5, "13:30", "1.5 horas", "IMAX", 17.0, "Titanic")

    sala = Salas()
    sala.agregar(sala1)
    sala.agregar(sala2)
    sala1.funciones.agregar(funcion1)
    sala2.funciones.agregar(funcion2)
    sala2.funciones.agregar(funcion3)
    sala2.funciones.agregar(funcion4)
    sala2.funciones.agregar(funcion5)
    print("Dictionary representation of Salas:")
    print(sala.dictt())
    sala.upload_json_salas("salas.json")
    data = sala.load_json_salas("salas.json")
    sala.objetos_salas(data)
