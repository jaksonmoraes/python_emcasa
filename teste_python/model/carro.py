class Carro:
    def __init__(self, placa:int, modelo:str):
        self.__placa = placa
        self.__modelo = modelo
    
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

## termina aqui