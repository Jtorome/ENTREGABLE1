from conductor import CONDUCTOR
from servicio import SERVICIO 

class CALIFICACION:

	def __init__(self, Calificacion, Descripcion, Conductor, Pasajero, Servicio):

		'''ATRIBUTO
		self._Calificacion
		self._Descripcion
		self._Conductor
		self._Pasajero
		self._Servicio
		'''

		self.setCalificacion(Calificacion)
		self.setDescripcionCa(Descripcion)
		self.setServicio(Servicio)
		self.setConductorCa(Conductor)
		self.setPasajero(Pasajero)

	def setCalificacion(self, calificacion):
		j=1
		while(j==1):
			if(calificacion>=0 and calificacion<=5):
				self._Calificacion=float(calificacion)
				j=j+1
			else:
				print("VALOR MAL: ")

	def getCalificacion(self):
		return self._Calificacion

	def setDescripcionCa(self, descripcion):
		self._Descripcion=descripcion

	def getDescripcionCa(self):
		return self._Descripcion

	def setConductorCa(self, conductor):
		self._Conductor=conductor
		conductor.setCalificacionesCon(self)
		conductor.setAcumuladoCalificacion(conductor)

	def getConductorCa(self):
		return self._Conductor

	def setPasajero(self, pasajero):
		self._Pasajero=pasajero
		pasajero.setCalificacionPa(self)
		pasajero.setCalificacionPromedio(pasajero)

	def getPasajero(self):
		return self._Pasajero

	def setServicio(self, servicio):
		self._Servicio=servicio
		servicio.setCalificacionesSer(self)
		servicio.setCalificacionPromedioSer(servicio)

	def getServicio(self):
		return self._Servicio