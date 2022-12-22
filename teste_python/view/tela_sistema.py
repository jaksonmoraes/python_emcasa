class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("------------SisPessoa----------------")
        print("Escolha sua opção")
        print("1 - Pessoa")
        print("2 - Carro")
        print("3 - Vendas")
        print("0 - Finalizar sistema")
        
        opcao = int(input("Escolha a opção:"))
        return opcao
