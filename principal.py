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
        "3": self.SalirPrincipal
        }

        self.choicesIniciarSesion={
        #"1": self.Conductor,
        #"2": self.Pasajero,
        #"3": self.Administrador,
        #"4": self.atras
        }

        self.choicesRegistrarme={
        "1": self.AgregarConductor,
        "2": self.AgregarPasajero,
        #"3": self.atras
        }

    @staticmethod
    def display_MenuInicial():
        print(MENSAJE.men.get("MenuInicial"))

    @staticmethod
    def display_MenuIniciarSesion():
        print(MENSAJE.men.get("MenuIniciarSesion"))

    @staticmethod
    def display_MenuResgistrarme():
        print(MENSAJE.men.get("MenuRegistrarme"))
     
    @staticmethod
    def AgregarConductor():
        archivo=open("registro.txt", "a")
        print(MENSAJE.men.get("Antes@"))
        X=True
        while X:
            Correo=input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co"
            X=PRINCIPAL.VerificarCorreo("CONDUCTOR", Correo)
        Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
        Nombre=input(MENSAJE.men.get("IngresarNombre"))
        Cell=input(MENSAJE.men.get("IngresarCell"))
        CONDUCTOR(Correo, Contrasena, Nombre, Cell)
        archivo.write("CONDUCTOR, "+Correo+", "+Contrasena+", "+Nombre+", "+Cell+", 0, 0"+"\n")

    @staticmethod
    def VerificarCorreo(palabra, correo):
        archivo=open("registro.txt", "r")
        X=True
        while X:
            pal=0
            noesta=0
            for line in archivo:
                if palabra in line:
                    pal=pal+1
                    if correo in line:
                        print(MENSAJE.men.get("CorreoInvalido"))
                        X=False
                    else:
                        noesta=noesta+1
            if noesta==pal:
                return False
                X=False
            else:
                return True

    @staticmethod
    def AgregarPasajero():
        archivo=open("registro.txt", "a")
        print(MENSAJE.men.get("Antes@"))
        X=True
        while X:
            Correo=input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co"
            X=PRINCIPAL.VerificarCorreo("PASAJERO", Correo)
        Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
        Nombre=input(MENSAJE.men.get("IngresarNombre"))
        Cell=input(MENSAJE.men.get("IngresarCell"))
        PASAJERO(Correo, Contrasena, Nombre, Cell)
        archivo.write("PASAJERO, "+Correo+", "+Contrasena+", "+Nombre+", "+Cell+", 0"+"\n")

    @staticmethod
    def SalirPrincipal():
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
            elif (int(opcion)!=1 and int(opcion)!=3 and int(opcion)!=2):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion=="1":
                self.runIniciarSesion()
            elif opcion=="2":
                self.runRegistrarme()

    def runIniciarSesion(self):

        while True:
            self.display_MenuIniciarSesion()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choicesIniciarSesion.get(opcion)
            if action:
                action()
            elif(int(opcion)!=1 and int(opcion)!=3 and int(opcion)!=2 and int(opcion)!=4):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if(opcion=="4"):
                break

    def runRegistrarme(self):

        while True:
            self.display_MenuResgistrarme()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choicesRegistrarme.get(opcion)
            if action:
                action()
                break
            elif(int(opcion)!=1 and int(opcion)!=3 and int(opcion)!=2):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if (opcion=="3"):
                break

if __name__=="__main__":
    PRINCIPAL().runInicial()