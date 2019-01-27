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
        return self._Contrasena

    def setComentarios(self, comentarios):
        self._listaComentarios.append(comentarios)

    def getComentarios(self):
        return self._listaComentarios

    @staticmethod
    def VerificarRegistro(palabra, correo):
        archivo=open("registro.txt", "r")
        for line in archivo:
            line=line.split(',')
            if palabra==line[0]:
                if correo == line[1]:
                    return True
        return False

    @staticmethod
    def VerificarCorreo(correo, contrasena):
        cont=0  
        if len(PERSONA.listaPersonas)==0:
            return "Invalido"
        else:
            for info in PERSONA.listaPersonas:              
                if correo==info.getCorreo():
                    if contrasena==info.getContrasena():
                        if cont == 0:
                            info1=info
                            cont=cont+1
                        else:
                            info2=info
                            cont=cont+1
            if cont == 0:       
                return "Invalido"
        if cont == 1:
            return info1
        if cont == 2:
            return [info1, info2]

    @staticmethod
    def BuscarPersona(correo):
        for persona in PERSONA.listaPersonas:
            if persona.getCorreo()==correo:
                return persona