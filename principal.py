import os
from persona import PERSONA
from conductor import CONDUCTOR
from pasajero import PASAJERO
from vehiculo import VEHICULO
from servicio import SERVICIO
from comentario import COMENTARIO
from calificacion import CALIFICACION
from mensaje import MENSAJE
from ficticio import FICTICIO
from datetime import datetime
from datetime import date
from datetime import timedelta
import time

class PRINCIPAL:

    def __init__(self):

        self.choicesInicial={
        "1": self.IniciarSesion,
        #"2": self.Registrarme,
        #"3": FICTICIO.PobladoDeAplicacion,
        #"4": FICTICIO.DatosFicticiosTxt,
        "5": self.SalirPrincipal
        }

        self.choicesRegistrarme={
        "1": self.AgregarConductor,
        "2": self.AgregarPasajero,
        #"3": self.atras
        }

    @staticmethod
    def display_MenuInicial():
        print(MENSAJE.men.get("MenuInicial"))

    @staticmethod
    def display_MenuIniciarSesion():
        print(MENSAJE.men.get("MenuIniciarSesion"))

    @staticmethod
    def display_MenuVerificarCorreo():
        print(MENSAJE.men.get("MenuVerificarCorreo"))
        print(MENSAJE.men.get("Opcion"))

    @staticmethod
    def display_MenuResgistrarme():
        print(MENSAJE.men.get("MenuRegistrarme"))
        
    @staticmethod
    def display_MenuPasajero():
        print(MENSAJE.men.get("MenuPasajero"))
        
    @staticmethod
    def display_MenuConductor():
        print(MENSAJE.men.get("MenuConductor"))

    @staticmethod
    def display_MenuAdmin():
        print(MENSAJE.men.get("MenuAdmin"))
     
    @staticmethod
    def AgregarConductor():
        arconductor=open("Conductor.txt", "a")
        print(MENSAJE.men.get("Antes@"))
        while True:
            Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
            if CONDUCTOR.BuscadorDeConductor(Correo) == None:
                break
            else:
                print(MENSAJE.men.get("CorreoInvalido"))
        Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
        Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
        while True:
            Cell=eval(input(MENSAJE.men.get("IngresarCell")))
            if type(Cell) != int:
                print(MENSAJE.men.get("CelularInvalido"))
            else:
                break
        conductor=CONDUCTOR(Correo, Contrasena, Nombre, Cell)
        arconductor.write(Correo+","+Contrasena+","+Nombre+","+str(Cell)+",0,0\n")
        PRINCIPAL.AgregarVehiculo(conductor)

    @staticmethod
    def AgregarVehiculo(conductor):
        print(MENSAJE.men.get("InfoVehiculo"))
        while True:
            Placa=input(MENSAJE.men.get("IngresarPlaca"))
            if Placa == "3":
                return
            if VEHICULO.VerificarPlaca(Placa) == None:
                break
            else:
                print(MENSAJE.men.get("PlacaInvalida"))
        ColorVehiculo=input(MENSAJE.men.get("IngresarColor"))
        while True:
            TipoVehiculo=(input(MENSAJE.men.get("IngresarTipoVehiculo"))).lower()
            if TipoVehiculo!="moto" and TipoVehiculo!="carro":
                print(MENSAJE.men.get("ErrorTipoVehi"))
            else:
                break
        ModeloVehiculo=(input(MENSAJE.men.get("IngresarModeloVehi"))).lower()
        if TipoVehiculo=="moto":
            CantidadAsientos=2
        elif TipoVehiculo=="carro":
            CantidadAsientos=5
        if len(conductor.getVehiculos()) == 0:
            Activo="si"
        else:
            while True:
                Activo=(input(MENSAJE.men.get("ActivarVehiculo"))).lower()
                if Activo=="si":
                    if CONDUCTOR.VerificarActivacion(conductor) == False:
                        break
                else:
                    break
        VEHICULO(Placa, ColorVehiculo, TipoVehiculo, ModeloVehiculo, int(CantidadAsientos), conductor, Activo)

    @staticmethod
    def AgregarPasajero():
        print(MENSAJE.men.get("Antes@"))
        while True:
            Correo=(input(MENSAJE.men.get("IngresarCorreo"))+"@unal.edu.co").lower()
            if PASAJERO.BuscadorDePasajeros(Correo) == None:
                break
            else:
                print(MENSAJE.men.get("CorreoInvalido"))
        Contrasena=input(MENSAJE.men.get("IngresarContrasena"))
        Nombre=(input(MENSAJE.men.get("IngresarNombre"))).lower()
        while True:
            Cell=eval(input(MENSAJE.men.get("IngresarCell")))
            if type(Cell) != int:
                print(MENSAJE.men.get("CelularInvalido"))
            else:
                break
        PASAJERO(Correo, Contrasena, Nombre, Cell)

    @staticmethod
    def ProgramarViaje(infousuario):
        SERVICIO.ActualizarSerDis()
        Vehiculo=CONDUCTOR.VehiculoActivado(infousuario)
        if Vehiculo.getTipoVehiculo()=="moto":
            MaxAsientosDis=1
        elif Vehiculo.getTipoVehiculo()=="carro":
            MaxAsientosDis=4
        for servicio in SERVICIO.ServiciosDisponibles:
            if servicio.getConductorSer() == infousuario:
                print(MENSAJE.men.get("ServicioEnCurso"))
                return
        print(MENSAJE.men.get("InfoServicio"))
        while True:
            while True:
                opcion=input(MENSAJE.men.get("IngresarFecha"))
                lista=["1", "2"]
                if opcion in lista:
                    break
                else:
                    print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion == "1":
                FechaSer=time.strftime("%y/%m/%d")
                break
            elif opcion == "2":
                FechaSer=(datetime.today()+timedelta(days=1)).strftime("%y/%m/%d")
                break
        if opcion == "1":
            while True:
                HoraEncuentro=input(MENSAJE.men.get("IngresarHoraEncuentro"))
                if HoraEncuentro=="3":
                    return
                if HoraEncuentro<=time.strftime("%H:%M"):
                    print(MENSAJE.men.get("HoraYaPaso"))
                elif HoraEncuentro>time.strftime("%H:%M"):
                    break
        else:
            HoraEncuentro=input(MENSAJE.men.get("IngresarHoraEncuentro"))
        SitioEncuentro=(input(MENSAJE.men.get("IngresarSitioEncuentro"))).upper()
        LugarInicio=(input(MENSAJE.men.get("IngresarLugarInicio"))).upper()
        LugarFin=(input(MENSAJE.men.get("IngresarLugarFin"))).upper()
        while True:
            AsientosDisponibles=input(MENSAJE.men.get("IngresarAsientosDisponibles"))
            if int(AsientosDisponibles) > MaxAsientosDis:
                print(MENSAJE.men.get("AsientosMaximos").format(Vehiculo.getTipoVehiculo(), MaxAsientosDis))
            else:
                break
        SERVICIO(HoraEncuentro, SitioEncuentro, LugarInicio, LugarFin, AsientosDisponibles, infousuario, Vehiculo, FechaSer)

    @staticmethod
    def CrearComentario(infousuario):
        persona=PERSONA.BuscarPersona(infousuario.getCorreo())
        Descripcion=input(MENSAJE.men.get("IngresarDescripcion"))
        if Descripcion=="3":
            return
        Fecha=time.strftime("%d/%m/%y")
        COMENTARIO(Descripcion, persona, Fecha)

    @staticmethod
    def SalirPrincipal():
        print(MENSAJE.men.get("salir"))
        os._exit(0)

    @staticmethod
    def VerServicios(infousuario):
        SERVICIO.ActualizarSerDis()
        if len(SERVICIO.ServiciosDisponibles) == 0:
            print(MENSAJE.men.get("SinServicios"))
            return
        else:
            cont=1
            for servicio in SERVICIO.ServiciosDisponibles:
                print(MENSAJE.men.get("FormatoVerServicios").format(cont, servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre(), servicio.getVehiculoSer().getModeloVehiculo(), servicio.getFechaSer()))
                cont=cont+1
        PRINCIPAL.EscogerServicio(infousuario)

    @staticmethod
    def EscogerServicio(infousuario):
        while True:
            opcion=eval(input(MENSAJE.men.get("IngreseServicioEscogido")))
            if opcion<0 and opcion>len(SERVICIO.ServiciosDisponibles):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion==0:
                break
            else:
                servicio=SERVICIO.ServiciosDisponibles[opcion-1]
                if servicio.getAsientosDisponibles() == 0:
                    print(MENSAJE.men.get("ViajeLleno"))
                    return
                while True:
                    ServicioEspecial=input(MENSAJE.men.get("ServicioEspecialSioNo"))
                    if ServicioEspecial != "1" and ServicioEspecial != "2":
                        print(MENSAJE.men.get("OpcionIncorrecta").format(ServicioEspecial))
                    else:
                        break
                if ServicioEspecial == "1":
                    if servicio.getAsientosDisponibles() == 1:
                        print(MENSAJE.men.get("ViajeLleno"))
                        return
                    while True:
                        lista=["1", "2", "3", "4"]
                        razon=input(MENSAJE.men.get("MenuRazones")[0])
                        if razon in lista:
                            razon=[2, MENSAJE.men.get("MenuRazones")[int(razon)]]
                            break
                        else:
                            print(MENSAJE.men.get("OpcionIncorrecta").format(razon))
                else:
                    razon=[1]
                print(SERVICIO.ServicioTomado(infousuario, servicio, razon))
                return

    @staticmethod
    def VerViajeActual(infousuario):
        SERVICIO.ActualizarSerDis()
        if len(infousuario.getServicioActual())==0:
            print(MENSAJE.men.get("SinServiciosCon"))
            return
        servicio=infousuario.getServicioActual()[0]
        print(MENSAJE.men.get("FormatoViajeActual").format(servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles()))
        print(MENSAJE.men.get("MenuFormatoViajeActual"))
        while True:
            opcion=input(MENSAJE.men.get("Opcion"))
            lista=["1", "2", "3", "4"]
            if opcion in lista:
                break
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
        if opcion == "1":
            PRINCIPAL.CambioInfoSer(servicio)
        elif opcion == "2":
            print(SERVICIO.EliminarServicio(servicio))
        elif opcion == "3":
            PRINCIPAL.VerPasajeros(infousuario.getServicioActual()[0])
        elif opcion == "4":
            return

    @staticmethod
    def VerPasajeros(ServicioActual):
        print(MENSAJE.men.get("MensajeVerPasajero"))
        cont=1
        PasajeroxAsiento=ServicioActual.getPasajeroxAsiento()
        if len(ServicioActual.getPasajeros()) == 0:
            return print(MENSAJE.men.get("ServicioSinPasajeros"))
        for pasajero in ServicioActual.getPasajeros():
            if PasajeroxAsiento[pasajero][0] == 1:
                print(MENSAJE.men.get("FormatoVerPasajero")[1].format(cont, pasajero.getNombre(), pasajero.getCalificacionPromedio(), len(pasajero.getServiciosPa()), 1))
            elif PasajeroxAsiento[pasajero][0] == 2:
                print(MENSAJE.men.get("FormatoVerPasajero")[0].format(cont, pasajero.getNombre(), pasajero.getCalificacionPromedio(), len(pasajero.getServiciosPa()), 2, PasajeroxAsiento[pasajero][1]))
            cont+=1
        print(MENSAJE.men.get("EspacioVacio"))
        while True:
            opcion=input(MENSAJE.men.get("DeseaEliminarPas"))
            if opcion != "1" and opcion != "2":
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            else:
                break
        if opcion == "1":
            num=int(input(MENSAJE.men.get("QuePasDeseaEliminar")))
            print(SERVICIO.EliminarPasajeroDeServicio(ServicioActual, num))
        elif opcion == "2":
            return

    @staticmethod
    def CambioInfoSer(servicio):
        print(MENSAJE.men.get("CambiarInfo"))
        while True:
            cambio=input(MENSAJE.men.get("Opcion"))
            lista=["1", "2", "3", "4", "5", "6"]
            if cambio in lista:
                break
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(cambio))
        if cambio == "1":
            HoraNueva=input(MENSAJE.men.get("IngresarHoraEncuentro"))
            servicio.setHoraEncuentro(HoraNueva)
        elif cambio == "2":
            SitioNuevo=input(MENSAJE.men.get("IngresarSitioEncuentro"))
            servicio.setSitioEncuentro(SitioNuevo)
        elif cambio == "3":
            LugarNuevo=input(MENSAJE.men.get("IngresarLugarInicio"))
            servicio.setLugarInicio(LugarNuevo)
        elif cambio == "4":
            LugarNuevo=input(MENSAJE.men.get("IngresarLugarFin"))
            servicio.setLugarFin(LugarNuevo)
        elif cambio == "5":
            AsientosNuevo=input(MENSAJE.men.get("IngresarAsientosDisponibles"))
            servicio.setAsientosDisponibles(AsientosNuevo)
        elif cambio == "6":
            return
        return

    @staticmethod
    def InfoViaje(infousuario):
        if len(infousuario.getViajeActual())==0:
            print(MENSAJE.men.get("SinServicios"))
            return
        Servicio=infousuario.getViajeActual()[0]
        print(MENSAJE.men.get("FormatoInfoSer").format(Servicio.getHoraEncuentro(), Servicio.getSitioEncuentro(), Servicio.getLugarInicio(), Servicio.getLugarFin(), Servicio.getAsientosDisponibles(), Servicio.getFechaSer()))
        conductor=Servicio.getConductorSer()
        print(MENSAJE.men.get("FormatoInfoCon").format(conductor.getNombre(), conductor.getCell(), conductor.getNumeroServicios(), conductor.getAcumuladoCalificacion()))
        vehiculo=CONDUCTOR.VehiculoActivado(conductor)
        print(MENSAJE.men.get("FormatoInfoVehi").format(vehiculo.getPlaca(), vehiculo.getColor(), vehiculo.getTipoVehiculo(), vehiculo.getModeloVehiculo()))
        PRINCIPAL.MenuInfoViaje(infousuario)

    @staticmethod
    def MenuInfoViaje(infousuario):
        while True:
            print(MENSAJE.men.get("MenuInfoViaje"))
            opcion=input(MENSAJE.men.get("Opcion"))
            lista=["1", "2"]
            if opcion in lista:
                break
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
        if opcion == "1":
            servicio=infousuario.getViajeActual()[0]
            print(SERVICIO.EliminarPasajero(infousuario, servicio))
            return
        elif opcion == "2":
            return

    @staticmethod
    def VerMiHistorial(infousuario):
        if len(CONDUCTOR.getServiciosCon(infousuario))==0:
            print(MENSAJE.men.get("HistorialVacio"))
            return
        cont=1
        for servicio in CONDUCTOR.getServiciosCon(infousuario):
            print(MENSAJE.men.get("FormatoVerMiHistorial").format(cont, servicio.getFechaSer(), servicio.getHoraEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getCalificacionPromedioSer()))
            cont=cont+1
        PRINCIPAL.RevisarServicio(infousuario)

    @staticmethod
    def RevisarServicio(infousuario):
        while True:
            opcion=eval(input(MENSAJE.men.get("RevisarViaje")))
            if opcion == 0:
                return
            elif opcion<0 and opcion>len(CONDUCTOR.getServiciosCon(infousuario)):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            else:
                break
        servicio=(CONDUCTOR.getServiciosCon(infousuario))[opcion-1]
        cont=1
        for pasajero in servicio.getPasajeros():
            print(MENSAJE.men.get("FormatoRevisarPasajero").format(cont, pasajero.getNombre(), pasajero.getCell(), pasajero.getCalificacionPromedio()))
            cont=cont+1

    @staticmethod
    def CalificarServicio(infousuario):
        SERVICIO.ActualizarSerDis()
        if len(infousuario.getServicioNoCalificado()) == 0:
            print(MENSAJE.men.get("SinServiciosCalificacion"))
            return
        cont=1
        for servicio in infousuario.getServicioNoCalificado():
            print(MENSAJE.men.get("FormatoVerServicios").format(cont, servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre(), servicio.getFechaSer()))
            cont=cont+1
        while True:
            opcion=eval(input(MENSAJE.men.get("ServicioACalificar")))
            if opcion=="b":
                return
            elif type(opcion)!=int:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            elif opcion<=0 and opcion>len(infousuario.getServicioNoCalificado()):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            else:
                opcion=opcion-1
                break
        servicio=infousuario.getServicioNoCalificado()[opcion]
        while True:
            Calificacion=eval(input(MENSAJE.men.get("IngresarCalificacion")))
            if Calificacion<0 and Calificacion>5:
                print(MENSAJE.men.get("ValorMalCali"))
            elif Calificacion == 6:
                return
            else:
                break
        while True:
            opcion=input(MENSAJE.men.get("DeseaComentar"))
            if opcion!="1" and opcion!="2":
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            elif opcion=="1":
                Comentario=input(MENSAJE.men.get("IngresarComentario"))
                break
            elif opcion=="2":
                Comentario=None
                break
        CALIFICACION(Calificacion, Comentario, None, servicio)
        infousuario.getServicioNoCalificado().remove(servicio)

    @staticmethod
    def CalificarPasajeros(infousuario):
        SERVICIO.ActualizarSerDis()
        if len(infousuario.getPasajeroNoCalificado())==0:
            print(MENSAJE.men.get("SinPasajerosPorCalificar"))
            return
        cont=1
        for pasajero in infousuario.getPasajeroNoCalificado():
            print(MENSAJE.men.get("FormatoRevisarPasajero").format(cont, pasajero.getNombre(), pasajero.getCell(), pasajero.getCalificacionPromedio()))
            cont=cont+1
        while True:
            opcion=input(MENSAJE.men.get("PasajeroACalificar"))
            if opcion=="b":
                return
            elif opcion<0 and opcion>len(infousuario.getPasajeroNoCalificado()):
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            else:
                opcion=opcion-1
                break
        pasajero=infousuario.getPasajeroNoCalificado()[opcion]
        while True:
            Calificacion=eval(input(MENSAJE.men.get("IngresarCalificacion")))
            if Calificacion<0 and Calificacion>5:
                print(MENSAJE.men.get("ValorMalCali"))
            elif Calificacion == 6:
                return
            else:
                break
        while True:
            opcion=input(MENSAJE.men.get("DeseaComentar"))
            if opcion!="1" and opcion!="2":
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            elif opcion=="1":
                Comentario=input(MENSAJE.men.get("IngresarComentario"))
                break
            elif opcion=="2":
                Comentario=None
                break
        CALIFICACION(Calificacion, Comentario, pasajero)
        infousuario.getPasajeroNoCalificado().remove(pasajero)

    @staticmethod
    def VerPerfil(palabra, infousuario):
        if palabra=="PASAJERO":
            print(MENSAJE.men.get("FormatoVerPerfilPasajero").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getCalificacionPromedio()))
        elif palabra=="CONDUCTOR":
            print(MENSAJE.men.get("FormatoVerPerfilConductor").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getNumeroServicios(), infousuario.getAcumuladoCalificacion()))
        while True:
            print(MENSAJE.men.get("CambiarInfoVerPerfil"))
            opcion=input(MENSAJE.men.get("Opcion"))
            if opcion == "3":
                return
            lista=["1", "2", "3"]
            if opcion in lista:
                PRINCIPAL.CambiarInfoVerPerfil(palabra, opcion, infousuario)
                if palabra=="PASAJERO":
                    print(MENSAJE.men.get("FormatoVerPerfilPasajero").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getCalificacionPromedio()))
                    return
                elif palabra=="CONDUCTOR":
                    print(MENSAJE.men.get("FormatoVerPerfilConductor").format(infousuario.getCorreo(), infousuario.getContrasena(), infousuario.getNombre(), infousuario.getCell(), infousuario.getNumeroServicios(), infousuario.getAcumuladoCalificacion()))
                    return
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))

    @staticmethod
    def CambiarInfoVerPerfil(palabra, opcion, infousuario):
        if opcion == "1":
            contrasena=input(MENSAJE.men.get("IngresarNuevaContrasena"))
            infousuario.setContrasena(contrasena)
        elif opcion == "2":
            while True:
                Cell=eval(input(MENSAJE.men.get("IngresarNuevoCell")))
                if type(Cell) != int:
                    print(MENSAJE.men.get("CelularInvalido"))
                else:
                    break
            infousuario.setCell(cell)

    @staticmethod
    def Comentarios(infousuario):
        print(MENSAJE.men.get("MenuComentarios"))
        while True:
            opcion=input(MENSAJE.men.get("Opcion"))
            lista=["1", "2", "3"]
            if opcion in lista:
                break
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
        if opcion == "1":
            PRINCIPAL.CrearComentario(infousuario)
        elif opcion == "2":
            PRINCIPAL.VerHistorialComen(infousuario)
        elif opcion == "3":
            return

    @staticmethod
    def VerHistorialComen(infousuario):
        persona=PERSONA.BuscarPersona(infousuario.getCorreo())
        for comentario in persona.getComentarios():
            print(MENSAJE.men.get("FormatoComentarios").format(infousuario.getNombre(), comentario.getFecha(), comentario.getDescripcion()))

    @staticmethod
    def MejorCalificados():
        while True:
            lista=["1", "2"]
            print(MENSAJE.men.get("MenuMejorCalificados"))
            opcion=input(MENSAJE.men.get("Opcion"))
            if opcion in lista:
                break
            else:
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
        if opcion == "1":
            lista=PASAJERO.MejorCalificadosPasajero()
            for i in lista:
                print(i)
        elif opcion == "2":
            lista=CONDUCTOR.MejorCalificadosConductor()
            for i in lista:
                print(i)

    @staticmethod
    def InformacionSobre():
        print(MENSAJE.men.get("MenuInformacionSobre"))
        while True:
            lista=["1", "2", "3", "4", "5", "10"]
            opcion=input(MENSAJE.men.get("Opcion"))
            if opcion in lista:
                break
            else:
               print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
        if opcion == "1":
            PRINCIPAL.MejorCalificados()
        elif opcion == "2":
            print(MENSAJE.men.get("MensajeRutaFavorita"))
            for c in SERVICIO.RutaFavorita():
                print(c)
        elif opcion == "3":
            print(MENSAJE.men.get("MensajeVehiculoFavorito"))
            for c in SERVICIO.VehiculoFavorito():
                print(c)
        elif opcion == "4":
            print(MENSAJE.men.get("MensajeHoraMasConcurrida"))
            for c in SERVICIO.HoraMasConcurrida():
                print(c)
        elif opcion == "5":
            print(MENSAJE.men.get("MensajeConductorMasViajes"))
            for c in CONDUCTOR.ConductorConMasViajes():
                print(c)
        elif opcion == "10":
            return

    @staticmethod
    def IniciarSesion():
        infousuario=True
        while infousuario==True:
            print(MENSAJE.men.get("MensajeInicioSesion"))
            correo=(input(MENSAJE.men.get("IngresarCorreo"))).lower()
            if correo=="3":
                return
            contrasena=input(MENSAJE.men.get("IngresarContrasena"))
            infousuario=PERSONA.VerificarCorreo(correo, contrasena)
            if infousuario=="Invalido":
                print(MENSAJE.men.get("ContraOCorreoInvalido"))
                infousuario=True

        if type(infousuario)!=list:
            Pasajero=PASAJERO.BuscadorDePasajeros(infousuario.getCorreo())
            Conductor=CONDUCTOR.BuscadorDeConductor(infousuario.getCorreo())
            if Pasajero!=None:
                PRINCIPAL.InicioSesionPasajero(Pasajero)
            elif Conductor!=None:
                PRINCIPAL.InicioSesionConductor(Conductor)
        elif len(infousuario)==2 and type(infousuario)==list:
            PRINCIPAL.display_MenuVerificarCorreo()
            while True:
                opcion=input()
                lista=["1", "2", "3"]
                if opcion in lista:
                    break
                else:
                    print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion == "1":
                infousuario=PASAJERO.BuscadorDePasajeros(infousuario[0].getCorreo())
                PRINCIPAL.InicioSesionPasajero(infousuario)
            elif opcion == "2":
                infousuario=CONDUCTOR.BuscadorDeConductor(infousuario[0].getCorreo())
                PRINCIPAL.InicioSesionConductor(infousuario)
            elif opcion == "3":
                return
        print(MENSAJE.men.get("CerradoSesion"))

    @staticmethod
    def InicioSesionPasajero(infousuario):

        while True:
            PRINCIPAL.display_MenuPasajero()
            while True:
                opcion=input(MENSAJE.men.get("Opcion"))
                print("")
                lista=["1", "2", "3", "4", "5", "6", "7", "8"]
                if opcion in lista:
                    break
                else:
                    print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion == "1":
                PRINCIPAL.VerServicios(infousuario)
            elif opcion == "2":
                PRINCIPAL.InfoViaje(infousuario)
            elif opcion == "3":
                vermihistorial=PASAJERO.VerMiHistorial(infousuario)
                if vermihistorial == MENSAJE.men.get("HistorialVacio"):
                    print(vermihistorial)
                else:
                    for c in vermihistorial:
                        print(c)
            elif opcion == "4":
                PRINCIPAL.CalificarServicio(infousuario)
            elif opcion == "5":
                PRINCIPAL.Comentarios(infousuario)
            elif opcion == "6":
                PRINCIPAL.VerPerfil("PASAJERO", infousuario)
            elif opcion == "7":
                PRINCIPAL.InformacionSobre()
            elif opcion == "8":
                break
        
    @staticmethod
    def InicioSesionConductor(infousuario):

        while True:
            PRINCIPAL.display_MenuConductor()
            while True:
                opcion=input(MENSAJE.men.get("Opcion"))
                print("")
                lista=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
                if opcion in lista:
                	break
                else:
                    print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion == "1":
                PRINCIPAL.ProgramarViaje(infousuario)
            elif opcion == "2":
                PRINCIPAL.VerViajeActual(infousuario)
            elif opcion == "3":
                PRINCIPAL.VerMiHistorial(infousuario)
            elif opcion == "4":
                PRINCIPAL.AgregarVehiculo(infousuario)
            elif opcion == "5":
                vervehiculos=CONDUCTOR.VerVehiculos(infousuario)
                for c in vervehiculos:
                    print(c)
                while True:
                    option=input(MENSAJE.men.get("CambiarVehiActi"))
                    print("")
                    if option!="1" and option!="2":
                        print(MENSAJE.men.get("OpcionIncorrecta").format(option))
                    else: break
                if option == "1":
                    while True:
                        num=eval(input(MENSAJE.men.get("ActivacionVehi")))
                        if type(num) != int:
                            print(MENSAJE.men.get("OpcionIncorrecta").format(option))
                        elif num<1 and num>len(CONDUCTOR.getVehiculos()):
                            print(MENSAJE.men.get("OpcionIncorrecta").format(option))
                        else:
                            break
                    CONDUCTOR.CambioVehiActi(infousuario, num)
                    for c in CONDUCTOR.VerVehiculos(infousuario):
                        print(c)
            elif opcion == "6":
                PRINCIPAL.CalificarPasajeros(infousuario)
            elif opcion == "7":
                PRINCIPAL.Comentarios(infousuario)
            elif opcion == "8":
                PRINCIPAL.VerPerfil("CONDUCTOR", infousuario)
            elif opcion == "9":
                PRINCIPAL.InformacionSobre()
            elif opcion == "10":
                return
                
    @staticmethod
    def InicioSesionAdmin():

        infousuario=True
        while infousuario==True:
            print(MENSAJE.men.get("MensajeInicioSesion"))
            correo=(input(MENSAJE.men.get("IngresarCorreo"))).lower()
            if correo=="3":
                return
            contrasena=input(MENSAJE.men.get("IngresarContrasena"))
            archivo=open("registro.txt", "r").readlines()
            for line in archivo:
                line=line.split(",")
                if "ADMINISTRADOR" == line[0] and correo == line[1] and contrasena == line[2]:
                    infousuario=line
                    break
            if infousuario==True:
                print(MENSAJE.men.get("ContraOCorreoInvalido"))

        while True:
            PRINCIPAL.display_MenuAdmin()
            while True:
                opcion=input(MENSAJE.men.get("Opcion"))
                print("")
                lista=["1", "2", "3", "4", "5", "6"]
                if opcion in lista:
                    break
                else:
                    print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion == "1":
                for c in COMENTARIO.VerTodosLosComentarios():
                    print(c)
            elif opcion == "2":
                for c in PASAJERO.getListaPasajeros():
                    print(c)
            elif opcion == "3":
                for c in CONDUCTOR.getListaConductores():
                    print(c)
            elif opcion == "4":
                print(PASAJERO.EliminarPasajeroAdmin(input(MENSAJE.men.get("CorreoAEliminar"))))
            elif opcion == "5":
                print(CONDUCTOR.EliminarConductorAdmin(input(MENSAJE.men.get("CorreoAEliminar"))))
            elif opcion == "6":
                break

    @staticmethod
    def idiomaMensajes():

        while True:
            print(MENSAJE.Mensaje.get("textoIdioma"))
            while True:
                idioma = input(MENSAJE.Mensaje.get("SeleccioneIdioma"))
                if idioma!="1" and idioma!="2":
                    print(MENSAJE.espanol.get("OpcionIncorrecta").format(idioma))
                    print(MENSAJE.ingles.get("OpcionIncorrecta").format(idioma))
                else:
                    break
            if idioma =="1":
                MENSAJE.men = MENSAJE.espanol
                return
            elif idioma=="2":
                MENSAJE.men = MENSAJE.ingles
                return

    def runInicial(self):

        PRINCIPAL.idiomaMensajes()
        cont3=0
        cont4=0
        while True:
            self.display_MenuInicial()
            opcion=input(MENSAJE.men.get("Opcion"))
            if opcion == "3":
                cont3+=1
            elif opcion == "4":
                cont4+=1
            print("")
            action=self.choicesInicial.get(opcion)
            if action:
                action()
            elif opcion!="1" and opcion!="3" and opcion!="2" and opcion!="4" and opcion!="5" and opcion!="96":
                print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            elif opcion == "2":
                self.runRegistrarme()
            elif opcion == "96":
                self.InicioSesionAdmin()
            elif opcion == "3":
                if cont3 == 1:
                    FICTICIO.PobladoDeAplicacion()
                else:
                    print(MENSAJE.men.get("YaSeGeneraron"))
            elif opcion == "4":
                if cont4 == 1:
                    FICTICIO.DatosFicticiosTxt()
                else:
                    print(MENSAJE.men.get("YaSeGeneraron"))
                

    def runRegistrarme(self):

        while True:
            self.display_MenuResgistrarme()
            opcion=input(MENSAJE.men.get("Opcion"))
            print("")
            action=self.choicesRegistrarme.get(opcion)
            if action:
                action()
                break
            if opcion!="1" and opcion!="3" and opcion!="2":
                    print(MENSAJE.men.get("OpcionIncorrecta").format(opcion))
            if opcion=="3":
                break

if __name__=="__main__":
    PRINCIPAL().runInicial()