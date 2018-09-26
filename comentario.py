import time
from persona import PERSONA
class COMENTARIO:

	listaComentarios=[]

	def __init__(self, Descripcion, Persona, Fecha=time.strftime("%d/%m/%y")):

		'''ATRIBUTOS
		self._FechaHora
		self._Descripcion
		self._Persona
		'''

		self.setDescripcion(Descripcion)
		self.setPersona(Persona)
		self._Fecha=Fecha
		COMENTARIO.listaComentarios.append(self)

	def setFecha(self, fecha):
		self._Fecha=fecha

	def getFecha(self):
		return self._Fecha

	def setDescripcion(self, descripcion):
		self._Descripcion=descripcion

	def getDescripcion(self):
		return self._Descripcion

	def setPersona(self, persona):
		self._Persona=persona
		persona.setComentarios(self)

	def getPersona(self):
		return self._Persona