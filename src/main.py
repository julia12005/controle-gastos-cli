from src.app import adicionar_gasto, calcular_total, listar_gastos
from src.api_cotacao import buscar_cotacao_dolar, converter_dolar_para_real

def menu():
    while True:
        print("\n--- CONTROLE DE GASTOS ---")
        print("1 - Adicionar gasto")
        print("2 - Ver total")
        print("3 - Listar gastos")
        print("4 - Consultar cotação do dólar")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Valor: "))
            descricao = input("Descrição: ")
            print(adicionar_gasto(valor, descricao))

        elif opcao == "2":
            print(f"Total: R$ {calcular_total()}")

        elif opcao == "3":
            for g in listar_gastos():
                print(g)

        elif opcao == "4":
            try:
                cotacao = buscar_cotacao_dolar()
                print(f"Cotação atual do dólar: US$ 1,00 = R$ {cotacao:.2f}")

                valor = float(input("Digite um valor em dólar para converter: "))
                convertido = converter_dolar_para_real(valor)

                print(f"US$ {valor:.2f} equivale a R$ {convertido:.2f}")
            except Exception as erro:
                print(f"Erro ao consultar cotação: {erro}")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()