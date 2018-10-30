from vehiculo import VEHICULO
from persona import PERSONA
class CONDUCTOR(PERSONA):

	ListaConductores=[]

	def __init__(self, Correo, Contrasena, Nombre, Cell, NumeroServicios=0, AcumuladoCalificacion=0):

		PERSONA.__init__(self, Correo, Contrasena, Nombre, Cell)

		'''ATRIBUTOS
		self._NumeroServicios
		self._AcumuladoCalificacion
		self._listaVehiculos
		self._listaServiciosCon
		self._listaCalificacionesCon
		'''

		self._listaVehiculos = []
		self._listaServiciosCon = []
		self._listaCalificacionesCon=[]
		self._NumeroServicios=NumeroServicios
		self._AcumuladoCalificacion=AcumuladoCalificacion
		CONDUCTOR.ListaConductores.append(self)

	def setNumeroServicios(self):
		ser=self.getServiciosCon()
		self._NumeroServicios=len(ser)

	def getNumeroServicios(self):
		return self._NumeroServicios

	def setAcumuladoCalificacion(self, conductor):
		cond=conductor.getServiciosCon()
		if len(cond)==0:
			return ("Es conductor nuevo")
		sum=0
		for cal in cond:
			sum=float(sum+(cal.getCalificacionPromedioSer()))
		self._AcumuladoCalificacion=float(sum)

	def getAcumuladoCalificacion(self):
		return self._AcumuladoCalificacion

	def setVehiculos(self, vehiculos):
		self._listaVehiculos.append(vehiculos)

	def getVehiculos(self):
		return self._listaVehiculos

	def setServiciosCon(self, servicios):
		self._listaServiciosCon.append(servicios)

	def getServiciosCon(self):
		return self._listaServiciosCon

	def setCalificacionesCon(self, calificaciones):
		self._listaCalificacionesCon.append(calificaciones)

	def getCalificacionesCon(self):
		return self._listaCalificacionesCon

	@staticmethod
	def VerVehiculos(Conductor):
		vehiculos=list()
		cont="1"
		con=1
		for vehiculo in Conductor.getVehiculos():
			text=str(cont)+". "+vehiculo.getPlaca()+", "+vehiculo.getColor()+", "+vehiculo.getTipoVehiculo()+", Activo: "+vehiculo.getActivo()
			text=text.split(',')
			vehiculos.append(','.join(text))
			con=con+1
			cont=con
		return vehiculos

	@staticmethod
	def VerificarActivacion(Conductor):
		archivo=open("registro.txt", "r").readlines()
		contenido=list()
		for vehiculo in Conductor.getVehiculos():
			if vehiculo.getActivo().split()[0] == "si":
				vehiculo.setActivo("no")
				for line in archivo:
					if "VEHICULO" == line.split(',')[0] and vehiculo.getPlaca() == line.split(',')[1] and "si" == line.split(',')[6].split()[0]:
						line=line.replace(",si\n",",no\n").split(',')
						contenido.append(','.join(line))
		with open('registro.txt', 'w') as archivo:
			archivo.writelines(contenido)
		return False