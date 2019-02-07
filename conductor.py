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
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        for line in archivo:
            line=line.split(',')
            if "CONDUCTOR"==line[0] and line[1]==self.getCorreo():
                line[5]=str(self._NumeroServicios)
                contenido.append(','.join(line))
            else:
                contenido.append(','.join(line))
        with open("registro.txt","w") as archivo:
            archivo.writelines(contenido)

    def getNumeroServicios(self):
        return self._NumeroServicios

    def setAcumuladoCalificacion(self):
        cond=self.getServiciosCon()
        sum=0
        for cal in cond:
            sum=float(sum+int(cal.getCalificacionPromedioSer()))
        self._AcumuladoCalificacion=float(sum)
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        for line in archivo:
            line=line.split(',')
            if "CONDUCTOR"==line[0] and line[1]==self.getCorreo():
                line[6]=str(self._AcumuladoCalificacion)+"\n"
                contenido.append(','.join(line))
            else:
                contenido.append(','.join(line))
        with open("registro.txt","w") as archivo:
            archivo.writelines(contenido)

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
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        for vehiculo in Conductor.getVehiculos():
            if vehiculo.getActivo().split()[0] == "si":
                vehiculo.setActivo("no")
                for line in archivo:
                    if "VEHICULO" == line.split(',')[0] and vehiculo.getPlaca() == line.split(',')[1] and "si" == line.split(',')[7].split()[0]:
                        line=line.replace(",si\n",",no\n").split(',')
                        contenido.append(','.join(line))
                    else:
                        line=line.split(',')
                        contenido.append(','.join(line))
        with open('registro.txt', 'w') as archivo:
            archivo.writelines(contenido)
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
        archivo=open("registro.txt", "r").readlines()
        contenido=list()
        for vehiculo in Conductor.getVehiculos():
            vehiculo2=Conductor.getVehiculos()[num-1]
            if vehiculo.getActivo().split()[0] == "si":
                vehiculo.setActivo("no")
                for line in archivo:
                    if "VEHICULO" == line.split(',')[0] and vehiculo.getPlaca() == line.split(',')[1] and "si" == line.split(',')[7].split()[0]:
                        line=line.replace(",si\n", ",no\n").split(',')
                        contenido.append(','.join(line))
                    elif "VEHICULO" == line.split(',')[0] and vehiculo2.getPlaca() == line.split(',')[1] and "no" == line.split(',')[7].split()[0]:
                        line=line.replace(",no\n", ",si\n").split(',')
                        contenido.append(','.join(line))
                    else:
                        line=line.split(',')
                        contenido.append(','.join(line))
        vehiculo2.setActivo("si")
        with open('registro.txt', 'w') as archivo:
            archivo.writelines(contenido)
        return

    @staticmethod
    def MejorCalificadosConductor():
        calificaciones=[]
        for conductor in CONDUCTOR.ListaConductores:
            if len(calificaciones) == 0:
                calificaciones.append(conductor)
            elif len(calificaciones) == 1:
                if float(calificaciones[0].getAcumuladoCalificacion()) >= conductor.getAcumuladoCalificacion():
                    calificaciones.append(conductor)
                elif float(calificaciones[0].getAcumuladoCalificacion()) < conductor.getAcumuladoCalificacion():
                    calificaciones.insert(0, conductor)
            elif len(calificaciones) == 2:
                if float(calificaciones[0].getAcumuladoCalificacion()) >= conductor.getAcumuladoCalificacion():
                    if float(calificaciones[1].getAcumuladoCalificacion()) >= conductor.getAcumuladoCalificacion():
                        calificaciones.append(conductor)
                    elif float(calificaciones[1].getAcumuladoCalificacion()) < conductor.getAcumuladoCalificacion():
                        calificaciones.insert(1, conductor)
                elif float(calificaciones[0].getAcumuladoCalificacion()) < conductor.getAcumuladoCalificacion():
                    calificaciones.insert(0, conductor)
            elif len(calificaciones) == 3:
                if float(calificaciones[0].getAcumuladoCalificacion()) >= float(conductor.getAcumuladoCalificacion()):
                    if float(calificaciones[1].getAcumuladoCalificacion()) >= float(conductor.getAcumuladoCalificacion()):
                        if float(calificaciones[2].getAcumuladoCalificacion()) < float(conductor.getAcumuladoCalificacion()):
                            calificaciones.insert(2, conductor)
                            calificaciones.remove(calificaciones[3])
                    elif float(calificaciones[1].getAcumuladoCalificacion()) < conductor.getAcumuladoCalificacion():
                        calificaciones.insert(1, conductor)
                        calificaciones.remove(calificaciones[3])
                elif float(calificaciones[0].getAcumuladoCalificacion()) < conductor.getAcumuladoCalificacion():
                    calificaciones.insert(0, conductor)
                    calificaciones.remove(calificaciones[3])
        listaCalificaciones=list()
        cont=1
        for pas in calificaciones:
            text=MENSAJE.men.get("FormatoMejorCalificadoConductor").format(cont, pas.getNombre(), pas.getAcumuladoCalificacion())
            text=text.split(',')
            listaCalificaciones.append(','.join(text))
            cont=cont+1
        return listaCalificaciones