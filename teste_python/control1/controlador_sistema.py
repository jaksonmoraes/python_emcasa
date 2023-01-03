from teste_python.view1.tela_sistema import TelaSistema
from teste_python.control1.controla_pessoa import ControlaPessoa
from teste_python.control1.controla_carro import ControlaCarro
from teste_python.control1.controla_venda import ControlaVenda


class ControladorSistema:
    def __init__(self):
        self.__controlador_pessoa = ControlaPessoa(self)
        self.__controlador_carro = ControlaCarro(self)
        self.__controlador_venda = ControlaVenda(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    @property
    def controlador_carro(self):
        return self.__controlador_carro
    
    @property
    def controlador_venda(self):
        return self.controlador_venda
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_pessoa(self):
        #chama o controlador de pessoa
        self.__controlador_pessoa.abre_tela()
    
    def cadastra_carro(self):
        self.__controlador_carro.abre_tela()
    
    def cadastra_venda(self):
        self.__controlador_venda.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        lista_opcoes = {1:self.cadastra_pessoa, 2:self.cadastra_carro, 3:self.cadastra_venda, 0:self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        