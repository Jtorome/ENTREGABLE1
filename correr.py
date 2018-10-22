from persona import PERSONA
from pasajero import PASAJERO
from conductor import CONDUCTOR
from servicio import SERVICIO
from calificacion import CALIFICACION
from vehiculo import VEHICULO
from comentario import COMENTARIO

class CORRER:

	#archivo=open("registro.txt", "a")
	#X=(b'jtorom@unal.edu.co' in b'archivo')
	
	archivo=open("registro.txt", "r").readlines()
	a=archivo[1].split(',')
	print(a)
	"""linea=0
	for line in archivo:
		if "scabrera" in line:
			break
		linea=linea+1	
	X=archivo[linea]
	X=X.split(',')
	print(X)
	X=X[2]
	if X=="admin2":
		print(X)"""

	"""contra=0
	linea=0
	line1=0
	line2=0
	cont=0
	correo="juan@unal.edu.co"
	contrasena="hola"
	for line in archivo:
		cont=cont+1
		line=line.split(',')
		print(cont)
		if correo==line[1]:
			if contrasena==line[2]:
				contra=contra+1
				if(contra==1):
					line1=linea
				if(contra>1):
					line2=linea
		linea=linea+1

	line1=archivo[line1]
	line2=archivo[line2]
	print(line1)
	print(line2)"""
	
	#print(archivo[0])
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
