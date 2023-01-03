from teste_python.view.tela_pessoa import TelaPessoa
from teste_python.view.tela_carro import TelaCarro
from teste_python.control.controla_carro import ControlaCarro
from teste_python.view.tela_venda import TelaVenda


class ControlaVenda:
    def __init__(self, controlador_sistema):
        self.__vendas = []
        self.__carros = []
        self.__tela_pessoa = TelaPessoa()
        self.__tela_carro = TelaCarro()
        self.__tela_venda = TelaVenda()
        self.__controlador_sistema = controlador_sistema
        self.__controla_carro = ControlaCarro(self)
    
    def lista_carros_disponiveis(self):
        print("\nExistem {} carros no sistema".format(len(self.__carros)))
        for carro in self.__carros:
            self.__tela_carro.mostra_carro({"modelo": carro.modelo, "placa": carro.placa})
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1:self.lista_carros_disponiveis, 0:self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()