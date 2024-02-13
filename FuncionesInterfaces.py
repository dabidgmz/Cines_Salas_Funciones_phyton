import json
from Funciones import Funciones
from MongoDB import Mongo

class FuncionesInterfaces():
    def __init__(self, funcs=None):
        self.funciones = funcs
        self.mongo = Mongo(db="Iot_db")
        self.jsonFlag = False
        if funcs is None:
            self.funciones = Funciones()
            self.jsonFlag = True
            self.data = self.funciones.read_json('Funciones.json')
            self.funciones.lista_object_hook_funcion(self.data)
            

    def buscar_indice(self, nombre, lista):
        for i, funcion in enumerate(lista):
            if funcion.nombre == nombre:
                return i
        return -1

    def mostrar_menu(self):
        print(" Menú de Funciones")
        print("1. Crear nueva función")
        print("2. Ver funciones")
        print("3. Editar función")
        print("4. Eliminar función")
        print("5. Salir")

    def crear_funcion(self):
        nf = input("Numero de la Funcion: ")
        hora_inicio = input("Hora de Incio de la Función: ")
        duracion = input("Duracion de la Función: ")
        tipo_proyeccion = input("Tipo de Proyeccion: ")
        precio_entrada = input("Precio de entrada de la función $: ")
        pelicula = input("Pelicula de la función : ")
        funciones = Funciones(nf, hora_inicio, duracion, tipo_proyeccion, precio_entrada, pelicula)
        self.funciones.create(funciones)
        print(self.funciones.get_output())
        nueva_funcion = {"numero_funcion": nf,"hora_inicio": hora_inicio,"duracion": duracion,"tipo_proyeccion": tipo_proyeccion,"precio_entrada": precio_entrada,"pelicula": pelicula
        }
        self.mongo.insert_one("Funciones", nueva_funcion)
        if self.jsonFlag:
            funciones.save_to_json("Funciones.json")
        print("Funcion creada y guardada correctamente.")
        return funciones
    
    def ver_funciones(self, busq=None):
        if not busq:
            print("Lista completa de funciones:")
            for func_instance in self.funciones.lista:
                print("Función:", func_instance.get_output())
            return self.funciones.lista
        else:
            indice = self.buscar_indice(busq, self.funciones.lista)
            if indice == -1:
                print("Ninguna Funcion encontrada.")
                pass
            print(self.funciones.lista[indice].get_output())
            return [self.funciones.lista[indice]]

    def editar_funcion(self, nf, salasflag = None):
        if nf is None:
            print("No se encontró la funcion")
            pass
        else:
            indice = self.buscar_indice(nf, self.funciones.lista)
            campos = ['nf', 'genero', 'hora_inicio', 'duracion', 'descripcion']
            for campo in campos:
                nuevo_valor = input(f"Ingresa nuevo {campo}: (Dejar en blanco para omitir)")
                if nuevo_valor != "":
                    if campo == 'año':
                        setattr(self.funciones.lista[indice], campo, int(nuevo_valor))
                    else:
                        setattr(self.funciones.lista[indice], campo, nuevo_valor)
            print(self.funciones.lista[indice].get_output())
            if self.jsonFlag and salasflag == None:
                self.funciones.over_json('Funciones.json')
            return self.funciones.lista[indice]

    def eliminar_funcion(self, nombre):
        if nombre is None:
            print("No se encontró la funcion")
            pass
        else:
            indice = self.buscar_indice(nombre, self.funciones.lista)
            if indice == -1:
                print("No se encontró la funcion o no existe")
                pass
            del self.funciones.lista[indice]
            if self.jsonFlag:
                self.funciones.over_json('Funciones.json')

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear_funcion()
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "2":
                busq = input("Mostrar función por su nuumro:(Dejar en blanco para mostrar todas.)")
                self.ver_funciones(busq)
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "3":
                edit = input("Buscar función por su numero para editar:")
                self.editar_funcion(edit)
                input("Función editada correctamente, presiona cualquier tecla para continuar...")
                pass
            elif opcion == "4":
                dele = input("Buscar función por su numero para eliminar:")
                self.eliminar_funcion(dele)
                input("Función eliminada correctamente, presiona cualquier tecla para continuar...")
                pass
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    insFunciones = Funciones()
    menu_funciones = FuncionesInterfaces(insFunciones)
    menu_funciones.ejecutar()
