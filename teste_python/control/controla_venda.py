from view.tela_pessoa import TelaPessoa
from model.pessoa import Pessoa
from view.tela_carro import TelaCarro
from model.carro import Carro
from control.controla_carro import ControlaCarro
from view.tela_venda import TelaVenda


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
        for carro in self.__carros:
            self.__tela_carro.mostra_carro(dados_carro)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1:self.lista_carros_disponiveis, 0:self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()