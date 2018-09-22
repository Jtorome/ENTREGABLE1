from persona import PERSONA
from pasajero import PASAJERO
from conductor import CONDUCTOR
from servicio import SERVICIO
from calificacion import CALIFICACION
from vehiculo import VEHICULO

class CORRER:
	
	#persona1=PERSONA()
	pasajero1 = PASAJERO()
	conductor1 = CONDUCTOR()
	servicio1 = SERVICIO("7:30", "Agora", "Bloque 12", "M7", 3, conductor1 )
	calificacion1 = CALIFICACION(3.0, "NO JODA CARE MONDÁ", conductor1, pasajero1, servicio1)
	calificacion2 = CALIFICACION(4.0, "NO JODA CARE MONDÁ", conductor1, pasajero1, servicio1)

	print(servicio1.getHoraEncuentro())
	print(servicio1.getCalificacionPromedioSer())
	print(conductor1.getAcumuladoCalificacion())
	print(conductor1.getNumeroServicios())
	print(pasajero1.getCalificacionPromedio())
	print("TIPO DE VEHICULOS: ")
	vehiculo1=VEHICULO("etd305", "rojo", "Carro", 5, conductor1)
	vehiculo2=VEHICULO("s", "verde","Moto", 2, conductor1)
	con=conductor1.getVehiculos()
	for vehi in con:
		print(vehi.getTipoVehiculo())
