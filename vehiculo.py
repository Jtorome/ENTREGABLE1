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
        self.setTipoVehiculo(TipoVehiculo)
        self.setCantidadAsientos(CantidadAsientos)
        self.setConductorVe(Conductor)
        VEHICULO.ListaVehiculos.append(self)

    def setPlaca(self, placa):
        self._Placa=placa

    def getPlaca(self):
        return self._Placa

    def setColor(self, color):
        self._Color=color

    def getColor(self):
        return self._Color

    def setTipoVehiculo(self, tipoVehiculo):
        self._TipoVehiculo=tipoVehiculo

    def getTipoVehiculo(self):
        return self._TipoVehiculo

    def setCantidadAsientos(self, cantidadAsientos):
        self._CantidadAsientos=int(cantidadAsientos)

    def getCantidadAsientos(self):
        return self._CantidadAsientos

    def setConductorVe(self, conductor):
        self._Conductor=conductor
        conductor.setVehiculos(self)

    def getConductorVe(self):
        return self._conductor