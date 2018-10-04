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

        self.choicesInicial={
        #"1": self.IniciarSesion,
        #"2": self.Registrarme,
        "3": self.Salir
        }

        self.choicesIniciarSesion={
        #"1": self.Conductor,
        #"2": self.Pasajero,
        #"3": self.Administrador,
        "4": self.Salir
        }

        self.choicesRegistrarme={
        "1": self.AgregarConductor,
        "2": self.AgregarPasajero,
        "3": self.Salir
        }

    @staticmethod
    def display_MenuInicial():
        print(MENSAJE.men.get("MenuInicial"))

    @staticmethod
    def display_MenuIniciarSesion():
        print(MENSAJE.men.get("MenuIniciarSesion"))

    @staticmethod
    def display_Menu3():
        print(MENSAJE.men.get("Menu3"))
     
    @staticmethod
    def AgregarConductor():
        print(MENSAJE.men.get("Antes@"))
        Correo=input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co"
        Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
        Nombre=input(MENSAJE.men.get("IngresarNombre"))
        Cell=input(MENSAJE.men.get("IngresarCell"))
        CONDUCTOR(Correo, Contrasena, Nombre, Cell)

    @staticmethod
    def AgregarPasajero():
        print(MENSAJE.men.get("Antes@"))
        Correo=input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co"
        Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
        Nombre=input(MENSAJE.men.get("IngresarNombre"))
        Cell=input(MENSAJE.men.get("IngresarCell"))
        PASAJERO(Correo, Contrasena, Nombre, Cell)

    @staticmethod
    def Salir():
        print(MENSAJE.men.get("salir"))
        os._exit(0)

    @staticmethod
    def idiomaMensajes():
        while True:
            print(MENSAJE.Mensaje.get("textoIdioma"))
            idioma = input(MENSAJE.Mensaje.get("SeleccioneIdioma"))
            if idioma =="1":
                MENSAJE.men = MENSAJE.espanol
                break
            elif idioma=="2":
                MENSAJE.men = MENSAJE.ingles
                break
            else:
                print(MENSAJE.espanol.get("OpcionIncorrecta").format(idioma))
                print(MENSAJE.ingles.get("OpcionIncorrecta").format(idioma))


    def runInicial(self):

        PRINCIPAL.idiomaMensajes()

        while True:
            self.display_MenuInicial()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choicesInicial.get(opcion)
            if action:
                action()
            elif (opcion<1 and opcion>3):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion=="1" or opcion=="2":
                self.runIniciarSesion()
            else:
                self.runRegistrarme()

    def runIniciarSesion(self):

        while True:
            self.display_MenuIniciarSesion()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choicesIniciarSesion.get(opcion)
            if action:
                action()
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))

    def runRegistrarme(self):

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
    PRINCIPAL().runInicial()




