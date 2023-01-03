from teste_python.view1.tela_pessoa import TelaPessoa
from teste_python.model1.pessoa import Pessoa


class ControlaPessoa:
    def __init__(self, controlador_sistema):
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema
    
    def pega_pessoa_por_cpf(self, cpf:int):
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def incluir_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        pessoa = Pessoa(dados_pessoa["nome"], dados_pessoa["cpf"])
        self.__pessoas.append(pessoa) 
       
    def alterar_pessoa(self):
        self.lista_pessoas()
        cpf_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf_pessoa)
        
        if(pessoa is not None):
            novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.cpf = novos_dados_pessoa["cpf"]
            self.lista_pessoas()
        else:
            self.__tela_pessoa.mostra_mensagem("Essa pessoa não existe")
            
    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    
    def lista_pessoas(self):
        print ("\nExistem {} pessoas no sistema".format(len(self.__pessoas)))
        for pessoa in self.__pessoas:
            self.__tela_pessoa.mostra_pessoa({"nome": pessoa.nome, "cpf": pessoa.cpf})
    
    def excluir_pessoa(self):
        self.lista_pessoas()
        cpf_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.pega_pessoa_por_cpf(cpf_pessoa)
        
        if(pessoa is not None):
            self.__pessoas.remove(pessoa)
            self.lista_pessoas()
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa inexistente")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1:self.incluir_pessoa, 2:self.alterar_pessoa, 3:self.lista_pessoas, 4:self.excluir_pessoa, 0:self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()