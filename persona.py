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