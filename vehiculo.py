class VEHICULO:

    ListaVehiculos=[]

    def __init__(self, Placa, Color, TipoVehiculo, CantidadAsientos, Conductor):

        '''ATRIBUTOS
        self._Placa
        self._Color
        self._TipoVehiculos
        self._CantidadAsientos
        self._Conductor
        '''

        self.setPlaca(placa)
        self.setColor(color)
        self.setTipoVehiculos(tipoVehiculos)
        self.setCantidadAsientos(cantidadAsientos)
        self.setConductor(conductor)
        VEHICULO.ListaVehiculos.append(self)

    def setPlaca(self, placa):
        self._Placa=placa

    def getPlaca(self):
        return self._Placa

    def setColor(self, color):
        self._Color=color

    def getColor(self):
        return self._Color

    def SetTipoVehiculo(self, tipoVehiculo):
        self._TipoVehiculo=TipoVehiculo

    def getTipoVehiculo(self):
        return self._TipoVehiculo

    def SetCantidadAsientos(self, cantidadAsientos):
        self._CantidadAsientos=int(CantidadAsientos)

    def getCantidadAsientos(self):
        return self._CantidadAsientos

    @staticmethod
    def setConductor(self, conductor):
        self._Conductor=conductor
        conductor.setVehiculo(self)

    @staticmethod
    def getConductor(self):
        return self._conductor