from calificacion import CALIFICACION
from servicio import SERVICIO

class PASAJERO:

    listaPasajero=[]

    def __init__(self, CalificacionPromedio):

        '''ATRIBUTOS
        self._CalificacionPromedio
        self._listaServiciosPa
        self._litaCalificacionPa
        '''

        self._listaServiciosPa=[]
        self._listaCalificacionPa=[]
        self.setCalificacionPromedio(CalificacionPromedio)
        PASAJERO.listaPasajeros.append(self)

        def setCalificacionPromedio(pasajero):
            pasa=pasajero.getCalificacionPa()
            if(len(pasa)==0):
                return ("Pasajero nuevo")
            sum=0
            for cal in pasa:
                sum=sum+cal.getPuntuacion()
            self._CalificacionPromedio(sum/(len(pasa)))

        def getCalificacionPromedio(self):
            return self._CalificacionPromedio

        def setServiciosPa(self, servicios):
            self._listaServiciosPa.append(servicios)

        def getServiciosPa(self):
            return self._listaServiciosPa

        def setCalificacionPa(self, calificacion):
            self._listaCalificacionPa(calificacion)

        def getCalificacionPa(self):
            return self._listaCalificacionPa
