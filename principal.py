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
        "1": self.AgregarConductor,
        "2": self.AgregarPasajero,
        "3": self.AgregarDatosFicticios,
        "4": self.Salir
            }

        self.choices2={
        "1": self.AgregarConductor,
        "2": self.AgregarPasajero,
        "3": self.CrearComentario,
        "4": self.AgregarDatosFicticios,
        "5": self.Salir
            }

        self.choices3={
        "1": self.AgregarConductor,
        "2": self.AgregarPasajero,
        "3": self.CrearComentario,
        "4": self.Calificar,
        "5": self.CrearServicio,
        "6": self.AgregarVehiculo,
        "7": self.Salir
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
        print(MENSAJE.Mensaje.get("textoIdioma"))
        idioma = input(MENSAJE.Mensaje.get("SeleccioneIdioma"))
        if idioma =="1":
            MENSAJE.men = MENSAJE.español
        else:
            MENSAJE.men = MENSAJE.ingles
            
    @staticmethod
    def AgregarConductor():
        print(MENSAJE.men.get("Antes@"))
        Correo=input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co"
        Contraseña=input(MENSAJE.men.get("IngresarContraseña"))
        Nombre=input(MENSAJE.men.get("IngresarNombre"))
        Cell=input(MENSAJE.men.get("IngresarCell"))
        CONDUCTOR(Correo, Contraseña, Nombre, Cell)

    @staticmethod
    def AgregarPasajero():
        print(MENSAJE.men.get("Antes@"))
        Correo=input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co"
        Contraseña=input(MENSAJE.men.get("IngresarContraseña"))
        Nombre=input(MENSAJE.men.get("IngresarNombre"))
        Cell=input(MENSAJE.men.get("IngresarCell"))
        PASAJERO(Correo, Contraseña, Nombre, Cell)

    @staticmethod
    def Salir():
        print(MENSAJE.men.get("salir"))
        os._exit(0)

    #@staticmethod
    #def 

    def run1(self):

        PRINCIPAL.idiomaMensajes()

        while True:
            self.display_Menu1()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choices1.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion==1 or opcion==2:
                self.run2()
                os._exit(0)
            else:
                self.run3()
                os._exit(0)

    def run2(self):

        while True:
            self.display_Menu2()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choices2.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion==4:
                self.runt3()
                os._exit(0)

    def run3(self):

        while True:
            self.display_Menu3()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choices3.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))

if __name__=="__main__":
    PRINCIPAL().run1()