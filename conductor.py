from vehiculo import VEHICULO

class CONDUCTOR:

    ListaConductores=[]

    def __init__(self, NumeroServicios=0, AcumuladoCalificacion=0):

        '''ATRIBUTOS
        self._NumeroServicios
        self._AcumuladoCalificacion
        self._listaVehiculos
        self._listaServiciosCon
        self._listaCalificacionesCon
        '''

        self._listaVehiculos = []
        self._listaServiciosCon = []
        self._listaCalificacionesCon=[]
        self.setNumeroServicios()
        self.setAcumuladoCalificacion()
        CONDUCTOR.ListaConductores.append(self)

        def setNumeroServicios(self):
            self._NumeroServicios=NumeroServicios+1

        def getNumeroServicios(self):
            return self._NumeroServicios

        def setAcumuladoCalificacion(self, conductor):
            cond=conductor.getCalificacionesCon()
            if len(cond)==0:
                return ("Es conductor nuevo")
            sum=0
            for cal in cond:
                sum=sum+(cal.getCalificacionPromedioSer)
                self._AcumuladoCalificacion=float(sum)

            def getAcumuladoCalificacion(self):
                return self._AcumuladoCalificacion

            def setVehiculos(self, vehiculos):
                self._listaVehiculos.append(vehiculos)

            def getVehiculos(self):
                return self._listaVehiculos

            def setServiciosCon(self, servicios):
                self._listaServiciosCon.appen(servicios)

            def getServiciosCon(self):
                return self._listaServiciosCon

            def setCalificacionesCon(self, calificaciones):
                self._listaCalificacionesCon(calificaciones)

            def getCalificacionesCon(self):
                return self._listaCalificacionesCon