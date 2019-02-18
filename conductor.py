from vehiculo import VEHICULO
from persona import PERSONA
from mensaje import MENSAJE
class CONDUCTOR(PERSONA):

    ListaConductores=[]

    def __init__(self, Correo, Contrasena, Nombre, Cell, NumeroServicios=0, AcumuladoCalificacion=0):

        PERSONA.__init__(self, Correo, Contrasena, Nombre, Cell)

        '''ATRIBUTOS
        self._NumeroServicios
        self._AcumuladoCalificacion
        self._listaVehiculos
        self._listaServiciosCon
        self._listaCalificacionesCon
        '''

        self._listaVehiculos = []
        self._listaServiciosCon = []
        self._ServicioActual=[]
        self._PasajeroNoCalificado=[]
        self._NumeroServicios=NumeroServicios
        self._AcumuladoCalificacion=AcumuladoCalificacion
        CONDUCTOR.ListaConductores.append(self)

    def setNumeroServicios(self):
        ser=self.getServiciosCon()
        self._NumeroServicios=len(ser)

    def getNumeroServicios(self):
        self.setNumeroServicios()
        return self._NumeroServicios

    def setAcumuladoCalificacion(self):
        cond=self.getServiciosCon()
        sum=0
        for cal in cond:
            sum=float(sum+int(cal.getCalificacionPromedioSer()))
        self._AcumuladoCalificacion=float(sum)

    def getAcumuladoCalificacion(self):
        self.setAcumuladoCalificacion()
        return self._AcumuladoCalificacion

    def setVehiculos(self, vehiculos):
        self._listaVehiculos.append(vehiculos)

    def getVehiculos(self):
        return self._listaVehiculos

    def setServiciosCon(self, servicios):
        self._listaServiciosCon.append(servicios)

    def getServiciosCon(self):
        return self._listaServiciosCon

    def setServicioActual(self, servicio):
        self._ServicioActual.append(servicio)

    def getServicioActual(self):
        return self._ServicioActual

    def setPasajeroNoCalificado(self, pasajero):
        self._PasajeroNoCalificado.append(pasajero)

    def getPasajeroNoCalificado(self):
        return self._PasajeroNoCalificado

    @staticmethod
    def VerVehiculos(Conductor):
        vehiculos=list()
        con=1
        for vehiculo in Conductor.getVehiculos():
            text=str(con)+". "+vehiculo.getPlaca()+", "+vehiculo.getColor()+", "+vehiculo.getTipoVehiculo()+", "+vehiculo.getModeloVehiculo()+", Activo: "+vehiculo.getActivo()
            text=text.split(',')
            vehiculos.append(','.join(text))
            con=con+1
        return vehiculos

    @staticmethod
    def VerificarActivacion(Conductor):
        for vehiculo in Conductor.getVehiculos():
            if vehiculo.getActivo().split()[0] == "si":
                vehiculo.setActivo("no")
        return False

    @staticmethod
    def VehiculoActivado(infousuario):
        for vehiculo in infousuario.getVehiculos():
            if vehiculo.getActivo()=="si":
                return vehiculo

    @staticmethod
    def BuscadorDeConductor(correo):
        for conductor in CONDUCTOR.ListaConductores:
            if conductor.getCorreo()==correo:
                return conductor

    @staticmethod
    def CambioVehiActi(Conductor, num):
        for vehiculo in Conductor.getVehiculos():
            if vehiculo.getActivo().split()[0] == "si":
                vehiculo.setActivo("no")
        vehiculo2=Conductor.getVehiculos()[num-1]
        vehiculo2.setActivo("si")
        return

    @staticmethod
    def MejorCalificadosConductor():
        lista=[]
        calificaciones=[]
        Informacion=[]
        for conductor in CONDUCTOR.ListaConductores:
            lista.append(conductor.getNombre())
            calificaciones.append(conductor.getAcumuladoCalificacion())
        for i in range(1, 4):
            if len(calificaciones) == 0:
                return Informacion
            Max=max(calificaciones)
            posicion=calificaciones.index(Max)
            text=MENSAJE.men.get("FormatoMejorCalificadoConductor").format(i, lista[posicion], Max)
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            calificaciones.remove(Max)
        return Informacion

    @staticmethod
    def ConductorConMasViajes():
        lista=[]
        cont=[]
        Informacion=[]
        for conductor in CONDUCTOR.ListaConductores:
            cont.append(int(conductor.getNumeroServicios()))
            lista.append(conductor.getNombre())
        for i in range(1, 4):
            if len(cont) == 0:
                return Informacion
            Max=max(cont)
            posicion=cont.index(Max)
            text=MENSAJE.men.get("FormatoConductorMasViajes").format(i, lista[posicion], Max)
            text=text.split(',')
            Informacion.append(','.join(text))
            lista.remove(lista[posicion])
            cont.remove(Max)
        return Informacion