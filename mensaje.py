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
			1. Ver servicios disponibles.
			2. Informacion sobre mi viaje.
			3. Cerrar sesion.
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
	2. Eliminar servicio.
	3. Atras.""",

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
	"SinServiciosCon": "Usted no tiene viaje programado.",
	"NoPuedeTomarSer": "Usted no puede tomar este servicio ya que usted mismo lo propuso.",
	"ViajeLleno": "Ya no quedan cupos en este viaje por favor toma otro.",
	"RegistradoEnSer": "Usted a quedado registrado en el servicio que parte a las {0} del {1} hacia {2}",
	"AsientosMaximos": "La cantidad maxima de asientos disponibles para un {0} son {1}",
	"HoraYaPaso": "La hora ingresada ya paso. Por favor ingrese una hora que no haya pasado.",
	"FormatoInfoSer": "Informacion sobre el servicio.\nHora de encuentro: {0}, sitio de encuentro: {1}, lugar de inicio: {2}, lugar de llegada: {3}, asientos disponibles: {4}, Fecha: {5}.\n",
	"FormatoInfoCon": "Informacion Sobre el conductor.\nNombre: {0}, Celular: {1}, servicios hechos: {2}, Acumulado de calificacion: {3}.\n",
	"FormatoInfoVeh": "Informacion sobre el vehiculo.\nPlaca: {0}, color: {1}, tipo de vehiculo: {2}.\n"
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
			
	"Opcion": "Select an option:",   
	"NoViaje":"You have no scheduled trip ",
	"NoHistorial":"You have not done any Intercampus trip ", 
	"InfoVehiculo":"Enter the vehicle information to use ",
	"IngresarPlaca":"Enter the number of license plate: ",
	"IngresarColor":"Enter the color of vehicle: ",
	"IngresarTipoVehiculo":"Enter the vehicle type: ",
	"IngresarCantidadAsientos":"Ingrese la cantidad total de asientos del vehiculo: ",
	"OpcionIncorrecta": "{0} is not a valid choice.",
	"IngresarCorreo":"Enter your mail: ",
	"IngresarContrasena": "Enter your password: ",
	"IngresarNombre":"Enter your name: ",
	"IngresarCell": "Enter your cellphone: ",
	"Antes@": "Plase enter your user before that @",
	"Salir": "Bye Bye",
	"IngresarDescripcion": "How was your travel ?: ",
	"CorreoInvalido": "The email address you have entered is already registered: ",
	"CorreoInexistente": "The email you entered is not registered: ",
	"ContrasenaInvalida": "Invalid password.",
	"MensajeInicioSesion": """        Login
		Press 3 to exit."""

			}