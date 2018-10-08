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