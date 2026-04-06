from src.app import adicionar_gasto, calcular_total, listar_gastos

def menu():
    while True:
        print("\n--- CONTROLE DE GASTOS ---")
        print("1 - Adicionar gasto")
        print("2 - Ver total")
        print("3 - Listar gastos")
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

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()