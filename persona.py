from mensaje import MENSAJE
class PERSONA():

	listaPersonas=[]

	def __init__(self, Correo, Contrasena, Nombre, Cell):

		'''ATRIBUTOS
		self._Correo
		self._Contrasena
		self._Nombre
		self._Cell
		self._listaComentarios
		'''

		self._listaComentarios=[]
		self.setCorreo(Correo)
		self.setContrasena(Contrasena)
		self.setNombre(Nombre)
		self.setCell(Cell)
		PERSONA.listaPersonas.append(self)

	def setCorreo(self, correo):
		self._Correo=correo

	def getCorreo(self):
		return self._Correo

	def setNombre(self, nombre):
		self._Nombre=nombre

	def getNombre(self):
		return self._Nombre

	def setCell(self, cell):
		self._Cell= cell

	def getCell(self):
		return self._Cell

	def setContrasena(self, contrasena):
		self._Contrasena= contrasena

	def getContrasena(self):
		return self.Contrasena

	def setComentarios(self, comentarios):
		self._listaComentarios.append(comentarios)

	def getComentarios(self):
		return self._listaComentarios

	@staticmethod
	def VerificarRegistro(palabra, correo):
		archivo=open("registro.txt", "r")
		X=True
		while X:
			pal=0
			noesta=0
			for line in archivo:
				line=line.split(',')
				if palabra==line[0]:
					pal=pal+1
					if correo == line[1]:
						print(MENSAJE.men.get("CorreoInvalido"))
						X=False
					else:
						noesta=noesta+1
			if noesta==pal:
				return False
				X=False
			else:
				return True

	@staticmethod
	def VerificarCorreo(correo, contrasena):
		archivo=open("registro.txt", "r").readlines()
		linea=0
		corre=0
		contra=0
		while True:
			for line in archivo:
				line=line.split(',')
				if correo==line[1]:
					corre=corre+1
					if contrasena==line[2]:
						contra=contra+1
						if(contra==1):
							line1=linea
						if(contra>1):
							line2=linea
				linea=linea+1
			if corre==1 and contra==0:
				print(MENSAJE.men.get("ContrasenaInvalida"))
				return True
				break
			if corre==1 and contra==1:
				line1=archivo[line1].split(',')
				return line1
				break
			if corre==0:
				print(MENSAJE.men.get("CorreoInexistente"))
				return True
				break
			if corre==2 and contra ==2:
				line1=archivo[line1].split(',')
				line2=archivo[line2].split(',')
				print(MENSAJE.men.get("MenuVerificarCorreo"))
				opcion=input(MENSAJE.men.get("Opcion"))
				if opcion=="1":
					if "PASAJERO" ==line1[0]:
						return line1
						break
					if "PASAJERO"==line2[0]:
						return line2
						break
				if opcion=="2":
					if "CONDUCTOR"==line1[0]:
						return line1
						break
					if "CONDUCTOR"==line2[0]:
						return line2
						break
				if opcion=="3":
					return "salir"
					break