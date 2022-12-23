from teste_python.model.carro import Carro
from teste_python.view.tela_carro import TelaCarro


class ControlaCarro:
    def __init__(self, controlador_sistema):
        self.__carros = []
        self.__tela_carro = TelaCarro()
        self.__controlador_sistema = controlador_sistema
    
    def pega_carro_por_placa(self, placa: int):
        for carro in self.__carros:
            if carro.placa == placa:
                return carro
            return None
    
    def incluir_carro(self):
        dados_carro = self.__tela_carro.pega_dados_carro()
        carro = Carro(dados_carro["modelo"], dados_carro["placa"])
        self.__carros.append(carro)
    
    def alterar_carro(self):
        self.lista_carros()
        placa_carro = self.__tela_carro.seleciona_carro()
        carro = self.pega_carro_por_placa(placa_carro)

        if(carro is not None):
            novos_dados_carro = self.__tela_carro.pega_dados_carro()
            carro.modelo = novos_dados_carro["modelo"]
            carro.placa = novos_dados_carro["placa"]
            self.lista_carros()
        else:
            self.__tela_carro.mostra_mensagem("Esta carroça no existe")
    
    def lista_carros(self):
        print("\nExistem {} carros no sistema".format(len(self.__carros)))
        for carro in self.__carros:
            self.__tela_carro.mostra_carro({"modelo": carro.modelo, "placa": carro.placa})
    
    def excluir_carro(self):
        self.lista_carros()
        placa_carro = self.__tela_carro.seleciona_carro()
        carro = self.pega_carro_por_placa(placa_carro)

        if(carro is not None): #and carro in self.__carros:
            self.__carros.remove(carro)
            self.lista_carros()
        else:
            self.__tela_carro.mostra_mensagem("Carroça inexistente")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_carro, 2: self.alterar_carro, 3: self.lista_carros, 4: self.excluir_carro, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_carro.tela_opcoes()]()
