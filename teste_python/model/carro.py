class Carro:
    def __init__(self, placa:int, modelo:str):
        self.__placa = placa
        self.__modelo = modelo
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def modelo(self):
        return  self.__modelo
    
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    
    @modelo.setter
    def modelo(self, modelo):
        self.modelo = modelo