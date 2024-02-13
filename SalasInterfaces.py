import json
from Salas import Salas
from Funciones import Funciones
from FuncionesInterfaces import FuncionesInterfaces

class SalasInterfaces():

    def __init__(self, salass = None):
        self.salas = salass

        self.jsonflag = False
        if salass is None:
            self.jsonflag = True
            self.salas = Salas()
            self.data = self.salas.read_json('Salas.json')
            self.salas.lista_object_hook_sala(self.data)

    def buscar_indice(self, num, lista):
        for i, sala in enumerate(lista):
            if sala.Numero_sala == num:
                return i
        return -1

    def mostrar_menu(self):
        print("Menú de Salas ")
        print("1. Crear nueva sala")
        print("2. Ver salas")
        print("3. Editar salas")
        print("4. Eliminar sala")
        print("5. Salir")

    def crear_sala(self):
        Numero_sala = int(input("Numero de la sala: "))
        capacidad= input("Capacidad: ")
        formato_pantalla =input("Formato de la pantalla: ")
        sonido= input("sonido: ")
        tipo= input("tipo: ")
        insFunciones = Funciones()

        menu_func = FuncionesInterfaces(insFunciones)
        menu_func.ejecutar()
        salas = Salas(Numero_sala,capacidad,formato_pantalla,sonido,tipo,insFunciones)
        self.salas.create(salas)

        if self.jsonflag:
            self.salas.save_to_json("Salas.json")
        print("Sala creada y guardada correctamente.")
        return salas
    def ver_salas(self, busq=None):
        if not busq:
            print("Lista completa de salas:")
            for sala_instance in self.salas.lista:
                print("Sala:", sala_instance.get_output())
            return self.salas.lista
        else:
            busq = int(busq)
            indice = self.buscar_indice(busq, self.salas.lista)
            if indice != -1:
                print("Sala:", self.salas.lista[indice].get_output())
            else:  
                print(f"No se encontró ninguna sala con el número {busq}.")
            return [self.salas.lista[indice]]

    def editar_sala(self, num):
        if num is None:
            print("No se encontró la sala")
            pass
        else:
            indice = self.buscar_indice(num, self.salas.lista)
            sala_editar = self.salas.lista[indice]
            campos = ['Num', 'Encargado', 'Asientos', 'Vip']
            for campo in campos:
                nuevo_valor = input(f"Ingresa nuevo {campo}: (Dejar en blanco para omitir)")
                if nuevo_valor != "":
                    if campo == 'Num' or campo == 'Asientos':
                        setattr(sala_editar, campo, int(nuevo_valor))
                    elif campo == 'Vip':
                        setattr(sala_editar, campo, bool(nuevo_valor))
                    else:
                        setattr(sala_editar, campo, nuevo_valor)
            sala_ed = sala_editar.funciones
            menu_func = FuncionesInterfaces(sala_ed)
            menu_func.ejecutar()
            sala_editar.funciones = menu_func.funciones

            print(sala_editar.get_output())
            if self.jsonflag:
                self.salas.over_json('Salas.json')
            input("Sala editada correctamente, presiona cualquier tecla para continuar...")



    def eliminar_sala(self, num):
        if num is None:
            print("No se encontró la sala")
            pass
        else:
            if self.jsonflag:
                data = self.salas.read_json('Salas.json')
                self.salas.lista_object_hook_sala(data)
            indice = self.buscar_indice(num, self.salas.lista)
            del self.salas.lista[indice]
            if self.jsonflag:
                self.salas.over_json('Salas.json')
            input("Sala eliminada correctamente, presiona cualquier tecla para continuar...")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear_sala()
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "2":
                num_busq = input("Mostrar sala por su numero:(Dejar en blanco para mostrar todas.)")
                self.ver_salas(num_busq)
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "3":
                num_edit = int(input("Buscar sala por su numero para editar:"))
                self.editar_sala(num_edit)
                pass
            elif opcion == "4":
                num_del = int(input("Buscar sala por su numero para eliminar:"))
                self.eliminar_sala(num_del)
                input("Presiona cualquier tecla para continuar...")
                pass
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    insSalas = Salas()
    menu_salas = SalasInterfaces(insSalas)
    menu_salas.ejecutar()
