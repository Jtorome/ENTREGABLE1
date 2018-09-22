from calificacion import CALIFICACION
from servicio import SERVICIO
class PASAJERO:

    listaPasajeros=[]

    def __init__(self, CalificacionPromedio=0):

        '''ATRIBUTOS
        self._CalificacionPromedio
        self._listaServiciosPa
        self._litaCalificacionPa
        '''

        self._listaServiciosPa=[]
        self._listaCalificacionPa=[]
        self._CalificacionPromedio=CalificacionPromedio
        PASAJERO.listaPasajeros.append(self)

    def setCalificacionPromedio(self, pasajero):
        pasa=pasajero.getCalificacionPa()
        if(len(pasa)==0):
            return ("Pasajero nuevo")
        sum=0
        for cal in pasa:
            sum=sum+cal.getCalificacion()
        self._CalificacionPromedio=(sum/(len(pasa)))

    def getCalificacionPromedio(self):
        return self._CalificacionPromedio

    def setServiciosPa(self, servicios):
        self._listaServiciosPa.append(servicios)

    def getServiciosPa(self):
        return self._listaServiciosPa

    def setCalificacionPa(self, calificacion):
        self._listaCalificacionPa.append(calificacion)

    def getCalificacionPa(self):
        return self._listaCalificacionPa
