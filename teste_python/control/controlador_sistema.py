from view.tela_sistema import TelaSistema
from control.controla_pessoa import ControlaPessoa

class ControladorSistema:
    def __init__(self):
        self.__controlador_pessoa = ControlaPessoa(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_pessoa(self):
        #chama o controlador de pessoa
        self.__controlador_pessoa.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        lista_opcoes = {1:self.cadastra_pessoa, 0:self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        