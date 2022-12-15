class TelaCarro:
    def tela_opcoes(self):
        print("----- CARRO -----")
        print("Qual sua opcao")
        print("1 - Incluir carro")
        print("2 - Alterar carro")
        print("3 - Listar carro")
        print("4 - Excluir carro")
        print("0 - Retornar")
    
        opcao = int(input("Qual sua opcao na tela carro: "))
        return opcao
    
    def pega_dados_carro(self):
        print("------ Dados do veiculo ------")
        modelo = input("Modelo: ")
        placa = input("PLACA: ")
    
        return {"modelo": modelo, "placa": placa}
    
    def mostra_carro(self, dados_carro):
        print("Modelo do carro: ", dados_carro["modelo"])
        print("Placa do veiculo: ", dados_carro["placa"])
        print("\n")
    
    def seleciona_carro(self):
        placa = input("Placa do carro a ser buscado: ")
        return placa
    
    def mostra_mensagem(self, msg):
        print(msg)