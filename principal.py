import os
from calificacion import CALIFICACION
from comentario import COMENTARIO
from conductor import CONDUCTOR
from pasajero import PASAJERO
from persona import PERSONA
from vehiculo import VEHICULO
from servicio import SERVICIO
from mensaje import MENSAJE

class PRINCIPAL:

    def __init__(self):

        self.choices1={
        "1": self.AgregarPersona,
        "2": self.AgregarDatosFicticios,
        "3": self.Salir
            }

        self.choices2={
        "1": self.AgregarPersona,
        "2": self.AgregarConductor,
        "3": self.AgregarPasajero,
        "4": self.CrearComentario,
        "5": self.AgregarDatosFicticios,
        "6": self.Salir
            }

        self.choices3={
        "1": self.AgregarPersona,
        "2": self.AgregarConductor,
        "3": self.AgregarPasajero,
        "4": self.CrearComentario,
        "5": self.Calificar,
        "6": self.CrearServicio,
        "7": self.AgregarVehiculo,
        "8": self.Salir
            }

    @staticmethod
    def display_Menu1():
        print(MENSAJE.men.get("Menu1"))

    @staticmethod
    def display_Menu2():
        print(MENSAJE.men.get("Menu2"))

    @staticmethod
    def display_Menu3():
        print(MENSAJE.men.get("Menu3"))

    @staticmethod
    def idiomaMensajes():
        print(MENSAJE.mensaje.get("textoIdioma"))
        idioma = input(MENSAJE.mensaje.get("SeleccioneIdioma"))
        if idioma =="1":
            MENSAJE.men = MENSAJE.español
        else:
            MENSAJE.men = MENSAJE.ingles

    def run1(self):

        PRINCIPAL.idiomaMensajes()

        while true:
            self.display_Menu1()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choices1.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion==1:
                self.run2()
                os._exit(0)
            else:
                self.run3()
                os._exit(0)
                    
    def run2(self):

        while true:
            self.display_Menu2()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choices2.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion==5:
                self.runt3()
                os._exit(0)

    def run3(self):
        while true:
            self.display_Menu3()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choices3.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
                
if __name__=="__main__":
    PRINCIPAL().run()