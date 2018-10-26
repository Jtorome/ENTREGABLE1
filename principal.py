import os
from persona import PERSONA
from conductor import CONDUCTOR
from pasajero import PASAJERO
from vehiculo import VEHICULO
from servicio import SERVICIO
from comentario import COMENTARIO
from calificacion import CALIFICACION
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
	def display_MenuVerificarCorreo():
		print(MENSAJE.men.get("MenuVerificarCorreo"))
		print(MENSAJE.men.get("Opcion"))

	@staticmethod
	def display_MenuResgistrarme():
		print(MENSAJE.men.get("MenuRegistrarme"))
		
	@staticmethod
	def display_MenuPasajero():
		print(MENSAJE.men.get("MenuPasajero"))
		
	@staticmethod
	def display_MenuConductor():
		print(MENSAJE.men.get("MenuConductor"))

	@staticmethod
	def display_MenuAdmin():
		print(MENSAJE.men.get("MenuAdmin"))
	 
	@staticmethod
	def AgregarConductor():
		print(MENSAJE.men.get("Antes@"))
		X=True
		while X:
			Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
			X=PERSONA.VerificarRegistro("CONDUCTOR", Correo)
		Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
		Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
		Cell=(input(MENSAJE.men.get("IngresarCell"))).lower()
		conductor=CONDUCTOR(Correo, Contrasena, Nombre, Cell)
		PRINCIPAL.AgregarVehiculo(Correo, Contrasena, Nombre, Cell, conductor)

	@staticmethod
	def AgregarVehiculo(Correo, Contrasena, Nombre, Cell, conductor):
		archivo=open("registro.txt", "a")
		print(MENSAJE.men.get("InfoVehiculo"))
		Placa=input(MENSAJE.men.get("IngresarPlaca"))
		ColorVehiculo=input(MENSAJE.men.get("IngresarColor"))
		TipoVehiculo=input(MENSAJE.men.get("IngresarTipoVehiculo"))
		CantidadAsientos=input(MENSAJE.men.get("IngresarCantidadAsientos"))
		VEHICULO(Placa, ColorVehiculo, TipoVehiculo, CantidadAsientos, conductor)
		archivo.write("\n"+"CONDUCTOR,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0,0,"+Placa+","+ColorVehiculo+","+CantidadAsientos)

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
			elif infousuario=="Invalido":
				print(MENSAJE.men.get("ContraOCorreoInvalido"))

		if type(infousuario)==list:
			archivo=open("registro.txt", "r").readlines()
			line1=archivo[infousuario[0]].split(',')
			line2=archivo[infousuario[1]].split(',')
			PRINCIPAL.display_MenuVerificarCorreo()
			opcion=input()
			if opcion=="1":
				if "PASAJERO" ==line1[0]:
					infousuario = line1
				if "PASAJERO"==line2[0]:
					infousuario = line2
			if opcion=="2":
				if "CONDUCTOR"==line1[0]:
					infousuario = line1
				if "CONDUCTOR"==line2[0]:
					infousuario = line2
			if opcion=="3":
				infousuario = "salir"

		if infousuario!="salir" and infousuario!="Invalido":
			if "PASAJERO"==infousuario[0]:
				PRINCIPAL.InicioSesionPasajero(infousuario)
			if "CONDUCTOR"==infousuario[0]:
				PRINCIPAL.InicioSesionConductor(infousuario)
			if "ADMINISTRADOR"==infousuario[0]:
				PRINCIPAL.InicioSesionAdmin()
			print(MENSAJE.men.get("CerradoSesion"))
		

	@staticmethod
	def InicioSesionPasajero(infousuario):
	
		for pasajero in PASAJERO.listaPasajeros:
			if (pasajero.getCorreo()==infousuario[1] and pasajero.getContrasena()==infousuario[2] and pasajero.getNombre()==infousuario[3] and pasajero.getCell()==infousuario[4]):
				infousuario=pasajero
				break

		while True:
			PRINCIPAL.display_MenuPasajero()
			opcion=input(MENSAJE.men.get("Opcion"))
			print("")
			if (int(opcion)!=1 and int(opcion)!=2):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif (int(opcion)==1):
				SERVICIO.VerServicios()
			elif (int(opcion)==2):
				break

	@staticmethod
	def VerServicios():
		if len(SERVICIO.ServiciosDisponibles) ==0:
			print(MENSAJE.men.get("SinServicios"))
		else:
			cont=1
			for servicio in SERVICIO.ServiciosDisponibles:
				print(MENSAJE.men.get("FormatoVerServicios").format(cont+". "+servicio.getHoraEncuentro()+", "+servicio.getSitioEncuentro()+", "+servicio.getLugarInicio()+", "+servicio.getLugarFin()+", "+servicio.getAsientosDisponibles()+", "+servicio.getConductorSer().getNombre()))
				cont=cont+1
				
	@staticmethod
	def InicioSesionConductor(infousuario):
	
		for conductor in CONDUCTOR.ListaConductores:
			if (conductor.getCorreo()==infousuario[1] and conductor.getContrasena()==infousuario[2] and conductor.getNombre()==infousuario[3] and conductor.getCell()==infousuario[4]):
				infousuario=conductor
				break

		while True:
			PRINCIPAL.display_MenuConductor()
			opcion=input(MENSAJE.men.get("Opcion"))
			print("")
			if (int(opcion)!=1 and int(opcion)!=2 and int(opcion)!=3 and int(opcion)!=4):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif (int(opcion)==1):
				SERVICIO.ProgramarViaje()
			elif (int(opcion)==2):
				SERVICIO.VerViajeActual()
			elif (int(opcion)==3):
				SERVICIO.VerMiHistorial()
			elif (int(opcion)==4):
				break
				
	@staticmethod
	def InicioSesionAdmin():
		
		while True:
			PRINCIPA.display_MenuAdmin()
			opcion=input(MENSAJE.men.get("Opcion"))
			print("")
			if (int(opcion)!=1 and int(opcion)!=2 and int(opcion)!=3 and int(opcion)!=4):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif(int(opcion)==1):
				pass

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

		archivo=open("registro.txt", "r").readlines()
		for line in archivo:
			line=line.split(',')
			if "PASAJERO" == line[0]:
				PASAJERO(line[1], line[2], line[3], line[4])
			if "CONDUCTOR" == line[0]:
				conductor=CONDUCTOR(line[1], line[2], line[3], line[4])
				VEHICULO(line[7], line[8], line[9], line[10], conductor)

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