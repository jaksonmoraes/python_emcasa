from view.tela_pessoa import TelaPessoa
from model.pessoa import Pessoa
from view.tela_carro import TelaCarro
from model.carro import Carro
from control.controla_carro import ControlaCarro
from view.tela_venda import TelaVenda


class ControlaVenda:
    def __init__(self, controlador_sistema):
        self.__vendas = []
        self.__tela_pessoa = TelaPessoa()
        self.__tela_carro = TelaCarro()
        self.__controlador_sistema = controlador_sistema
        self.__mostra_carros = mostra_carros
    
    def lista_carros_disponiveis(self):
        self.__mostra_carros.lista_carros()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1:self.lista_carros_disponiveis, 0:self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.tela_venda.tela_opcoes()]()