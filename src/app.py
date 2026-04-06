gastos = []

def adicionar_gasto(valor, descricao):
    if valor <= 0:
        return "Valor inválido"
    
    gastos.append({
        "valor": valor,
        "descricao": descricao
    })
    return "Gasto adicionado com sucesso"

def calcular_total():
    return sum(gasto["valor"] for gasto in gastos)

def listar_gastos():
    return gastos