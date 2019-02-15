class VEHICULO:

    ListaVehiculos=[]

    def __init__(self, Placa, Color, TipoVehiculo, ModeloVehiculo, CantidadAsientos, Conductor, Activo):

        '''ATRIBUTOS
        self._Placa
        self._Color
        self._TipoVehiculos
        self._ModeloVehiculo
        self._CantidadAsientos
        self._Conductor
        '''

        self.setPlaca(Placa)
        self.setColor(Color)
        self.setTipoVehiculo(TipoVehiculo)
        self.setModeloVehiculo(ModeloVehiculo)
        self.setCantidadAsientos(CantidadAsientos)
        self.setConductorVe(Conductor)
        self.setActivo(Activo)
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

    def setModeloVehiculo(self, modelovehiculo):
        self._ModeloVehiculo=modelovehiculo

    def getModeloVehiculo(self):
        return self._ModeloVehiculo

    def setCantidadAsientos(self, cantidadAsientos):
        self._CantidadAsientos=cantidadAsientos

    def getCantidadAsientos(self):
        return self._CantidadAsientos

    def setConductorVe(self, conductor):
        self._Conductor=conductor
        conductor.setVehiculos(self)

    def getConductorVe(self):
        return self._conductor

    def setActivo(self, activo):
        self._Activo=activo

    def getActivo(self):
        return self._Activo

    @staticmethod
    def VerificarPlaca(Placa):
        for vehiculo in VEHICULO.ListaVehiculos:
            if Placa == vehiculo.getPlaca():
                return vehiculo

    @staticmethod
    def BuscadorDeVehiculo(Placa):
        for vehiculo in VEHICULO.ListaVehiculos:
            if Placa == vehiculo.getPlaca():
                return vehiculo