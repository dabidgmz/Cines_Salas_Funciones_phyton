from Cines import Cines
from Salas import Salas
from SalasInterfaces import SalasInterfaces
from Arreglo import Arreglo
import json

class CinesInterfaces(Arreglo):
    def __init__(self, ciness = None):
        self.cines = ciness

        self.jsonflag = False
        if ciness is None:
            self.jsonflag = True
            self.cines = Cines()
            self.data = self.salas.read_json('Cines.json')
            self.salas.lista_object_hook_cine(self.data)

    def buscar_indice(self, num, lista):
        for i, cine in enumerate(lista):
            if cine.num == num:
                return i
        return -1

    def mostrar_menu(self):
        print("Menú de Cines ")
        print("1. Crear nuevo cine")
        print("2. Ver cines")
        print("3. Editar cine")
        print("4. Eliminar cine")
        print("5. Salir")

    def crear_cine(self):
        num = input("Numero del cine: ")
        nombre = input("Nombre del cine: ")
        ubi= input("Direccion del cine: ")
        capacidad= input("Capacidad del cine: ")
        numero_salas= input("Numero de Salas del cine: ")
        clasificacion= input("Clasificacion del cine: ")
        insSalas = Salas()

        menu_sal = SalasInterfaces(insSalas)
        menu_sal.ejecutar()
        cines = Cines( num,nombre,ubi,capacidad,numero_salas, clasificacion, insSalas)
        self.cines.create(cines)

        if self.jsonflag:
            self.salas.save_to_json("Cines.json")
        print("Cine creado y guardado correctamente.")
        return cines

    def ver_cines(self, busq=None):
        if not busq:
            print("Lista completa de cines:")
            for cine_instance in self.cines.lista:
                print("Cine:", cine_instance.get_output())
            return self.cines.lista
        else:
            busq = busq
            indice = self.buscar_indice(busq, self.cines.lista)
            if indice != -1:
                print("Cine:", self.salas.lista[indice].get_output())
            else:  
                print(f"No se encontró ninguna cine con el nombre {busq}.")
            return [self.cines.lista[indice]]

    def editar_cine(self, num):
        if num is None:
            print("No se encontró el cine")
            pass
        else:
            indice = self.buscar_indice(num, self.cines.lista)
            cine_editar = self.cines.lista[indice]
            campos = ['num,nombre','ubi','capacidad','numero_salas', 'clasificacion']
            for campo in campos:
                nuevo_valor = input(f"Ingresa nuevo {campo}: (Dejar en blanco para omitir)")
                if nuevo_valor != "":
                    if campo == 'capacidad':
                        setattr(cine_editar, campo, int(nuevo_valor))
                    else:
                        setattr(cine_editar, campo, nuevo_valor)
            cine_ed = cine_editar.funciones
            menu_sal = SalasInterfaces(cine_ed)
            menu_sal.ejecutar()
            cine_editar.salas = menu_sal.salas

            print(cine_editar.get_output())
            if self.jsonflag:
                self.salas.over_json('Cines.json')
            input("Cine editado correctamente, presiona cualquier tecla para continuar...")


    def eliminar_sala(self, nom):
        if nom is None:
            print("No se encontró el cine")
            pass
        else:
            indice = self.buscar_indice(nom, self.cines.lista)
            del self.cines.lista[indice]
            if self.jsonflag:
                self.cines.over_json('Cines.json')
            input("Cine eliminado correctamente, presiona cualquier tecla para continuar...")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear_cine()
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "2":
                num_busq = input("Mostrar cine por su nommero:(Dejar en blanco para mostrar todas.)")
                self.ver_cines(num_busq)
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "3":
                num_edit = input("Buscar cine por su nombre para editar:")
                self.editar_cine(num_edit)
                pass
            elif opcion == "4":
                num_del = input("Buscar cine por su nombre para eliminar:")
                self.eliminar_cine(num_del)
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    insCines = Cines()
    menu_cines = CinesInterfaces(insCines)
    menu_cines.ejecutar()
