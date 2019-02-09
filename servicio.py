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
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        for line in archivo:
            line=line.split(',')
            if line[1]==self.getHoraEncuentro() and line[6]==self.getConductorSer().getCorreo() and line[7]==self.getFechaSer():
                if len(line)==9:
                    line[8]=str(self._CalificacionPromedioSer)+"\n"
                    contenido.append(','.join(line))
                else:
                    line[8]=str(self._CalificacionPromedioSer)
                    contenido.append(','.join(line))
            else:
                contenido.append(','.join(line))
        with open("registro.txt","w") as archivo:
            archivo.writelines(contenido)

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

    def setPasajeros(self, pasajeros):
        self._listaPasajeros.append(pasajeros)
        pasajeros.setServiciosPa(self)
        pasajeros.setViajeActual(self)
        self._AsientosDisponibles=self._AsientosDisponibles-1

    def getPasajeros(self):
        return self._listaPasajeros

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
    def ServicioTomado(infousuario, servicio):
        cont=len(servicio.getPasajeros())
        for i in range(cont):
            if infousuario.getCorreo()==servicio.getPasajeros()[i].getCorreo():
                return MENSAJE.men.get("NoPuedeTomarSer")
        if infousuario.getCorreo() == servicio.getConductorSer().getCorreo():
            return MENSAJE.men.get("NoPuedeTomarSer")
        else:
            archivo=open("registro.txt", "r").readlines()
            contenido=list()
            text=servicio.getInformacionSerCompleta().split(',')
            for line in archivo:
                if line.split(',')[0]=="SERVICIO":
                    if line.split(',')[1]==text[1] and line.split(',')[6]==text[6] and line.split(',')[7]==text[7]:
                        line=(line.split()[0])+","+infousuario.getCorreo()+"\n"
                        contenido.append(','.join(line.split(',')))
                    else:
                        contenido.append(','.join(line.split(',')))
                else:
                    contenido.append(','.join(line.split(',')))
            with open('registro.txt', 'w') as archivo:
                archivo.writelines(contenido)
            servicio.setPasajeros(infousuario)
            return MENSAJE.men.get("RegistradoEnSer").format(servicio.getHoraEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin())

    @staticmethod
    def EliminarServicio(servicio):
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        text=servicio.getInformacionSerCompleta().split(',')
        for line in archivo:
            linea=line.split(',')
            if linea[0]=="SERVICIO":
                if linea[1]!=text[1] and linea[6]!=text[6] and linea[7]!=text[7]:
                    line=line.split(',')
                    contenido.append(','.join(line))
            else:
                contenido.append(','.join(line.split(',')))
        with open('registro.txt', 'w') as archivo:
            archivo.writelines(contenido)
        SERVICIO.ServiciosDisponibles.remove(servicio)
        (servicio.getConductorSer()).getServicioActual().remove(servicio)
        for pasajero in servicio.getPasajeros():
            pasajero.getViajeActual().remove(servicio)
        return MENSAJE.men.get("ServicioEliminado")

    @staticmethod
    def EliminarPasajero(infousuario, servicio):
        servicio.setAsientosDisponibles(int(servicio.getAsientosDisponibles()+1))
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        servicio.getPasajeros().remove(infousuario)
        infousuario.getViajeActual().remove(servicio)
        infousuario.getServiciosPa().remove(servicio)
        text=servicio.getInformacionSerCompleta().split(',')
        for line in archivo:
            linea=line.split(',')
            if "SERVICIO"==linea[0]:
                if linea[1]==text[1] and linea[6]==text[6] and linea[7]==text[7]:
                    contenido.append(','.join(text)+"\n")
                else:
                    contenido.append(','.join(linea))
            else:
                contenido.append(','.join(linea))
        with open('registro.txt', 'w') as archivo:
            archivo.writelines(contenido)
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
        contador=1
        for i in range(1, 3):
            Max=max(cont)
            posicion=cont.index(Max)
            LI=lista[posicion].split(',')[0]
            LF=lista[posicion].split(',')[1]
            text=MENSAJE.men.get("FormatoRutaFavorita").format(contador, LI, LF)
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            cont.remove(Max)
            contador=contador+1
        return Informacion


