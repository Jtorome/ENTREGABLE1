class MENSAJE:
	Mensaje = {
	"textoIdioma" : """ 
			1. Espanol(spanish)
			2. Ingles(english)
			""",
	"SeleccioneIdioma":"Seleccione una opcion / Select an option: "
			  }

	espanol = {

	"MenuInicial" :"""
			1. Iniciar Sesion
			2. Registrarme
			3. Salir
			""",
			
	"MenuRegistrarme" :"""
					Registrarme como:
			1. Conductor
			2. Pasajero
			3. Atras
			""",

	"MenuVerificarCorreo" :"""
					Quiere iniciar sesion como:
			1. Pasajero
			2. Conductor
			3. atras
			""",
			
	"MenuPasajero" :"""
					Inicio sesion como pasajero
			1. Ver servicios disponibles
			2. Informacion sobre mi viaje.
			3. Calificar servicio.
			4. Comentarios.
			5. Ver perfil.
			6. Cerrar sesion.
			""",

	"MenuConductor" :"""
					Inicio sesion como conductor
			1. Programar viaje
			2. Ver viaje actual
			3. Ver mi historial
			4. Agregar nuevo vehiculo
			5. Ver vehiculos
			6. Calificar pasajeros
			7. Comentarios
			8. Ver perfil
			9. Cerrar sesion
			""",
			
	"MenuAdmin":"""
					Estas en el menu de administrador
			1. Crear datos ficticios.
			2. Crear datos ficticios del txt.
			3. Actualizar servicios disponibles.
			4. Cerrar sesion.
			""",

	"MenuComentarios": """
	1. Hacer comentario a la plataforma o reportar algo.
	2. Ver mis comentarios.
	3. Atras
	""",

	"CambiarInfo": """"
					¿Que desea cambiar?
			1. Hora de encuentro.
			2. Sitio de encuentro.
			3. Lugar de inicio.
			4. Lugar de llegada.
			5. La cantidad de asientos.
			6. Atras.
			""",

	"MenuFormatoViajeActual":"""
			1. Cambiar informacion.
			2. Eliminar Servicio.
			3. Atras.""",

	"RevisarViaje": """
	Ingrese 0 para salir.
	¿Que viaje desea revisar?: 
	""",

	"MenuInfoViaje":"""
	1. Cancelar servicio.
	2. Atras
	""",

	"CambiarInfoVerPerfil":"""
	1. Cambiar contraseña.
	2. Cambiar numero de celular
	3. Atras
	""",
			
	"Opcion":"Ingrese la opcion: ",
	"NoViaje":"No tiene ningun viaje programado.",
	"NoHistorial":"No ha echo ningun viaje Intercampus.",
	"InfoVehiculo":"""	Ingrese la informacion del vehiculo a usar.
	Presione 3 para cancelar.""",
	"IngresarPlaca":"Ingrese la placa del vehiculo: ",
	"PlacaInvalida": "Placa ya existe en el sistema.",
	"IngresarColor":"Ingrese el color del vehiculo: ",
	"IngresarTipoVehiculo":"Ingrese el tipo de vehiculo(Carro o moto): ",
	"IngresarCantidadAsientos":"Ingrese la cantidad total de asientos del vehiculo: ",
	"ActivarVehiculo":"¿Va a utilizar este vehiculo en su proximo viaje?(Si o No)",
	"OpcionIncorrecta":"{0} no es una opcion valida.",
	"IngresarCorreo":"Ingrese su correo: ",
	"IngresarContrasena": "Ingrese su Contrasena: ",
	"IngresarNombre": "Ingrese su nombre:",
	"IngresarCell": "Ingrese su celular:",
	"Antes@": "Por favor escriba su usuario antes del @",
	"Salir": "Chaito",
	"IngresarDescripcion": "Ingrese 3 para salir.\nPor favor ingrese la descripcion: ",
	"CorreoInvalido": "Correo existente por favor ingrese otro: ",
	"CorreoInexistente": "El correo no esta registrado por favor registrese o ingrese uno que exista.",
	"ContraOCorreoInvalido": "Contrasena o correo invalidos.",
	"MensajeInicioSesion": """        Inicio de sesion
		Pulse 3 para salir.""",
	"CerradoSesion": "Has cerrado sesion.",
	"SinServicios": "En el momento no hay servicios disponibles.",
	"FormatoVerServicios": "{0}, hora de encuentro: {1}, sitio de encuentro: {2}, lugar de inicio: {3}, lugar de llegada: {4}, asientos disponibles: {5}, nombre del conductor: {6}, Fecha: {7}.\n",
	"InfoServicio": """	Ingrese la informacion del servicio.
	Presione 3 para cancelar.""",
	"IngresarHoraEncuentro": "Ingrese la hora de encuentro(24h): ",
	"IngresarSitioEncuentro": "Ingrese el campus de encuentro(Volador, minas, rio): ",
	"IngresarLugarInicio": "Ingrese el lugar donde iniciara el viaje(Ejemplo:bloque M8, 12, 4): ",
	"IngresarLugarFin": "Ingrese el lugar donde terminara el viaje(Ejemplo:bloque M8, 12, 4): ",
	"IngresarAsientosDisponibles": "Ingrese la cantidad de asientos disponibles: ",
	"ServicioEnCurso": "Usted ya tiene un servicio en curso por favor termine ese antes de programar otro.",
	"IngreseServicioEscogido": """
	Ingrese 0 para salir.
	Ingrese el servicio que desea tomar: """,
	"FormatoViajeActual": "Hora de encuentro: {0}, sitio de encuentro: {1}, lugar de inicio: {2}, lugar de llegada: {3}, asientos disponibles: {4}",
	"IngresarFecha":"""¿Cuando va a realizar su viaje: 1.Hoy.
                                2. Mañana: """,
	"SinServiciosCon":"Usted no tiene viaje programado.",
	"NoPuedeTomarSer":"Usted no puede tomar este servicio.",
	"ViajeLleno":"Ya no quedan asientos en este viaje por favor tomar otro",
	"RegistradoEnSer":"Usted a quedado registrado en el servicio que parte a las {0} del {1} hacia {2}",
	"AsientosMaximos":"La cantidad maxima de asientos disponibles para un {0} son {1}",
	"HoraYaPaso":"La hora ingresada ya paso. Por favor ingrese una hora que no haya pasado {0} son {1}",
	"FormatoInfoSer": "Informacion sobre el servicio.\nHora de encuentro: {0}, sitio de encuentro: {1}, lugar de inicio: {2}, lugar de llegada: {3}, asientos disponibles: {4}, Fecha: {5}.\n",
	"FormatoInfoCon": "Informacion Sobre el conductor.\nNombre: {0}, Celular: {1}, servicios hechos: {2}, Acumulado de calificacion: {3}.\n",
	"FormatoInfoVehi": "Informacion sobre el vehiculo.\nPlaca: {0}, color: {1}, tipo de vehiculo: {2}.\n",
	"HistorialVacio": "Usted no ha hecho ningun viaje.",
	"FormatoVerMiHistorial": "	Su historial es.\n{0}. Fecha: {1}, hora de salida: {2}, lugar de inicio: {3}, lugar de llegada: {4}, puntuacion: {5}.",
	"FormatoRevisarPasajero": "{0}. Nombre: {1}, celular: {2}, puntuacion: {3}.",
	"ServicioCancelado": "Su viaje a sido cancelado exitosamente.",
	"ServicioEliminado": "Servicio eliminado exitosamente.",
	"ValorMalCali": "Valor ingresado no es valido.",
	"IngresarCalificacion": """
	Ingrese 6 para salir.
Por favor ingrese la calificacion para el servicio de 0 a 5 siendo 0 muy malo y 5 muy bueno: """,
	"IngresarComentario": "Comentario sobre el servicio: ",
	"DeseaComentar": """¿Desea dejar un comentario con calificacion?: 1. Si
                                              2. No: """,
    "ServicioACalificar": "¿Que servicio desea calificar?\nIngrese 'b' para salir: ",
    "SinServiciosCalificacion": "Sin servicios para calificar.",
    "SinPasajerosPorCalificar": "Usted no tiene ningun pasajero por calificar.",
    "PasajeroACalificar": "¿Que pasajero desea calificar?\nIngrese 'b' para salir: ",
    "FormatoVerPerfilPasajero": "Correo: {0}, Contrasena: {1}, Nombre: {2}, Celular: {3}, Calificacion Promedio: {4}.",
    "IngresarNuevaContrasena": "Ingrese la nueva contrasena por favor: ",
    "IngresarNuevoCell": "Ingrese el nuevo numero celular: ",
    "FormatoVerPerfilConductor": "Correo: {0}, Contrasena: {1}, Nombre: {2}, Celular: {3}, Servicio hechos: {4}, Acumulado de calificaciones: {5}. ",
    "FormatoComentarios": "{0}    {1}\n{2}."
	}
	

	ingles = {
   "MenuInicial" :"""
			1. Log in
			2. Sign in 
			3. Exit
			""",
			
	"MenuRegistrarme" :"""
					Sign in as:
			1. Driver
			2. Passenger
			3. Back
			""",
			
	"MenuVerificarCorreo" :"""
					Please select your rol:
			1. Rider
			2. Driver
			3. Exit
			""",

	"MenuPasajero" :"""
					Login as rider
			1. Available services
			2. Information about my trip
			3. Log out
			""",
			
	"MenuConductor" :"""
					Login as conductor
			1. Schedule trip
			2. View current trip
			3. View my historial
			4. Log out
			""",

	"MenuProgramarViaje":"""
					You are planning a trip
			1.
			2.
			3. Exit
			""",
			
	"MenuAdministrador":"""
					You are in the menu of administrators
			1. View administrators
			2. View users registered
			3. View historial trips
			4. Log out 
			""",
	"MenuFormatoViajeActual":"""
			1. Change information.
			2. Delete servic.
			3. Back.""",
			
	"Opcion":"Select an option: ",
	"NoViaje":"You have not sheduled trip.",
	"NoHistorial":"You have not done any intercampus trip.",
	"InfoVehiculo":"""	Enter the vehicle information to use.
	Select 3 to cancel""",
	"IngresarPlaca":"Enter the number of license plate: ",
	"PlacaInvalida": "License plate already existing in the system.",
	"IngresarColor":"Enter the color of vehicle: ",
	"IngresarTipoVehiculo":"Enter the vehicle type(car or motorcycle): ",
	"IngresarCantidadAsientos": "Enter the total number of seats of the vehicle: ",
	"ActivarVehiculo":"Will you use this vehicle on your next trip? (Yes or No)",
	"OpcionIncorrecta":"{0} Is not valid choice. ",
	"IngresarCorreo":"Enter your mail: ",
	"IngresarContrasena": "Enter your password:  ",
	"IngresarNombre": "Enter your name:",
	"IngresarCell": "Enter your cellphone",
	"Antes@": "Please write your user before that @",
	"Salir": "Bye Bye",
	"IngresarDescripcion": "Please enter the description: ",
	"CorreoInvalido": "Existing mail please enter another: ",
	"CorreoInexistente": "The mail is not registered, please register or enter a valid mail",
	"ContraOCorreoInvalido": "Mail or password invalid.",
	"MensajeInicioSesion": """        Login
		Enter 3 to exit.""",
	"CerradoSesion": "Make closed session. ",
	"SinServicios": "There are no services available",
	"FormatoVerServicios": "{0}, Meeting time: {1}, Meetin place: {2}, Start place: {3}, Place of arrival: {4}, Available seats: {5}, Name of condutor: {6}.\n",
	"InfoServicio": """	Enter the information of service.
	Enter 3 to cancel.""",
	"IngresarHoraEncuentro": "Enter the meeting time(24h): ",
	"IngresarSitioEncuentro": "Enter the meeting place(Volador, minas, rio): ",
	"IngresarLugarInicio": "Enter the place where star the service(Example:bloque M8, 12, 4): ",
	"IngresarLugarFin": "Enter the place where the service will end(Example:bloque M8, 12, 4): ",
	"IngresarAsientosDisponibles": "Enter the number of seats available: ",
	"ServicioEnCurso": "You already have an ongoing service, please finish that before you schedule another.",
	"IngreseServicioEscogido": """
	Enter 0 to exit.
	Enter the servic that wish take: """,
	"FormatoSetActivo": "{0}, {1}.",
	"FormatoViajeActual": "Meeting time: {0}, Meeting place: {1}, Start place: {2}, Place of arrival: {3}, Available seats: {4}",
	"IngresarFecha":"Please enter date in format yymmdd(maximum one month in advance)",
	"FechaIncorrecta":"Invalid format(yymmdd) or limit date exceeded.",
	"SinServiciosCon":"You have no trip sheduled.",
	"NoPuedeTomarSer":"You must not take this service.",
	"ViajeLleno":"There are no seats left in this trip please take another",
	"RegistradoEnSer":"You have been registered in the service that leaves at {0} of {1} to {2}",
	"AsientosMaximos":"The maximum number of seats available for a {0} is {1}",
	"HoraYaPaso":"The time entered already step. Please enter a time that has not passed {0} are {1}",
	"FormatoInfoSer": "Information about the service. \n Meeting time: {0}, meeting place: {1}, starting place: {2}, place of arrival: {3}, available seats: {4}, Date: {5} . \n",
	"FormatoInfoCon": "Information about the conductor.\n Name: {0}, Cellphone: {1}, services done: {2}, Accumulated qualification: {3}.\n",
	"FormatoInfoVehi": "Information about the vehicule.\n License plate: {0}, color: {1}, Vehicle type: {2}.\n"
	}	