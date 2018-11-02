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
			2. Cerrar sesion
			""",

	"MenuConductor" :"""
					Inicio sesion como conductor
			1. Programar viaje
			2. Ver viaje actual
			3. Ver mi historial
			4. Agregar nuevo vehiculo
			5. Ver vehiculos
			6. Cerrar sesion
			""",
			
	"MenuAdmin":"""
					Estas en el menu de administrador
			1. Crear datos ficticios.
			2. Crear datos ficticios del txt.
			3. Actualizar servicios disponibles.
			4. Cerrar sesion.
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
	2. Atras.""",
			
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
	"IngresarDescripcion": "Por favor ingrese la descripcion: ",
	"CorreoInvalido": "Correo existente por favor ingrese otro: ",
	"CorreoInexistente": "El correo no esta registrado por favor registrese o ingrese uno que exista.",
	"ContraOCorreoInvalido": "Contrasena o correo invalidos.",
	"MensajeInicioSesion": """        Inicio de sesion
		Pulse 3 para salir.""",
	"CerradoSesion": "Has cerrado sesion.",
	"SinServicios": "En el momento no hay servicios disponibles.",
	"FormatoVerServicios": "{0}, hora de encuentro: {1}, sitio de encuentro: {2}, lugar de inicio: {3}, lugar de llegada: {4}, asientos disponibles: {5}, nombre del conductor: {6}.\n",
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
	"FormatoSetActivo": "{0}, {1}.",
	"FormatoViajeActual": "Hora de encuentro: {0}, sitio de encuentro: {1}, lugar de inicio: {2}, lugar de llegada: {3}, asientos disponibles: {4}",
		"IngresarFecha":"Favor ingresar fecha en formato yymmdd(maximo un mes de antelacion)",
	"FechaIncorrecta":"Formato invalido(yymmdd) o fecha limite excedida."
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
			2. Log out
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
	"FechaIncorrecta":"Invalid format(yymmdd) or limit date exceeded."

			}