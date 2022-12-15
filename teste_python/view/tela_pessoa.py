
class TelaPessoa:
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("----- PESSOA -----")
        print("Qual sua opcao")
        print("1 - Incluir pessoa")
        print("2 - Alterar pessoa")
        print("3 - Listar pessoa")
        print("4 - Excluir pessoa")
        print("0 - Retornar")
        
        opcao = int(input("Qual sua opcao na tela pessoa: "))
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_pessoa(self):
        print("----- Dados da pessoa -----")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        
        return {"nome": nome, "cpf": cpf}
    
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_pessoa(self, dados_pessoa):
        print("Nome da pessoa: ", dados_pessoa["nome"])
        print("CPF: ", dados_pessoa["cpf"])
        print("\n")
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_pessoa(self):
        cpf = input("CPF da pessoa a ser selecionada: ")
        return cpf
    
    def mostra_mensagem(self, msg):
        print(msg)