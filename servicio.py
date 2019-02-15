from conductor import CONDUCTOR
from mensaje import MENSAJE
import time
class SERVICIO:

    ListaServicios=[]
    ServiciosDisponibles=[]

    def __init__(self, HoraEncuentro, SitioEncuentro, LugarInicio, LugarFin, AsientosDisponibles, Conductor, Vehiculo, FechaSer, CalificacionPromedioSer=0):

        '''ATRIBUTOS
        self._HoraEncuentro
        self._SitioEncuentro
        self._LugarInicio
        self._LugarFin
        self._AsientosDisponibles
        self._CalificacionPromedioSer
        self._Conductor
        self._Vehiculo
        self._listaPasajeros
        self._listaCalificaciones
        '''
        self.setHoraEncuentro(HoraEncuentro)
        self.setSitioEncuentro(SitioEncuentro)
        self.setLugarInicio(LugarInicio)
        self.setLugarFin(LugarFin)
        self.setAsientosDisponibles(AsientosDisponibles)
        self.setConductorSer(Conductor)
        self.setVehiculoSer(Vehiculo)
        self.setFechaSer(FechaSer)
        self._CalificacionPromedioSer=CalificacionPromedioSer
        self._listaPasajeros=[]
        self._PasajeroxAsiento={}
        self._listaCalificacionesSer=[]
        SERVICIO.ServiciosDisponibles.append(self)
        SERVICIO.ListaServicios.append(self)


    def setHoraEncuentro(self, horaencuentro):
        self._HoraEncuentro=horaencuentro

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

    def setCalificacionPromedioSer(self):
        calificacion=self.getCalificacionesSer()
        if len(calificacion)==0:
            return
        sum=0
        for ca in calificacion:
            sum=sum+(ca.getCalificacion())
        self._CalificacionPromedioSer=float(sum/(len(calificacion)))

    def getCalificacionPromedioSer(self):
        self.setCalificacionPromedioSer()
        return self._CalificacionPromedioSer

    def setConductorSer(self, Conductor):
        self._Conductor=Conductor
        Conductor.setServiciosCon(self)
        Conductor.setServicioActual(self)
        CONDUCTOR.setNumeroServicios(Conductor)

    def getConductorSer(self):
        return self._Conductor

    def setVehiculoSer(self, vehiculo):
        self._Vehiculo=vehiculo

    def getVehiculoSer(self):
        return self._Vehiculo

    def setPasajeros(self, pasajeros, razon):
        self._listaPasajeros.append(pasajeros)
        pasajeros.setServiciosPa(self)
        pasajeros.setViajeActual(self)
        self._AsientosDisponibles=self._AsientosDisponibles-int(razon[0])

    def getPasajeros(self):
        return self._listaPasajeros

    def setPasajeroxAsiento(self, pasajero, razon):
        self._PasajeroxAsiento[pasajero]=razon

    def getPasajeroxAsiento(self):
        return self._PasajeroxAsiento

    def setCalificacionesSer(self, calificaciones):
        self._listaCalificacionesSer.append(calificaciones)
        self.setCalificacionPromedioSer()

    def getCalificacionesSer(self):
        return self._listaCalificacionesSer

    def setFechaSer(self, fechaser):
        self._FechaSer=fechaser

    def getFechaSer(self):
        return self._FechaSer

    def getInformacionSerCompleta(self):
        HE=self.getHoraEncuentro()
        SE=self.getSitioEncuentro()
        LI=self.getLugarInicio()
        LF=self.getLugarFin()
        AD=str(self.getAsientosDisponibles())
        CON=(self.getConductorSer()).getCorreo()
        PL=(self.getVehiculoSer()).getPlaca()
        FS=self.getFechaSer()
        CP=str(self.getCalificacionPromedioSer())
        if len(self.getPasajeros())==0:
            return "SERVICIO,"+HE+","+SE+","+LI+","+LF+","+AD+","+CON+","+PL+","+FS+","+CP
        elif len(self.getPasajeros())==1:
            return "SERVICIO,"+HE+","+SE+","+LI+","+LF+","+AD+","+CON+","+PL+","+FS+","+CP+","+(self.getPasajeros()[0]).getCorreo()
        elif len(self.getPasajeros())==2:
            return "SERVICIO,"+HE+","+SE+","+LI+","+LF+","+AD+","+CON+","+PL+","+FS+","+CP+","+(self.getPasajeros()[0]).getCorreo()+","+(self.getPasajeros()[1]).getCorreo()
        elif len(self.getPasajeros())==3:
            return "SERVICIO,"+HE+","+SE+","+LI+","+LF+","+AD+","+CON+","+PL+","+FS+","+CP+","+(self.getPasajeros()[0]).getCorreo()+","+(self.getPasajeros()[1]).getCorreo()+","+(self.getPasajeros()[2]).getCorreo()
        elif len(self.getPasajeros())==4:
            return "SERVICIO,"+HE+","+SE+","+LI+","+LF+","+AD+","+CON+","+PL+","+FS+","+CP+","+(self.getPasajeros()[0]).getCorreo()+","+(self.getPasajeros()[1]).getCorreo()+","+(self.getPasajeros()[2]).getCorreo()+","+(self.getPasajeros()[3]).getCorreo()

    @staticmethod
    def ActualizarSerDis():
        actual=time.strftime("%y/%m/%d")
        Hora=time.strftime("%H:%M")
        for servicio in SERVICIO.ServiciosDisponibles:
            FechaSer=servicio.getFechaSer()
            if FechaSer < actual:
                SERVICIO.ServiciosDisponibles.remove(servicio)
                (servicio.getConductorSer()).getServicioActual().remove(servicio)
                for pasajero in servicio.getPasajeros():
                    pasajero.getViajeActual().remove(servicio)
                    pasajero.setServicioNoCalificado(servicio)
                    servicio.getConductorSer().setPasajeroNoCalificado(pasajero)
            elif FechaSer == actual:
                if servicio.getHoraEncuentro() < Hora:
                    SERVICIO.ServiciosDisponibles.remove(servicio)
                    (servicio.getConductorSer()).getServicioActual().remove(servicio)
                    for pasajero in servicio.getPasajeros():
                        pasajero.getViajeActual().remove(servicio)
                        pasajero.setServicioNoCalificado(servicio)
                        servicio.getConductorSer().setPasajeroNoCalificado(pasajero)

    @staticmethod
    def ServicioTomado(infousuario, servicio, razon):
        cont=len(servicio.getPasajeros())
        for i in range(cont):
            if infousuario.getCorreo()==servicio.getPasajeros()[i].getCorreo():
                return MENSAJE.men.get("NoPuedeTomarSer")
        if infousuario.getCorreo() == servicio.getConductorSer().getCorreo():
            return MENSAJE.men.get("NoPuedeTomarSer")
        else:
            servicio.setPasajeros(infousuario, razon)
            servicio.setPasajeroxAsiento(infousuario, razon)
            return MENSAJE.men.get("RegistradoEnSer").format(servicio.getHoraEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin())

    @staticmethod
    def EliminarServicio(servicio):
        SERVICIO.ServiciosDisponibles.remove(servicio)
        (servicio.getConductorSer()).getServicioActual().remove(servicio)
        (servicio.getConductorSer()).getServiciosCon().remove(servicio)
        for pasajero in servicio.getPasajeros():
            pasajero.getViajeActual().remove(servicio)
        return MENSAJE.men.get("ServicioEliminado")

    @staticmethod
    def EliminarPasajero(infousuario, servicio):
        asientos=int(servicio.getPasajeroxAsiento()[infousuario][0])
        del ServicioActual.getPasajeroxAsiento()[infousuario]
        servicio.setAsientosDisponibles(int(servicio.getAsientosDisponibles()+asientos))
        servicio.getPasajeros().remove(infousuario)
        infousuario.getViajeActual().remove(servicio)
        infousuario.getServiciosPa().remove(servicio)
        return MENSAJE.men.get("ServicioCancelado")

    @staticmethod
    def BuscadorDeServicio(HoraEncuentro, Correo, Fecha):
        for servicio in SERVICIO.ListaServicios:
            if servicio.getHoraEncuentro()==HoraEncuentro and servicio.getConductorSer().getCorreo()==Correo and servicio.getFechaSer()==Fecha:
                return servicio

    @staticmethod
    def RutaFavorita():
        lista=[]
        cont=[]
        Informacion=[]
        for servicio in SERVICIO.ListaServicios:
            text=servicio.getLugarInicio()+","+servicio.getLugarFin()
            if text in lista:
                posicion=lista.index(text)
                cont[posicion]=cont[posicion]+1
            else:
                lista.append(text)
                cont.append(0)
        for i in range(1, 4):
            if len(cont) == 0:
                return Informacion
            Max=max(cont)
            posicion=cont.index(Max)
            LI=lista[posicion].split(',')[0]
            LF=lista[posicion].split(',')[1]
            text=MENSAJE.men.get("FormatoRutaFavorita").format(i, LI, LF)
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            cont.remove(Max)
        return Informacion

    @staticmethod
    def VehiculoFavorito():
        lista=[]
        cont=[]
        Informacion=[]
        for servicio in SERVICIO.ListaServicios:
            text=servicio.getVehiculoSer().getModeloVehiculo()
            if text in lista:
                posicion=lista.index(text)
                cont[posicion]=cont[posicion]+1
            else:
                lista.append(text)
                cont.append(0)
        for i in range(1, 4):
            if len(cont) == 0:
                return Informacion
            Max=max(cont)
            posicion=cont.index(Max)
            text=MENSAJE.men.get("FormatoVehiculoFavorito").format(i, lista[posicion])
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            cont.remove(Max)
        return Informacion

    @staticmethod
    def HoraMasConcurrida():
        lista=[]
        cont=[]
        Informacion=[]
        for servicio in SERVICIO.ListaServicios:
            text=servicio.getHoraEncuentro()
            if text in lista:
                posicion=lista.index(text)
                cont[posicion]=cont[posicion]+1
            else:
                lista.append(text)
                cont.append(0)
        for i in range(1, 4):
            if len(cont) == 0:
                return Informacion
            Max=max(cont)
            posicion=cont.index(Max)
            text=MENSAJE.men.get("FormatoHoraMasConcurrida").format(i, lista[posicion])
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            cont.remove(Max)
        return Informacion

    @staticmethod
    def EliminarPasajeroDeServicio(ServicioActual, num):
        asientos=int(ServicioActual.getPasajeroxAsiento()[ServicioActual.getPasajeros()[num-1]][0])
        del ServicioActual.getPasajeroxAsiento()[ServicioActual.getPasajeros()[num-1]]
        ServicioActual.getPasajeros().remove(ServicioActual.getPasajeros()[num-1])
        ServicioActual.setAsientosDisponibles(ServicioActual.getAsientosDisponibles()+asientos)
        return MENSAJE.men.get("PasajeroEliminado")