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
        SERVICIO("08:00", "MINAS", "M8", "12", 1, Cjuan, v1juan, "19/02/07", 0)
        S3juan=SERVICIO("12:00", "MINAS", "M8", "4", 4, Cjuan, v1juan, "19/03/20", 0)
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