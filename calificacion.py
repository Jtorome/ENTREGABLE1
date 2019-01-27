from conductor import CONDUCTOR
from servicio import SERVICIO
from pasajero import PASAJERO

class CALIFICACION:

    def __init__(self, Calificacion, Descripcion, Pasajero, Servicio=None):

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
        self.setPasajero(Pasajero)

    def setCalificacion(self, calificacion):
        self._Calificacion=float(calificacion)

    def getCalificacion(self):
        return self._Calificacion

    def setDescripcionCa(self, descripcion):
        self._Descripcion=descripcion

    def getDescripcionCa(self):
        return self._Descripcion

    def setPasajero(self, pasajero):
        self._Pasajero=pasajero
        if pasajero!=None and type(pasajero)!=str:
            pasajero.setCalificacionPa(self)

    def getPasajero(self):
        return self._Pasajero

    def setServicio(self, servicio):
        self._Servicio=servicio
        if servicio!=None and type(servicio)!=str:
            servicio.setCalificacionesSer(self)

    def getServicio(self):
        return self._Servicio