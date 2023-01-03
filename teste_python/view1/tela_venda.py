
class TelaVenda:
    def tela_opcoes(self):
        print("----- TELA VENDA -----")
        print("Qual sua opcao")
        print("1 - Listar carros")
        print("0 - Retornar")

        opcao = int(input("Qual sua opção na tela de vendas: "))
        return opcao
    
    def mostra_carros(self, dados_carro):
        print("Modelo do carro: ", dados_carro["modelo"])
        print("PLACA: ", dados_carro["placa"])
        print("\n")
