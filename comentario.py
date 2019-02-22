import time
from persona import PERSONA
from mensaje import MENSAJE
class COMENTARIO:

    listaComentarios=[]

    def __init__(self, Descripcion, Persona, Fecha):

        '''ATRIBUTOS
        self._FechaHora
        self._Descripcion
        self._Persona
        '''

        self.setDescripcion(Descripcion)
        self.setPersona(Persona)
        self.setFecha(Fecha)
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

    @staticmethod
    def VerTodosLosComentarios():
        Informacion=[]
        for comentario in COMENTARIO.listaComentarios:
            fecha=comentario.getFecha()
            Nombre=comentario.getPersona().getNombre()
            descripcion=comentario.getDescripcion()
            text=MENSAJE.men.get("FormatoComentariosAdmin").format(fecha, Nombre, descripcion)
            text=text.split(',')
            Informacion.append(','.join(text))
        return Informacion