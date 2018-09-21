from conductor import CONDUCTOR
class SERVICIO:

    ListaServicios=[]

    def __init__(self, HoraEncuentro, SitioEncuentro, LugarInicio, LugarFin, AsientosDisponibles, CalificacionPromedioSer, Conductor):

        '''ATRIBUTOS
        self._HoraEncuentro
        self._SitioEncuentro
        self._LugarInicio
        self._LugarFin
        self._AsientosDisponibles
        self._CalificacionPromedioSer
        self._Conductor
        self._listaPasajeros
        self._listaCalificaciones
        '''
        self.setHoraEncuentro(horaEncuentro)
        self.setSitioEncuentro(sitioEncuentro)
        self.setLugarInicio(lugarInicio)
        self.setLugarFin(lugarFin)
        self.setAsientosDisponibles(asientosDisponibles)
        self.setCalificacionPromedioSer(self)
        self.setConductor(conductor)
        self._listaPasajeros=[]
        self._listaCalificacionesSer=[]
        SERVICIO.ListaServicios.append(self)

    def setHoraEncuentro(self, horaEncuentro):
        self._HoraEncuentro=horaEncuentro

    def getHoraEncuentro(self):
        return self._HoraEncuentro

    def setSitioEncuentro(self, sitioEncuentro):
        self._SitioEncuentro=sitioEncuentro

    def getSitioEncuentro(self):
        return self._SitioEncuentro

    def setLugarInicio(self, lugarInicio):
        self._LugarInicio=lugarInicio

    def getLugarInicio(self):
        return self._LugarInicio

    def setLugarFin(self, lugarFin):
        self._LugarFin=lugarFin

    def getLugarFin(self):
        return self._LugarFin

    def setAsientosDisponibles(self, asientosDisponibles):
        self._AsientosDisponibles=int(asientosDisponibles)

    def getAsientosDisponibles(self):
        return self._AsientosDisponibles

    def setCalificacionPromedioSer(self, calificaciones):
        calificacion=calificaciones.getCalificacionesSer()
        if (len(calificacion)==0):
            return "El servicio no tiene calificaciones"
        sum=0
        for ca in calificacion:
            sum=sum+(ca.getCalificacion())
        self._CalificacionPromedioSer=float(sum/(len(calificacion)))

    def getCalificacionPromedioSer(self):
        return self._CalificacionPromedioSer

    @staticmethod
    def setConductor(self, conductor):
        self._Conductor=conductor
        conductor.setServiciosCon(self)

    @staticmethod
    def getConductor(self):
        return self._Conductor

    @staticmethod
    def setPasajeros(self, pasajeros):
        self._listaPasajeros.append(pasajeros)

    @staticmethod
    def getPasajeros(self):
        return self._listaPasajeros

    def setCalificacionesSer(self, calificaciones):
        self._listaCalificacionesSer.append(calificaciones)

    def getCalificacionesSer(self):
        return self._listaCalificacionesSer