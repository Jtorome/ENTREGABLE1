from persona import PERSONA
from pasajero import PASAJERO
from conductor import CONDUCTOR
from servicio import SERVICIO
from calificacion import CALIFICACION
from vehiculo import VEHICULO
from comentario import COMENTARIO
from mensaje import MENSAJE
import time

class CORRER: 

	opcion= int(input())
	if opcion != (1, 2, 3, 4, 5):
		print(MENSAJE.espanol.get("OpcionIncorrecta").format(opcion))
	"""actual=time.strftime("%y/%m/%d")
	a=actual.split('/')
	pasada="18/09/31"
	p=pasada.split('/')
	if actual > pasada:
		print("SIP")
	if a[2] >= p[2] and a[1] >= p[1] and a[0] > p[0]:
		print("DIA MAYOR")
	elif a[2] >= p[2] and a[1] >= p[1] and a[0] == p[0]:
		print("DIA IGUAL")"""

	"""archivo=open("registro.txt", "r").readlines()
	out=open("registro.txt", "w")
	for line in archivo:
		line=line.replace(",ACTIVO", "")
		out.writelines(line)"""

	"""contenido= list()

	with open('registro.txt', 'r') as archivo:
		for linea in archivo:
			columnas = linea.replace(",ACTIVO", "")
			columnas= columnas.split(',')
			contenido.append(','.join(columnas))

	print(contenido)
	with open('registro.txt', 'w') as archivo:
		archivo.writelines(contenido)"""

	"""actual=time.strftime("%H:%M")
	pasada="17:59"
	if pasada>actual:
		print("SI")"""

	"""conductor1 = CONDUCTOR("tro@unal.edu.co", "1234", "Bla", "12324")
	servicio1=SERVICIO("7:30", "Agora", "Bloque 12", "M7", 3, conductor1 )	
	pasajero1=PASAJERO("Juan", "hola", "JUAN", "1232")
	servicio1.setPasajeros(pasajero1)
	for servicios in pasajero1.getServiciosPa():
		print(servicios.getHoraEncuentro())
	print(pasajero1.getServiciosPa())
	if len(SERVICIO.ServiciosDisponibles) ==0:
		print(MENSAJE.espanol.get("SinServicios"))
	else:
		cont=1
		for servicio in SERVICIO.ServiciosDisponibles:
			print(MENSAJE.espanol.get("FormatoVerServicios").format(cont,servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre()))
			cont=cont+1"""

	"""PASAJERO("Juan", "hola", "JUAN", "1232")
	for pasajeros in PASAJERO.listaPasajeros:
		print(pasajeros.getCorreo())"""

	#archivo=open("registro.txt", "a")
	#X=(b'jtorom@unal.edu.co' in b'archivo')
	
	"""archivo=open("registro.txt", "r").readlines()
	a=archivo[1].split(',')
	print(a)
	print(len(a))"""

	"""archivo=open("registro.txt", "r").readlines()
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
					VEHICULO(line[1], line[2], line[3], line[4], conductor)

	for vehiculo in VEHICULO.ListaVehiculos:
		print(vehiculo.getPlaca())"""

	"""for pasajeros in PASAJERO.listaPasajeros:
		print(pasajeros.getCorreo()+", "+pasajeros.getNombre())"""

	"""for conductores in CONDUCTOR.ListaConductores:
		for vehiculo in conductores.getVehiculos():
			print(vehiculo.getPlaca())"""

	"""archivo=open("registro.txt", "r").readlines()
	for line in archivo:
		print(line)"""
	"""a=archivo[1].split(',')
	print(a)"""
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
	

	#calificacion1 = CALIFICACION(3.0, "NO JODA CARE MONDA", conductor1, pasajero1, servicio1)
	#calificacion2 = CALIFICACION(4.0, "NO JODA CARE MONDA", conductor1, pasajero1, servicio1)
	"""persona1=PERSONA("Juan", "hola", "JUAN", "1232")
	comentario1=COMENTARIO("MUY MALO", persona1)
	print(comentario1.getFecha())"""

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
