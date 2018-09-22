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

        self.setPlaca(Placa)
        self.setColor(Color)
        self.setTipoVehiculos(TipoVehiculos)
        self.setCantidadAsientos(CantidadAsientos)
        self.setConductorVe(onductor)
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

    def setConductorVe(self, conductor):
        self._Conductor=conductor
        conductor.setVehiculo(self)

    def getConductorVe(self):
        return self._conductor