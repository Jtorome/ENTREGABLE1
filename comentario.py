from persona import PERSONA
class COMENTARIO:

	listaComentarios=[]

	def __ini__(self, FechaHora, Descripcion, Persona):

		'''ATRIBUTOS
		self._FechaHora
		self._Descripcion
		self._Persona
		'''

		self.setFechaHora(fechaHora)
		self.setDescripcion(descripcion)
		self.setPersona(persona)
		COMENTARIO.listaComentarios.append(self)

	def setFechaHora(self, fechaHora):
		self._FechaHora=fechaHora
		
	def getFechaHora(self):
		return self._FechaHora

	@staticmethod
	def setDescripcion(self, descricion):
		self._Descripcion=descripcion

	@staticmethod
	def getDescripcion(self):
		return self._Descripcion

	@staticmethod
	def setPersona(self, persona):
		self._Persona=persona
		persona.setComentario(self)

	@staticmethod
	def getPersona(self):
		return self._Persona