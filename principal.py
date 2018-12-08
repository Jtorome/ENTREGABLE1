import os
from persona import PERSONA
from conductor import CONDUCTOR
from pasajero import PASAJERO
from vehiculo import VEHICULO
from servicio import SERVICIO
from comentario import COMENTARIO
from calificacion import CALIFICACION
from mensaje import MENSAJE
from ficticio import FICTICIO
from datetime import datetime, date, timedelta
import time

class PRINCIPAL:

	def __init__(self):

		self.choicesInicial={
		"1": self.IniciarSesion,
		#"2": self.Registrarme,
		"3": FICTICIO.DatosFicticiosTxt,
		"4": self.SalirPrincipal
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
		archivo.write("CONDUCTOR,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0,0\n")
		PRINCIPAL.AgregarVehiculo(conductor)

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
		TipoVehiculo=(input(MENSAJE.men.get("IngresarTipoVehiculo"))).lower()
		if TipoVehiculo=="moto":
			CantidadAsientos=2
		elif TipoVehiculo=="carro":
			CantidadAsientos=5
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
		VEHICULO(Placa, ColorVehiculo, TipoVehiculo, int(CantidadAsientos), conductor, Activo)
		archivo.write("VEHICULO,"+Placa+","+ColorVehiculo+","+TipoVehiculo+","+str(CantidadAsientos)+","+conductor.getCorreo()+","+Activo+"\n")

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
		archivo.write("PASAJERO,"+Correo+","+Contrasena+","+Nombre+","+Cell+",0\n")

	@staticmethod
	def ProgramarViaje(infousuario):
		SERVICIO.ActualizarSerDis()
		vehiculo=CONDUCTOR.VehiculoActivado(infousuario)
		if vehiculo.getTipoVehiculo()=="moto":
			MaxAsientosDis=1
		elif vehiculo.getTipoVehiculo()=="carro":
			MaxAsientosDis=4
		for servicio in SERVICIO.ServiciosDisponibles:
			if servicio.getConductorSer() == infousuario:
				return print(MENSAJE.men.get("ServicioEnCurso"))
		print(MENSAJE.men.get("InfoServicio"))
		while True:
			HoraEncuentro=input(MENSAJE.men.get("IngresarHoraEncuentro"))
			if HoraEncuentro=="3":
				return
			if HoraEncuentro<=time.strftime("%H:%M"):
				print(MENSAJE.men.get("HoraYaPaso"))
			elif HoraEncuentro>time.strftime("%H:%M"):
				break
		SitioEncuentro=input(MENSAJE.men.get("IngresarSitioEncuentro"))
		LugarInicio=input(MENSAJE.men.get("IngresarLugarInicio"))
		LugarFin=input(MENSAJE.men.get("IngresarLugarFin"))
		while True:
			AsientosDisponibles=input(MENSAJE.men.get("IngresarAsientosDisponibles"))
			if int(AsientosDisponibles)>MaxAsientosDis:
				print(MENSAJE.men.get("AsientosMaximos").format(vehiculo.getTipoVehiculo(), MaxAsientosDis))
			else:
				break
		while True:
			while True:
				opcion=eval(input(MENSAJE.men.get("IngresarFecha")))
				if type(opcion)!=int:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				elif opcion<1 and opcion>2:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				else:
					break
			if opcion==1:
				FechaSer=time.strftime("%y/%m/%d")
				break
			elif opcion==2:
				FechaSer=(datetime.today()+timedelta(days=1)).strftime("%y/%m/%d")
				break
		SERVICIO(HoraEncuentro, SitioEncuentro, LugarInicio, LugarFin, AsientosDisponibles, infousuario, FechaSer)
		archivo=open("registro.txt", "a")
		archivo.write("SERVICIO,"+HoraEncuentro+","+SitioEncuentro+","+LugarInicio+","+LugarFin+","+AsientosDisponibles+","+infousuario.getCorreo()+","+FechaSer+",0\n")

	@staticmethod
	def CrearComentario(infousuario):
		persona=PERSONA.BuscarPersona(infousuario.getCorreo())
		Descripcion=input(MENSAJE.men.get("IngresarDescripcion"))
		if Descripcion=="3":
			return
		Fecha=time.strftime("%d/%m/%y")
		COMENTARIO(Descripcion, persona, Fecha)
		archivo=open("registro.txt", "a")
		archivo.write("COMENTARIO,"+Descripcion+","+persona.getCorreo()+","+Fecha+"\n")

	@staticmethod
	def SalirPrincipal():
		print(MENSAJE.men.get("salir"))
		os._exit(0)

	@staticmethod
	def VerServicios(infousuario):
		SERVICIO.ActualizarSerDis()
		if len(SERVICIO.ServiciosDisponibles) == 0:
			return print(MENSAJE.men.get("SinServicios"))
		else:
			cont=1
			for servicio in SERVICIO.ServiciosDisponibles:
				print(MENSAJE.men.get("FormatoVerServicios").format(cont, servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre(), servicio.getFechaSer()))
				cont=cont+1
		PRINCIPAL.EscogerServicio(infousuario)

	@staticmethod
	def EscogerServicio(infousuario):
		while True:
			opcion=eval(input(MENSAJE.men.get("IngreseServicioEscogido")))
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion<0 and opcion>len(SERVICIO.ServiciosDisponibles):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if opcion==0:
				break
			else:
				servicio=SERVICIO.ServiciosDisponibles[opcion-1]
				if servicio.getAsientosDisponibles() == 0:
					return print(MENSAJE.men.get("ViajeLleno"))
				return print(SERVICIO.ServicioTomado(infousuario, servicio))

	@staticmethod
	def VerViajeActual(infousuario):
		SERVICIO.ActualizarSerDis()
		if len(infousuario.getServicioActual())==0:
			return print(MENSAJE.men.get("SinServiciosCon"))
		servicio=infousuario.getServicioActual()[0]
		print(MENSAJE.men.get("FormatoViajeActual").format(servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles()))
		print(MENSAJE.men.get("MenuFormatoViajeActual"))
		while True:
			opcion=eval(input(MENSAJE.men.get("Opcion")))
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if opcion<1 and opcion>3:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			else:
				break
		if opcion == 3:
			return
		elif opcion == 2:
			print(SERVICIO.EliminarServicio(servicio))
		elif opcion == 1:
			PRINCIPAL.CambioInfoSer(servicio)

	@staticmethod
	def CambioInfoSer(servicio):
		print(MENSAJE.men.get("CambiarInfo"))
		archivo=open("registro.txt", "r").readlines()
		contenido=list()
		for line in archivo:
			if "SERVICIO"==line.split(',')[0] and servicio.getHoraEncuentro()==line.split(',')[1] and servicio.getFechaSer()==line.split(',')[7] and servicio.getConductorSer().getCorreo()==line.split(',')[6]:
				while True:
					while True:
						cambio=eval(input(MENSAJE.men.get("Opcion")))
						if type(cambio)!=int:
							print(MENSAJE.men.get("OpcionIncorrecta").format(cambio))
						elif cambio<1 and cambio>6:
							print(MENSAJE.men.get("OpcionIncorrecta").format(cambio))
						else:
							break
					if cambio==1:
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
	def InfoViaje(infousuario):
		if len(infousuario.getViajeActual())==0:
			return print(MENSAJE.men.get("SinServicios"))
		Servicio=infousuario.getViajeActual()[0]
		print(MENSAJE.men.get("FormatoInfoSer").format(Servicio.getHoraEncuentro(), Servicio.getSitioEncuentro(), Servicio.getLugarInicio(), Servicio.getLugarFin(), Servicio.getAsientosDisponibles(), Servicio.getFechaSer()))
		conductor=Servicio.getConductorSer()
		print(MENSAJE.men.get("FormatoInfoCon").format(conductor.getNombre(), conductor.getCell(), conductor.getNumeroServicios(), conductor.getAcumuladoCalificacion()))
		vehiculo=CONDUCTOR.VehiculoActivado(conductor)
		print(MENSAJE.men.get("FormatoInfoVehi").format(vehiculo.getPlaca(), vehiculo.getColor(), vehiculo.getTipoVehiculo()))
		PRINCIPAL.MenuInfoViaje(infousuario)

	@staticmethod
	def MenuInfoViaje(infousuario):
		while True:
			print(MENSAJE.men.get("MenuInfoViaje"))
			opcion=eval(input(MENSAJE.men.get("Opcion")))
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion<1 and opcion>2:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			else:
				break
		if opcion==1:
			servicio=infousuario.getViajeActual()[0]
			return print(SERVICIO.EliminarPasajero(infousuario, servicio))
		elif opcion==2:
			return

	@staticmethod
	def VerMiHistorial(infousuario):
		if len(CONDUCTOR.getServiciosCon(infousuario))==0:
			return print(MENSAJE.men.get("HistorialVacio"))
		cont=1
		for servicio in CONDUCTOR.getServiciosCon(infousuario):
			print(MENSAJE.men.get("FormatoVerMiHistorial").format(cont, servicio.getFechaSer(), servicio.getHoraEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getCalificacionPromedioSer()))
			cont=cont+1
		PRINCIPAL.RevisarServicio(infousuario)

	@staticmethod
	def RevisarServicio(infousuario):
		while True:
			opcion=eval(input(MENSAJE.men.get("RevisarViaje")))
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion==0:
				return
			elif opcion<0 and opcion>len(CONDUCTOR.getServiciosCon(infousuario)):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			else:
				break
		servicio=(CONDUCTOR.getServiciosCon(infousuario))[opcion-1]
		cont=1
		for pasajero in servicio.getPasajeros():
			print(MENSAJE.men.get("FormatoRevisarPasajero").format(cont, pasajero.getNombre(), pasajero.getCell(), pasajero.getCalificacionPromedio()))
			cont=cont+1

	@staticmethod
	def CalificarServicio(infousuario):
		SERVICIO.ActualizarSerDis()
		if len(infousuario.getServicioNoCalificado())==0:
			return print(MENSAJE.men.get("SinServiciosCalificacion"))
		cont=1
		for servicio in infousuario.getServicioNoCalificado():
			print(MENSAJE.men.get("FormatoVerServicios").format(cont, servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre(), servicio.getFechaSer()))
			cont=cont+1
		while True:
			opcion=eval(input(MENSAJE.men.get("ServicioACalificar")))
			if opcion=="b":
				return
			elif type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion<=0 and opcion>len(infousuario.getServicioNoCalificado()):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			else:
				opcion=opcion-1
				break
		servicio=infousuario.getServicioNoCalificado()[opcion]
		while True:
			Calificacion=eval(input(MENSAJE.men.get("IngresarCalificacion")))
			if type(Calificacion)!=int:
				print(MENSAJE.men.get("ValorMalCali"))
			elif Calificacion<0 and Calificacion>5:
				print(MENSAJE.men.get("ValorMalCali"))
			elif Calificacion == 6:
				return
			else:
				break
		while True:
			opcion=input(MENSAJE.men.get("DeseaComentar"))
			if opcion!="1" and opcion!="2":
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion=="1":
				Comentario=input(MENSAJE.men.get("IngresarComentario"))
				break
			elif opcion=="2":
				Comentario=None
				break
		CALIFICACION(Calificacion, Comentario, None, servicio)
		infousuario.getServicioNoCalificado().remove(servicio)
		archivo=open("registro.txt", "a")
		archivo.write("CALIFICACION,"+str(Calificacion)+","+str(Comentario)+","+str(None)+","+servicio.getHoraEncuentro()+","+servicio.getConductorSer().getCorreo()+","+servicio.getFechaSer()+","+infousuario.getCorreo()+"\n")

	@staticmethod
	def CalificarPasajeros(infousuario):
		SERVICIO.ActualizarSerDis()
		if len(infousuario.getPasajeroNoCalificado())==0:
			return print(MENSAJE.men.get("SinPasajerosPorCalificar"))
		cont=1
		for pasajero in infousuario.getPasajeroNoCalificado():
			print(MENSAJE.men.get("FormatoRevisarPasajero").format(cont, pasajero.getNombre(), pasajero.getCell(), pasajero.getCalificacionPromedio()))
			cont=cont+1
		while True:
			opcion=eval(input(MENSAJE.men.get("PasajeroACalificar")))
			if opcion=="b":
				return
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion<0 and opcion>len(infousuario.getPasajeroNoCalificado()):
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			else:
				opcion=opcion-1
				break
		pasajero=infousuario.getPasajeroNoCalificado()[opcion]
		while True:
			Calificacion=eval(input(MENSAJE.men.get("IngresarCalificacion")))
			if type(Calificacion)!=int:
				print(MENSAJE.men.get("ValorMalCali"))
			elif Calificacion<0 and Calificacion>5:
				print(MENSAJE.men.get("ValorMalCali"))
			elif Calificacion == 6:
				return
			else:
				break
		while True:
			opcion=input(MENSAJE.men.get("DeseaComentar"))
			if opcion!="1" and opcion!="2":
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion=="1":
				Comentario=input(MENSAJE.men.get("IngresarComentario"))
				break
			elif opcion=="2":
				Comentario=None
				break
		CALIFICACION(Calificacion, Comentario, pasajero)
		infousuario.getPasajeroNoCalificado().remove(pasajero)
		archivo=open("registro.txt", "a")
		archivo.write("CALIFICACION,"+str(Calificacion)+","+str(Comentario)+","+pasajero.getCorreo()+","+infousuario.getCorreo()+"\n")

	@staticmethod
	def VerPerfil(palabra, infousuario):
		if palabra=="PASAJERO":
			print(MENSAJE.men.get("FormatoVerPerfilPasajero").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getCalificacionPromedio()))
		elif palabra=="CONDUCTOR":
			print(MENSAJE.men.get("FormatoVerPerfilConductor").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getNumeroServicios(), infousuario.getAcumuladoCalificacion()))
		while True:
			print(MENSAJE.men.get("CambiarInfoVerPerfil"))
			opcion=eval(input(MENSAJE.men.get("Opcion")))
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion<1 and opcion>3:
				print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			elif opcion==3:
				return
			else:
				PRINCIPAL.CambiarInfoVerPerfil(palabra, opcion, infousuario)
				if palabra=="PASAJERO":
					return print(MENSAJE.men.get("FormatoVerPerfilPasajero").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getCalificacionPromedio()))
				elif palabra=="CONDUCTOR":
					return print(MENSAJE.men.get("FormatoVerPerfilConductor").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getNumeroServicios(), infousuario.getAcumuladoCalificacion()))

	@staticmethod
	def CambiarInfoVerPerfil(palabra, opcion, infousuario):
		if opcion==1:
			contrasena=input(MENSAJE.men.get("IngresarNuevaContrasena"))
			archivo=open("registro.txt","r").readlines()
			contenido=list()
			for line in archivo:
				line=line.split(',')
				if line[0]==palabra and line[1]==infousuario.getCorreo():
					line[2]=contrasena
					contenido.append(','.join(line))
					infousuario.setContrasena(contrasena)
				else:
					contenido.append(','.join(line))
			with open("registro.txt", "w") as archivo:
				archivo.writelines(contenido)
		elif opcion==2:
			cell=input(MENSAJE.men.get("IngresarNuevoCell"))
			archivo=open("registro.txt", "r").readlines()
			contenido=list()
			for line in archivo:
				line=line.split(',')
				if line[0]==palabra and line[1]==infousuario.getCorreo():
					line[4]=cell
					contenido.append(','.join(line))
					infousuario.setCell(cell)
				else:
					contenido.append(','.join(line))
			with open("registro.txt", "w") as archivo:
				archivo.writelines(contenido)

	@staticmethod
	def Comentarios(infousuario):
		print(MENSAJE.men.get("MenuComentarios"))
		while True:
			opcion=eval(input(MENSAJE.men.get("Opcion")))
			if type(opcion)!=int:
				print(MENSAJE.men.get("OpcionIncorrecta"))
			elif opcion<1 and opcion>3:
				print(MENSAJE.men.get("OpcionIncorrecta"))
			else:
				break
		if opcion==1:
			PRINCIPAL.CrearComentario(infousuario)
		elif opcion==2:
			PRINCIPAL.VerHistorialComen(infousuario)
		elif opcion==3:
			return

	@staticmethod
	def VerHistorialComen(infousuario):
		persona=PERSONA.BuscarPersona(infousuario.getCorreo())
		for comentario in persona.getComentarios():
			print(MENSAJE.men.get("FormatoComentarios").format(infousuario.getNombre(), comentario.getFecha(), comentario.getDescripcion()))

	@staticmethod
	def IniciarSesion():
		infousuario=True
		while infousuario==True:
			print(MENSAJE.men.get("MensajeInicioSesion"))
			correo=(input(MENSAJE.men.get("IngresarCorreo"))).lower()
			if correo=="3":
				return
			contrasena=input(MENSAJE.men.get("IngresarContrasena"))
			infousuario=PERSONA.VerificarCorreo(correo, contrasena)
			if infousuario=="Invalido":
				print(MENSAJE.men.get("ContraOCorreoInvalido"))
				infousuario=True

		if len(infousuario)==2 and type(infousuario)==list:
			archivo=open("registro.txt", "r").readlines()
			line1=archivo[infousuario[0]].split(',')
			line2=archivo[infousuario[1]].split(',')
			PRINCIPAL.display_MenuVerificarCorreo()
			while True:
				opcion=eval(input())
				if type(opcion)!=int:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				elif opcion<1 and opcion>3:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				else:
					break
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
				return

		if len(infousuario)>2 and type(infousuario)==list:
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
			while True:
				opcion=eval(input(MENSAJE.men.get("Opcion")))
				print("")
				if type(opcion)!=int:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				elif opcion<1 and opcion>6:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				else:
					break
			if opcion==1:
				PRINCIPAL.VerServicios(infousuario)
			elif opcion==2:
				PRINCIPAL.InfoViaje(infousuario)
			elif opcion==3:
				PRINCIPAL.CalificarServicio(infousuario)
			elif opcion==4:
				PRINCIPAL.Comentarios(infousuario)
			elif opcion==5:
				PRINCIPAL.VerPerfil("PASAJERO", infousuario)
			elif opcion==6:
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
			while True:
				opcion=eval(input(MENSAJE.men.get("Opcion")))
				print("")
				if type(opcion)!=int:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				elif opcion<1 and opcion>9:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				else:
					break
			if opcion==1:
				PRINCIPAL.ProgramarViaje(infousuario)
			elif opcion==2:
				PRINCIPAL.VerViajeActual(infousuario)
			elif opcion==3:
				PRINCIPAL.VerMiHistorial(infousuario)
			elif opcion==4:
				PRINCIPAL.AgregarVehiculo(infousuario)
			elif opcion==5:
				for c in CONDUCTOR.VerVehiculos(infousuario):
					print(c)
			elif opcion==6:
				PRINCIPAL.CalificarPasajeros(infousuario)
			elif opcion==7:
				PRINCIPAL.Comentarios(infousuario)
			elif opcion==8:
				PRINCIPAL.VerPerfil("CONDUCTOR", infousuario)
			elif opcion==9:
				return
				
	@staticmethod
	def InicioSesionAdmin():
		
		while True:
			PRINCIPAL.display_MenuAdmin()
			while True:
				opcion=eval(input(MENSAJE.men.get("Opcion")))
				print("")
				if type(opcion)!=int:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				elif opcion<1 and opcion>4:
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
				else:
					break
			if opcion == 3:
				SERVICIO.ActualizarSerDis()
			elif opcion==4:
				break

	@staticmethod
	def idiomaMensajes():

		while True:
			print(MENSAJE.Mensaje.get("textoIdioma"))
			while True:
				idioma = eval(input(MENSAJE.Mensaje.get("SeleccioneIdioma")))
				if type(idioma)!=int:
					print(MENSAJE.espanol.get("OpcionIncorrecta").format(idioma))
					print(MENSAJE.ingles.get("OpcionIncorrecta").format(idioma))
				elif idioma<1 and idioma>2:
					print(MENSAJE.espanol.get("OpcionIncorrecta").format(idioma))
					print(MENSAJE.ingles.get("OpcionIncorrecta").format(idioma))
				else:
					break
			if idioma ==1:
				MENSAJE.men = MENSAJE.espanol
				return
			elif idioma==2:
				MENSAJE.men = MENSAJE.ingles
				return

	def runInicial(self):

		PRINCIPAL.idiomaMensajes()

		while True:
			self.display_MenuInicial()
			opcion=input(MENSAJE.men.get("Opcion"))
			print("")
			action=self.choicesInicial.get(opcion)
			if action:
				action()
			if opcion!="1" and opcion!="3" and opcion!="2" and opcion!="4":
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
			if opcion!="1" and opcion!="3" and opcion!="2":
					print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
			if opcion=="3":
				break

if __name__=="__main__":
	PRINCIPAL().runInicial()