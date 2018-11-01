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
		1: self.IniciarSesion,
		#"2": self.Registrarme,
		3: self.SalirPrincipal
		}

		self.choicesRegistrarme={
		1: self.AgregarConductor,
		2: self.AgregarPasajero,
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
		archivo=open("registro.txt", "a")
		print(MENSAJE.men.get("Antes@"))
		X=True
		cont=0
		while X:
			if cont>0:
				print(MENSAJE.men.get("CorreoInvalido"))
			Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
			X=PERSONA.VerificarRegistro("CONDUCTOR", Correo)
			cont=cont+1
		Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
		Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
		Cell=(input(MENSAJE.men.get("IngresarCell"))).lower()
		conductor=CONDUCTOR(Correo, Contrasena, Nombre, Cell)
		archivo.write("\n"+"CONDUCTOR,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0,0")
		PRINCIPAL.AgregarVehiculo(conducotor)

	@staticmethod
	def AgregarVehiculo(conductor):
		archivo=open("registro.txt", "a")
		print(MENSAJE.men.get("InfoVehiculo"))
		X=True
		cont=0
		while X:
			if cont>0:
				print(MENSAJE.men.get("PlacaInvalida"))
			Placa=input(MENSAJE.men.get("IngresarPlaca"))
			if Placa == "3":
				return
			X=VEHICULO.VerificarPlaca(Placa)
			cont=cont+1
		ColorVehiculo=input(MENSAJE.men.get("IngresarColor"))
		TipoVehiculo=input(MENSAJE.men.get("IngresarTipoVehiculo"))
		CantidadAsientos=input(MENSAJE.men.get("IngresarCantidadAsientos"))
		if len(conductor.getVehiculos()) == 0:
			Activo="si"
		else:
			X=True
			while X:
				Activo=(input(MENSAJE.men.get("ActivarVehiculo"))).lower()
				if Activo=="si":
					X=CONDUCTOR.VerificarActivacion(conductor)
				else:
					break
		VEHICULO(Placa, ColorVehiculo, TipoVehiculo, CantidadAsientos, conductor, Activo)
		archivo.write("\n"+"VEHICULO,"+Placa+","+ColorVehiculo+","+TipoVehiculo+","+CantidadAsientos+","+conductor.getCorreo()+","+Activo)

	@staticmethod
	def AgregarPasajero():
		archivo=open("registro.txt", "a")
		print(MENSAJE.men.get("Antes@"))
		X=True
		cont=0
		while X:
			if cont>0:
				print(MENSAJE.men.get("CorreoInvalido"))
			Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
			X=PERSONA.VerificarRegistro("PASAJERO", Correo)
			cont=cont+1
		Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
		Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
		Cell=(input(MENSAJE.men.get("IngresarCell"))).lower()
		PASAJERO(Correo, Contrasena, Nombre, Cell)
		archivo.write("\n"+"PASAJERO,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0")

	@staticmethod
	def ProgramarViaje(infousuario):
		for servicio in SERVICIO.ServiciosDisponibles:
			if servicio.getConductorSer() == infousuario:
				print(MENSAJE.men.get("ServicioEnCurso"))
				return
		print(MENSAJE.men.get("InfoServicio"))
		HoraEncuentro=input(MENSAJE.men.get("IngresarHoraEncuentro"))
		if HoraEncuentro == "3":
			return
		SitioEncuentro=input(MENSAJE.men.get("IngresarSitioEncuentro"))
		LugarInicio=input(MENSAJE.men.get("IngresarLugarInicio"))
		LugarFin=input(MENSAJE.men.get("IngresarLugarFin"))
		AsientosDisponibles=input(MENSAJE.men.get("IngresarAsientosDisponibles"))
		FechaSer=time.strftime("%y/%m/%d")
		SERVICIO(HoraEncuentro, SitioEncuentro, LugarInicio, LugarFin, AsientosDisponibles, infousuario)
		archivo=open("registro.txt", "a")
		archivo.write("\n"+"SERVICIO,"+HoraEncuentro+","+SitioEncuentro+","+LugarInicio+","+LugarFin+","+AsientosDisponibles+","+infousuario.getCorreo()+","+FechaSer+",0")

	@staticmethod
	def SalirPrincipal():
		print(MENSAJE.men.get("salir"))
		os._exit(0)

	@staticmethod
	def VerServicios():
		if len(SERVICIO.ServiciosDisponibles) == 0:
			return print(MENSAJE.men.get("SinServicios"))
		else:
			cont=1
			for servicio in SERVICIO.ServiciosDisponibles:
				print(MENSAJE.men.get("FormatoVerServicios").format(cont, servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre()))
				cont=cont+1

		while True:
			opcion=int(input(MENSAJE.men.get("IngreseServicioEscogido")))
			if opcion==0:
				break
			elif opcion<0 and opcion>=len(SERVICIO.ServiciosDisponibles):
				print(MENSAJE.men.get("OpcionIncorrecta"))
			else:
				servicio=SERVICIO.ServiciosDisponibles[opcion-1]

	@staticmethod
	def VerViajeActual(infousuario):
		servicio=infousuario.getServicioActual()[0]
		print(MENSAJE.men.get("FormatoViajeActual").format(servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles()))
		print(MENSAJE.men.get("MenuFormatoViajeActual"))
		opcion=int(input(MENSAJE.men.get("Opcion")))
		if opcion != 1 and opcion !=2:
			print(MENSAJE.men.get("Opcion"))
		elif opcion == 2:
			return
		elif opcion == 1:
			print(MENSAJE.men.get("CambiarInfo"))
			archivo=open("registro.txt", "r").readlines()
			contenido=list()
			for line in archivo:
				if "SERVICIO"==line.split(',')[0] and servicio.getHoraEncuentro()==line.split(',')[1] and servicio.getFechaSer()==line.split(',')[7] and servicio.getConductorSer().getCorreo()==line.split(',')[6]:
					while True:
						cambio=int(input(MENSAJE.men.get("Opcion")))
						if cambio!=1 and cambio!=2 and cambio!=3 and cambio!=4 and cambio!=5 and cambio!=6:
							print(MENSAJE.men.get("OpcionIncorrecta"))
						elif cambio==1:
							HoraVieja=servicio.getHoraEncuentro()
							HoraNueva=input(MENSAJE.men.get("IngresarHoraEncuentro"))
							line=line.replace(HoraVieja, HoraNueva).split(',')
							servicio.setHoraEncuentro(HoraNueva)
							contenido.append(','.join(line))
							break
						elif cambio==2:
							SitioViejo=servicio.getSitioEncuentro()
							SitioNuevo=input(MENSAJE.men.get("IngresarSitioEncuentro"))
							line=line.replace(SitioViejo, SitioNuevo).split(',')
							servicio.setSitioEncuentro(SitioNuevo)
							contenido.append(','.join(line))
							break
						elif cambio==3:
							LugarViejo=servicio.getLugarInicio()
							LugarNuevo=input(MENSAJE.men.get("IngresarLugarInicio"))
							line=line.replace(LugarViejo, LugarNuevo).split(',')
							servicio.setLugarInicio(LugarNuevo)
							contenido.append(','.join(line))
							break
						elif cambio==4:
							LugarViejo=servicio.getLugarFin()
							LugarNuevo=input(MENSAJE.men.get("IngresarLugarFin"))
							line=line.replace(LugarViejo, LugarNuevo).split(',')
							servicio.setLugarFin(input(MENSAJE.men.get("IngresarLugarFin")))
							contenido.append(','.join(line))
							break
						elif cambio==5:
							AsientosViejo=servicio.getAsientosDisponibles()
							AsientosNuevo=input(MENSAJE.men.get("IngresarAsientosDisponibles"))
							line=line.replace(AsientosViejo, AsientosNuevo).split(',')
							servicio.setAsientosDisponibles(AsientosNuevo)
							contenido.append(','.join(line))
							break
						elif cambio==6:
							return
				else:
					line=line.split(',')
					contenido.append(','.join(line))
			with open('registro.txt', 'w') as archivo:
				archivo.writelines(contenido)
				return

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
			if infousuario=="Invalido":
				print(MENSAJE.men.get("ContraOCorreoInvalido"))
				infousuario=True

		if len(infousuario)==2:
			archivo=open("registro.txt", "r").readlines()
			line1=archivo[infousuario[0]].split(',')
			line2=archivo[infousuario[1]].split(',')
			PRINCIPAL.display_MenuVerificarCorreo()
			opcion=int(input())
			if opcion!=1 and opcion!=2 and opcion!=3:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if opcion==1:
				if "PASAJERO" ==line1[0]:
					infousuario = line1
				if "PASAJERO"==line2[0]:
					infousuario = line2
			elif opcion==2:
				if "CONDUCTOR"==line1[0]:
					infousuario = line1
				if "CONDUCTOR"==line2[0]:
					infousuario = line2
			elif opcion==3:
				infousuario = "salir"

		if len(infousuario)>2:
			if "PASAJERO"==infousuario[0]:
				PRINCIPAL.InicioSesionPasajero(infousuario)
			elif "CONDUCTOR"==infousuario[0]:
				PRINCIPAL.InicioSesionConductor(infousuario)
			elif "ADMINISTRADOR"==infousuario[0]:
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
			opcion=int(input(MENSAJE.men.get("Opcion")))
			print("")
			if opcion!=1 and opcion!=2:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion==1:
				PRINCIPAL.VerServicios()
			elif opcion==2:
				break
		
	@staticmethod
	def InicioSesionConductor(infousuario):
		if type(infousuario) == list:
			for conductor in CONDUCTOR.ListaConductores:
				if (conductor.getCorreo()==infousuario[1] and conductor.getContrasena()==infousuario[2] and conductor.getNombre()==infousuario[3] and conductor.getCell()==infousuario[4]):
					infousuario=conductor
					break

		while True:
			PRINCIPAL.display_MenuConductor()
			opcion=int(input(MENSAJE.men.get("Opcion")))
			print("")
			if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion==1:
				PRINCIPAL.ProgramarViaje(infousuario)
			elif opcion==2:
				PRINCIPAL.VerViajeActual(infousuario)
			elif opcion==3:
				SERVICIO.VerMiHistorial()
			elif opcion==4:
				PRINCIPAL.AgregarVehiculo(infousuario)
			elif opcion==5:
				for c in CONDUCTOR.VerVehiculos(infousuario):
					print(c)
			elif opcion==6:
				break
				
	@staticmethod
	def InicioSesionAdmin():
		
		while True:
			PRINCIPAL.display_MenuAdmin()
			opcion=int(input(MENSAJE.men.get("Opcion")))
			print("")
			if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion == 3:
				SERVICIO.ActualizarSerDis()
			elif opcion==4:
				break

	@staticmethod
	def idiomaMensajes():

		while True:
			print(MENSAJE.Mensaje.get("textoIdioma"))
			idioma = int(input(MENSAJE.Mensaje.get("SeleccioneIdioma")))
			if idioma ==1:
				MENSAJE.men = MENSAJE.espanol
				break
			elif idioma==2:
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
			elif "CONDUCTOR" == line[0]:
				CONDUCTOR(line[1], line[2], line[3], line[4])
			elif "VEHICULO" == line[0]:
				for conductor in CONDUCTOR.ListaConductores:
					correo=line[5].split()
					if correo[0] == conductor.getCorreo():
						VEHICULO(line[1], line[2], line[3], line[4], conductor, line[6])
			elif "SERVICIO" == line[0]:
				for conductor in CONDUCTOR.ListaConductores:
					correo=line[6].split()
					if correo[0] == conductor.getCorreo():
						SERVICIO(line[1], line[2], line[3], line[4], line[5], conductor, line[7])

		PRINCIPAL.idiomaMensajes()

		while True:
			self.display_MenuInicial()
			opcion=int(input(MENSAJE.men.get("Opcion")))
			print("")
			action=self.choicesInicial.get(opcion)
			if action:
				action()
			elif opcion!=1 and opcion!=3 and opcion!=2:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if opcion==2:
				self.runRegistrarme()

	def runRegistrarme(self):

		while True:
			self.display_MenuResgistrarme()
			opcion=int(input(MENSAJE.men.get("Opcion")))
			print("")
			action=self.choicesRegistrarme.get(opcion)
			if action:
				action()
				break
			elif opcion!=1 and opcion!=3 and opcion!=2:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if opcion==3:
				break

if __name__=="__main__":
	PRINCIPAL().runInicial()