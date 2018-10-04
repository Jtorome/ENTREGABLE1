from persona import PERSONA
from pasajero import PASAJERO
from conductor import CONDUCTOR
from servicio import SERVICIO
from calificacion import CALIFICACION
from vehiculo import VEHICULO
from comentario import COMENTARIO

class CORRER:

	archivo=open("registro.txt", "a")
	#X=(b'jtorom@unal.edu.co' in b'archivo')
	
	archivo=open("registro.txt", "r")
	for line in archivo:
		if "scabrera" in line:
			if "PASAJERO" in line:
				print line
	#pasajero1 = PASAJERO()
	#conductor1 = CONDUCTOR("tro@unal.edu.co", "1234", "Bla", "12324")
	#servicio1 = SERVICIO("7:30", "Agora", "Bloque 12", "M7", 3, conductor1 )
	#calificacion1 = CALIFICACION(3.0, "NO JODA CARE MONDA", conductor1, pasajero1, servicio1)
	#calificacion2 = CALIFICACION(4.0, "NO JODA CARE MONDA", conductor1, pasajero1, servicio1)
	#comentario1=COMENTARIO("MUY MALO", persona1)
	#print(comentario1.getFecha())

	#print(servicio1.getHoraEncuentro())
	#print(servicio1.getCalificacionPromedioSer())
	#print(conductor1.getAcumuladoCalificacion())
	#print(conductor1.getNumeroServicios())
	#print(pasajero1.getCalificacionPromedio())
	#print("TIPO DE VEHICULOS: ")
	#vehiculo1=VEHICULO("etd305", "rojo", "Carro", 5, conductor1)
	#vehiculo2=VEHICULO("s", "verde","Moto", 2, conductor1)
	#con=conductor1.getVehiculos()
	#for vehi in con:
#		print(vehi.getTipoVehiculo())
