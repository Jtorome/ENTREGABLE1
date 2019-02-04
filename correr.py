from persona import PERSONA
from pasajero import PASAJERO
from conductor import CONDUCTOR
from servicio import SERVICIO
from calificacion import CALIFICACION
from vehiculo import VEHICULO
from comentario import COMENTARIO
from mensaje import MENSAJE
from principal import PRINCIPAL
from datetime import datetime, date, time, timedelta
import calendar
import time
#"SERVICIO,"+servicio.getHoraEncuentro()+","+servicio.getSitioEncuentro()+","+servicio.getLugarInicio()+","+servicio.getLugarFin()+","+str(servicio.getAsientosDisponibles())+","+(servicio.getConductorSer()).getCorreo()+","+servicio.getFechaSer()+","+str(servicio.getCalificacionPromedioSer())+"\n"
class CORRER:

    """archivo=open("registro.txt", "r").readlines()
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
            linea=line.split(',')
            if linea[0]=="SERVICIO":
                if len(linea)==10 and text[1]==linea[1] and text[6]==linea[6] and text[7]==linea[7]:
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[9].split()[0])
                    servicio.setPasajeros(pasajero)
                elif len(linea)==11 and text[1]==linea[1] and text[6]==linea[6] and text[7]==linea[7]:
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[9])
                    servicio.setPasajeros(pasajero)
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[10].split()[0])
                    servicio.setPasajeros(pasajero)
                elif len(linea)==12 and text[1]==linea[1] and text[6]==linea[6] and text[7]==linea[7]:
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[9])
                    servicio.setPasajeros(pasajero)
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[10])
                    servicio.setPasajeros(pasajero)
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[11].split()[0])
                    servicio.setPasajeros(pasajero)
                elif len(linea)==13 and text[1]==linea[1] and text[6]==linea[6] and text[7]==linea[7]:
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[9])
                    servicio.setPasajeros(pasajero)
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[10])
                    servicio.setPasajeros(pasajero)
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[11])
                    servicio.setPasajeros(pasajero)
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[12].split()[0])
                    servicio.setPasajeros(pasajero)
                SERVICIO.ActualizarSerDis()
            elif "CALIFICACION"==linea[0]:
                if len(linea)==8:
                    servicio=SERVICIO.BuscadorDeServicio(linea[4], linea[5], linea[6].split()[0])
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[7].split()[0])
                    CALIFICACION(linea[1], linea[2], linea[3], servicio)
                    pasajero.getServicioNoCalificado().remove(servicio)
                if len(linea)==5:
                    pasajero=PASAJERO.BuscadorDePasajeros(linea[3])
                    conductor=CONDUCTOR.BuscadorDeConductor(linea[4].split()[0])
                    CALIFICACION(linea[1], linea[2], pasajero)
                    conductor.getPasajeroNoCalificado().remove(pasajero)
            elif "COMENTARIO"==linea[0]:
                persona=PERSONA.BuscarPersona(linea[2])
                COMENTARIO(linea[1], persona, linea[3].split()[0])

    x=["1", CONDUCTOR.BuscadorDeConductor("juan@unal.edu.co")]
    print(x[1].getCorreo())
    print(type(x))
    if x == None:
        print("bLA")"""

    infousuario=True
    while infousuario==True:
        print(MENSAJE.espanol.get("MensajeInicioSesion"))
        correo=(input(MENSAJE.espanol.get("IngresarCorreo"))).lower()
        if correo=="3":
            break
        contrasena=input(MENSAJE.espanol.get("IngresarContrasena"))
        archivo=open("registro.txt", "r").readlines()
        for line in archivo:
            line=line.split(",")
            print("aca")
            if "ADMINISTRADOR" == line[0] and correo == line[1] and contrasena == line[2]:
                infousuario=line
                break
    if infousuario==True:
        print(infousuario)

    """pasajero=PASAJERO.BuscadorDePasajeros("alberto@unal.edu.co")
    persona=PERSONA.BuscarPersona("juan@unal.edu.co")
    print(persona.getComentarios()[0].getDescripcion())
    print(pasajero.getCalificacionPromedio())"""

    """servicio=SERVICIO.ListaServicios[0]
    archivo=open("registro.txt", "r").readlines()
    text=servicio.getInformacionSerCompleta().split(',')
    print(text)
    for line in archivo:
        if "SERVICIO"==line.split(',')[0]:
            linea=line.split(',')
            print(linea)
            if linea[1]==text[1] and linea[6]==text[6] and linea[7]==text[7]:
                print(text)"""

    """formato="%y/%m/%d"
    dia=datetime.now()
    day=dia.strftime(formato)
    bla=datetime.strptime(day, formato)
    print(bla)"""

    """for conductor in CONDUCTOR.ListaConductores:
        if "juan@unal.edu.co"==conductor.getCorreo():
            Conductor=conductor

    for vehiculo in conductor.getVehiculos():
        print(vehiculo.getActivo())
        if vehiculo.getActivo()=="si":
            print(type(vehiculo))"""

    #vehiculo=CONDUCTOR.VehiculoActivado(Conductor)
    #print(vehiculo)

    """actual=time.strftime("%y/%m/%d")
    a=actual.split('/')
    pasada="18/09/31"
    p=pasada.split('/')
    if actual > pasada:
        print("SIP")
    if a[2] >= p[2] and a[1] >= p[1] and a[0] > p[0]:
        print("DIA MAYOR")
    elif a[2] >= p[2] and a[1] >= p[1] and a[0] == p[0]:
        print("DIA IGUAL")"""

    """archivo=open("registro.txt", "r").readlines()
    out=open("registro.txt", "w")
    for line in archivo:
        line=line.replace(",ACTIVO", "")
        out.writelines(line)"""

    """contenido= list()

    with open('registro.txt', 'r') as archivo:
        for linea in archivo:
            columnas = linea.replace(",ACTIVO", "")
            columnas= columnas.split(',')
            contenido.append(','.join(columnas))

    print(contenido)
    with open('registro.txt', 'w') as archivo:
        archivo.writelines(contenido)"""

    """actual=time.strftime("%H:%M")
    pasada="17:59"
    if pasada>actual:
        print("SI")"""

    """conductor1 = CONDUCTOR("tro@unal.edu.co", "1234", "Bla", "12324")
    servicio1=SERVICIO("7:30", "Agora", "Bloque 12", "M7", 3, conductor1 )  
    pasajero1=PASAJERO("Juan", "hola", "JUAN", "1232")
    servicio1.setPasajeros(pasajero1)
    for servicios in pasajero1.getServiciosPa():
        print(servicios.getHoraEncuentro())
    print(pasajero1.getServiciosPa())
    if len(SERVICIO.ServiciosDisponibles) ==0:
        print(MENSAJE.espanol.get("SinServicios"))
    else:
        cont=1
        for servicio in SERVICIO.ServiciosDisponibles:
            print(MENSAJE.espanol.get("FormatoVerServicios").format(cont,servicio.getHoraEncuentro(), servicio.getSitioEncuentro(), servicio.getLugarInicio(), servicio.getLugarFin(), servicio.getAsientosDisponibles(), servicio.getConductorSer().getNombre()))
            cont=cont+1"""

    """PASAJERO("Juan", "hola", "JUAN", "1232")
    for pasajeros in PASAJERO.listaPasajeros:
        print(pasajeros.getCorreo())"""

    #archivo=open("registro.txt", "a")
    #X=(b'jtorom@unal.edu.co' in b'archivo')
    
    """archivo=open("registro.txt", "r").readlines()
    a=archivo[1].split(',')
    print(a)
    print(len(a))"""

    """archivo=open("registro.txt", "r").readlines()
    for line in archivo:
        line=line.split(',')
        if "PASAJERO" == line[0]:
            PASAJERO(line[1], line[2], line[3], line[4])
        elif "CONDUCTOR" == line[0]:
            CONDUCTOR(line[1], line[2], line[3], line[4])
        elif "VEHICULO" == line[0]:
            for conductor in CONDUCTOR.ListaConductores:
                correo=line[5].split()
                if correo[0] == conductor.getCorreo():
                    VEHICULO(line[1], line[2], line[3], line[4], conductor)

    for vehiculo in VEHICULO.ListaVehiculos:
        print(vehiculo.getPlaca())"""

    """for pasajeros in PASAJERO.listaPasajeros:
        print(pasajeros.getCorreo()+", "+pasajeros.getNombre())"""

    """for conductores in CONDUCTOR.ListaConductores:
        for vehiculo in conductores.getVehiculos():
            print(vehiculo.getPlaca())"""

    """archivo=open("registro.txt", "r").readlines()
    for line in archivo:
        print(line)"""
    """a=archivo[1].split(',')
    print(a)"""
    """linea=0
    for line in archivo:
        if "scabrera" in line:
            break
        linea=linea+1   
    X=archivo[linea]
    X=X.split(',')
    print(X)
    X=X[2]
    if X=="admin2":
        print(X)"""

    """contra=0
    linea=0
    line1=0
    line2=0
    cont=0
    correo="juan@unal.edu.co"
    contrasena="hola"
    for line in archivo:
        cont=cont+1
        line=line.split(',')
        print(cont)
        if correo==line[1]:
            if contrasena==line[2]:
                contra=contra+1
                if(contra==1):
                    line1=linea
                if(contra>1):
                    line2=linea
        linea=linea+1

    line1=archivo[line1]
    line2=archivo[line2]
    print(line1)
    print(line2)"""
    
    #print(archivo[0])
    #pasajero1 = PASAJERO()

    """pasajero1=PASAJERO("juan@unal.edu.co", "hola", "juan toro", "310")
    conductor1=CONDUCTOR("alberto@unal.edu.co", "bla", "alberto toro", "314")
    servicio1=SERVICIO("17:20", "Volador", "12", "M8", "1", conductor1, "18/11/5")
    calificacion1 = CALIFICACION(3.0, "NO JODA CARE MONDA", pasajero1)
    calificacion2 = CALIFICACION(4.0, "NO JODA CARE MONDA", None, servicio1)
    calificacion2 = CALIFICACION(4.5, "NO JODA CARE MONDA", None, servicio1)
    print(pasajero1.getCalificacionPromedio())
    print(conductor1.getAcumuladoCalificacion())"""


    """persona1=PERSONA("Juan", "hola", "JUAN", "1232")
    comentario1=COMENTARIO("MUY MALO", persona1)
    print(comentario1.getFecha())"""

    #print(servicio1.getHoraEncuentro())
    #print(servicio1.getCalificacionPromedioSer())
    #print(conductor1.getAcumuladoCalificacion())
    #print(conductor1.getNumeroServicios())
    #print(pasajero1.getCalificacionPromedio())
    #print("TIPO DE VEHICULOS: ")
    #vehiculo1=VEHICULO("etd305", "rojo", "Carro", 5, conductor1)
    #vehiculo2=VEHICULO("s", "verde","Moto", 2, conductor1)
    #con=conductor1.getVehiculos()
    #for vehi in con:
#       print(vehi.getTipoVehiculo())

#toro es un imbecil
#SERGIO IMBECIL