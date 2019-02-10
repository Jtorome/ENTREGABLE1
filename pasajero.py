from persona import PERSONA
from mensaje import MENSAJE
class PASAJERO(PERSONA):

    listaPasajeros=[]

    def __init__(self, Correo, Contrasena, Nombre, Cell, CalificacionPromedio=0):

        PERSONA.__init__(self, Correo, Contrasena, Nombre, Cell)

        '''ATRIBUTOS
        self._CalificacionPromedio
        self._listaServiciosPa
        self._litaCalificacionPa
        '''

        self._listaServiciosPa=[]
        self._ViajeActual=[]
        self._listaCalificacionPa=[]
        self._ServicioNoCalificado=[]
        self._CalificacionPromedio=CalificacionPromedio
        PASAJERO.listaPasajeros.append(self)

    def setCalificacionPromedio(self):
        pasa=self.getCalificacionPa()
        if len(pasa)==0:
            return 0.0
        sum=0
        for cal in pasa:
            sum=sum+cal.getCalificacion()
        self._CalificacionPromedio=float(sum/(len(pasa)))
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        for line in archivo:
            line=line.split(',')
            if line[0]=="PASAJERO" and line[1]==self.getCorreo():
                line[5]=str(self._CalificacionPromedio)+"\n"
                contenido.append(','.join(line))
            else:
                contenido.append(','.join(line))
        with open("registro.txt", "w") as archivo:
            archivo.writelines(contenido)

    def getCalificacionPromedio(self):
        self.setCalificacionPromedio()
        return self._CalificacionPromedio

    def setServiciosPa(self, servicios):
        self._listaServiciosPa.append(servicios)

    def getServiciosPa(self):
        return self._listaServiciosPa

    def setCalificacionPa(self, calificacion):
        self._listaCalificacionPa.append(calificacion)
        self.setCalificacionPromedio()

    def getCalificacionPa(self):
        return self._listaCalificacionPa

    def setViajeActual(self, servicio):
        self._ViajeActual.append(servicio)

    def getViajeActual(self):
        return self._ViajeActual

    def setServicioNoCalificado(self, servicio):
        self._ServicioNoCalificado.append(servicio)

    def getServicioNoCalificado(self):
        return self._ServicioNoCalificado

    @staticmethod
    def BuscadorDePasajeros(correo):
        for pasajero in PASAJERO.listaPasajeros:
            if pasajero.getCorreo()==correo:
                return pasajero

    @staticmethod
    def VerMiHistorial(infousuario):
        if len(infousuario.getServiciosPa()) == 0:
            return  MENSAJE.men.get("HistorialVacio")
        historial=list()
        cont=1
        for servicio in infousuario.getServiciosPa():
            text=MENSAJE.men.get("FormatoVerMiHistorialPasajero").format(cont, servicio.getFechaSer(), servicio.getHoraEncuentro(), servicio.getConductorSer().getNombre(), servicio.getVehiculoSer().getModeloVehiculo(), servicio.getVehiculoSer().getPlaca())
            text=text.split(',')
            historial.append(','.join(text))
            cont=cont+1
        return historial

    @staticmethod
    def MejorCalificadosPasajero():
        lista=[]
        calificaciones=[]
        Informacion=[]
        for pasajero in PASAJERO.listaPasajeros:
            lista.append(pasajero.getNombre())
            calificaciones.append(pasajero.getCalificacionPromedio())
        for i in range(1, 4):
            if len(calificaciones) == 0:
                return Informacion
            Max=max(calificaciones)
            posicion=calificaciones.index(Max)
            text=MENSAJE.men.get("FormatoMejorCalificadoPasajero").format(i, lista[posicion], Max)
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            calificaciones.remove(Max)
        return Informacion