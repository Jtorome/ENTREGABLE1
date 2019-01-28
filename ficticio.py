from pasajero import PASAJERO
from conductor import CONDUCTOR
from vehiculo import VEHICULO
from servicio import SERVICIO
from calificacion import CALIFICACION
from comentario import COMENTARIO
from persona import PERSONA
class FICTICIO:

    nombres=["Juan", "Camilo", "Maria", "Julia", "Manuela","Eduardo", "Sergio", "Cristian", "Jhonatan", "Louis", "Slappy", "Rose", "Yami"]
    apellidos=["Toro", "Ramirez", "Cabrera", "Santos", "Cordoba", "Vermillion", "Chronos", "Mejia", "Sanchez", "Montoya", "Cortes", "Heisenberg"]
    

    @staticmethod
    def DatosFicticiosTxt():
        archivo=open("registro.txt", "r").readlines()
        for line in archivo:
            line=line.split(',')
            if "PASAJERO" == line[0]:
                PASAJERO(line[1], line[2], line[3], line[4], line[5].split()[0])
            elif "CONDUCTOR" == line[0]:
                CONDUCTOR(line[1], line[2], line[3], line[4], line[5], line[6].split()[0])
            elif "VEHICULO" == line[0]:
                for conductor in CONDUCTOR.ListaConductores:
                    correo=line[5].split()
                    if correo[0] == conductor.getCorreo():
                        VEHICULO(line[1], line[2], line[3], line[4], conductor, line[6].split()[0])
            elif "SERVICIO" == line[0]:
                for conductor in CONDUCTOR.ListaConductores:
                    correo=line[6].split()
                    if correo[0] == conductor.getCorreo():
                        SERVICIO(line[1], line[2], line[3], line[4], line[5], conductor, line[7], line[8].split()[0])

        for servicio in SERVICIO.ListaServicios:
            text=servicio.getInformacionSerCompleta().split(',')
            for line in archivo:
                line=line.split(',')
                if line[0]=="SERVICIO":
                    if len(line)==10 and text[1]==line[1] and text[6]==line[6] and text[7]==line[7]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[9].split()[0])
                        servicio.setPasajeros(pasajero)
                    elif len(line)==11 and text[1]==line[1] and text[6]==line[6] and text[7]==line[7]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[9])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10].split()[0])
                        servicio.setPasajeros(pasajero)
                    elif len(line)==12 and text[1]==line[1] and text[6]==line[6] and text[7]==line[7]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[9])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[11].split()[0])
                        servicio.setPasajeros(pasajero)
                    elif len(line)==13 and text[1]==line[1] and text[6]==line[6] and text[7]==line[7]:
                        pasajero=PASAJERO.BuscadorDePasajeros(line[9])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[10])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[11])
                        servicio.setPasajeros(pasajero)
                        pasajero=PASAJERO.BuscadorDePasajeros(line[12].split()[0])
                        servicio.setPasajeros(pasajero)
                    SERVICIO.ActualizarSerDis()
                elif "CALIFICACION"==line[0]:
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
                    COMENTARIO(line[1], persona, line[3].split()[0])