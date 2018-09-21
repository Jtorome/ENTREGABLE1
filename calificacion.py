from conductor import CONDUCTOR
from servicio import SERVICIO
class CALIFICACION:

	def __init__(self, Calificacion, Descripcion, Conductor= None, Pasajero=None, Servicio):

		'''ATRIBUTO
		self._Calificacion
		self._Descripcion
		self._Conductor
		self._Pasajero
		self._Servicio
		'''

		self.setCalificacion(calificacion)
		self.setDescripcion(descripcion)
		self.setConductor(conductor)
		self.setPasajero(pasajero)
		self.setServicio(servicio)

	def setCalificacion(self, calificacion):
		self._Calificacion=int(calificacion)

	def getCalificacion(self):
		return self._Calificacion

	@staticmethod
	def setDescripcion(self, descripcion):
		self._Descripcion=descripcion

	@staticmethod
	def getDescripcion(self):
		return self._Descripcion

	@staticmethod
	def setConductor(self, conductor):
		self._Conductor=conductor
		conductor.setCalificacionesCon(self)
		conductor.setAcumuladoCalificacion(self)

	@staticmethod
	def getConductor(self):
		return self._Conductor

	@staticmethod
	def setPasajero(self, pasajero):
		self._Pasajero(pasajero)
		pasajero.setCalificacionesPa(self)
		pasajero.setCalificacionPromedio(self)

	@staticmethod
	def getPasajero(self):
		return self._Pasajero

	@staticmethod
	def setServicio(self, servicio):
		self._Servicio=servicio
		servicio.setCalificacionesSer(self)
		servicio.setCalificacionPromedioSer(self)

	@staticmethod
	def getServicio(self):
		return self._Servicio