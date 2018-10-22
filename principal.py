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
		"1": self.IniciarSesion,
		#"2": self.Registrarme,
		"3": self.SalirPrincipal
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
	def display_MenuPasajero():
		print(MENSAJE.men.get("MenuPasajero"))
	 
	@staticmethod
	def AgregarConductor():
		archivo=open("registro.txt", "a")
		print(MENSAJE.men.get("Antes@"))
		X=True
		while X:
			Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
			X=PERSONA.VerificarRegistro("CONDUCTOR", Correo)
		Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
		Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
		Cell=(input(MENSAJE.men.get("IngresarCell"))).lower()
		CONDUCTOR(Correo, Contrasena, Nombre, Cell)
		archivo.write("\n"+"CONDUCTOR,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0,0")

	@staticmethod
	def AgregarPasajero():
		archivo=open("registro.txt", "a")
		print(MENSAJE.men.get("Antes@"))
		X=True
		while X:
			Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
			X=PERSONA.VerificarRegistro("PASAJERO", Correo)
		Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
		Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
		Cell=(input(MENSAJE.men.get("IngresarCell"))).lower()
		PASAJERO(Correo, Contrasena, Nombre, Cell)
		archivo.write("\n"+"PASAJERO,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0")

	@staticmethod
	def SalirPrincipal():
		print(MENSAJE.men.get("salir"))
		os._exit(0)

	@staticmethod
	def IniciarSesion():
		infousuario=True
		while infousuario==True:
			print(MENSAJE.men.get("MensajeInicioSesion"))
			correo=(input(MENSAJE.men.get("IngresarCorreo"))).lower()
			if correo=="3":
				infousuario="salir"
				break
			contrasena=input(MENSAJE.men.get("IngresarContrasena"))
			infousuario=PERSONA.VerificarCorreo(correo, contrasena)
			if infousuario=="salir":
				break 
		if infousuario!="salir":
			if "PASAJERO"==infousuario[0]:
				PRINCIPAL.InicioSesionPasajero()
			if "CONDUCTOR"==infousuario[0]:
				PRINCIPAL.InicioSesionConductor()
			if "ADMINISTRADOR"==infousuario[0]:
				PRINCIPAL.InicioSesionAdmin()
			print(MENSAJE.men.get("CerradoSesion"))

	@staticmethod
	def InicioSesionPasajero():

		while True:
			PRINCIPAL.display_MenuPasajero()
			opcion=input(MENSAJE.men.get("Opcion"))
			print("")
			if (int(opcion)!=1 and int(opcion)!=2):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if (int(opcion)==1):
				SERVICIO.VerServicios()
			elif (int(opcion)==2):
				break

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
			if opcion=="2":
				self.runRegistrarme()

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