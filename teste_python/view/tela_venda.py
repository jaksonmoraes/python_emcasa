
class TelaVenda:
    def tela_opcoes(self):
        print("----- TELA VENDA -----")
        print("Qual sua opcao")
        print("1 - Listar carros")
        print("0 - Retornar")

        opcao = int(input("Qual sua opção na tela de vendas: "))
        return opcao
    
    def mostra_carros(self, dados_carro):
        print("Nome da pessoa: ", dados_pessoa["nome"])
        print("CPF: ", dados_pessoa["cpf"])
        print("\n")