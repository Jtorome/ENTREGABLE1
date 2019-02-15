from pasajero import PASAJERO
from conductor import CONDUCTOR
from vehiculo import VEHICULO
from servicio import SERVICIO
from calificacion import CALIFICACION
from comentario import COMENTARIO
from persona import PERSONA
class FICTICIO:
    
    @staticmethod
    def PobladoDeAplicacion():
        Cjuan=CONDUCTOR("juan@unal.edu.co", "hola", "juan toro", 310, 0, 0)
        v1juan=VEHICULO("xyz123", "Rojo", "carro", "spark", 4, Cjuan, "no")
        v2juan=VEHICULO("qwe563", "negro", "moto", "dt", 2, Cjuan, "si")
        Pjuan=PASAJERO("juan@unal.edu.co", "hola", "juan toro", 310, 0)
        Palberto=PASAJERO("alberto@unal.edu.co", "bla", "alberto toro", 314, 0)
        Ptoro=PASAJERO("toro@unal.edu.co", "Juan", "toro alberto", 315, 0)
        S1juan=SERVICIO("17:20", "Volador", "12", "M8", 4, Cjuan, v1juan, "19/01/28", 0)
        S1juan.setPasajeros(Palberto, [1])
        S1juan.setPasajeroxAsiento(Palberto, [1])
        S2juan=SERVICIO("08:00", "MINAS", "M8", "12", 1, Cjuan, v2juan, "19/02/06", 0)
        S3juan=SERVICIO("12:00", "MINAS", "M8", "4", 2, Cjuan, v1juan, "19/02/20", 0)
        S3juan.setPasajeros(Ptoro, [1])
        S3juan.setPasajeroxAsiento(Ptoro, [1])
        SERVICIO.ActualizarSerDis()
        C1=CALIFICACION(4, "Muy bueno", "None", S1juan)
        Palberto.getServicioNoCalificado().remove(S1juan)
        C2=CALIFICACION(4, "None", Palberto)
        Cjuan.getPasajeroNoCalificado().remove(Palberto)
        persona=PERSONA.BuscarPersona("juan@unal.edu.co")
        CO1=COMENTARIO("Muy malo mejorar ", persona, "05/11/18")

    @staticmethod
    def DatosFicticiosTxt():
        archivo=open("Conductor.txt", "r").readlines()
        for line in archivo:
            line=line.split(',')
            CONDUCTOR(line[0], line[1], line[2], line[3], line[4], line[5])

    """@staticmethod
    def DatosFicticiosTxt():
        archivo=open("registro.txt", "r").readlines()
        for line in archivo:
            line=line.split(',')
            if "PASAJERO" == line[0]:
                if PASAJERO.BuscadorDePasajeros(line[1]) == None:
                    PASAJERO(line[1], line[2], line[3], line[4], float(line[5].split()[0]))
            elif "CONDUCTOR" == line[0]:
                if CONDUCTOR.BuscadorDeConductor(line[1]) == None:
                    CONDUCTOR(line[1], line[2], line[3], line[4], line[5], line[6].split()[0])
            elif "VEHICULO" == line[0]:
                if  VEHICULO.VerificarPlaca(line[1]) == False:
                    for conductor in CONDUCTOR.ListaConductores:
                        correo=line[6].split()
                        if correo[0] == conductor.getCorreo():
                            VEHICULO(line[1], line[2], line[3], line[4], line[5], conductor, line[7].split()[0])
            elif "SERVICIO" == line[0]:
                if SERVICIO.BuscadorDeServicio(line[1], line[6], line[7]) == None:
                    for conductor in CONDUCTOR.ListaConductores:
                        correo=line[6].split()
                        if correo[0] == conductor.getCorreo():
                            vehiculo=VEHICULO.BuscadorDeVehiculo(line[7])
                            SERVICIO(line[1], line[2], line[3], line[4], line[5], conductor, vehiculo, line[8], line[9].split()[0])

        for servicio in SERVICIO.ListaServicios:
            text=servicio.getInformacionSerCompleta().split(',')
            for line in archivo:
                line=line.split(',')
                if line[0]=="SERVICIO":
                    if len(line)==11 and text[1]==line[1] and text[6]==line[6] and text[8]==line[8]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10].split()[0])
                        servicio.setPasajeros(pasajero)
                    elif len(line)==12 and text[1]==line[1] and text[6]==line[6] and text[8]==line[8]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[11].split()[0])
                        servicio.setPasajeros(pasajero)
                    elif len(line)==13 and text[1]==line[1] and text[6]==line[6] and text[8]==line[8]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[11])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[12].split()[0])
                        servicio.setPasajeros(pasajero)
                    elif len(line)==14 and text[1]==line[1] and text[6]==line[6] and text[8]==line[8]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[11])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[12])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[13].split()[0])
                        servicio.setPasajeros(pasajero)
                    SERVICIO.ActualizarSerDis()

        for line in archivo:
            line=line.split(',')
            if "CALIFICACION"==line[0]:
                if len(line)==8:
                    servicio=SERVICIO.BuscadorDeServicio(line[4], line[5], line[6].split()[0])
                    pasajero=PASAJERO.BuscadorDePasajeros(line[7].split()[0])
                    CALIFICACION(line[1], line[2], line[3], servicio)
                    pasajero.getServicioNoCalificado().remove(servicio)
                elif len(line)==5:
                    pasajero=PASAJERO.BuscadorDePasajeros(line[3])
                    conductor=CONDUCTOR.BuscadorDeConductor(line[4].split()[0])
                    CALIFICACION(line[1], line[2], pasajero)
                    conductor.getPasajeroNoCalificado().remove(pasajero)
            elif "COMENTARIO"==line[0]:
                persona=PERSONA.BuscarPersona(line[2])
                COMENTARIO(line[1], persona, line[3].split()[0])"""