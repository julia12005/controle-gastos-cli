from src.app import adicionar_gasto, calcular_total, gastos

def test_adicionar_gasto():
    gastos.clear()
    resultado = adicionar_gasto(10, "Lanche")
    assert resultado == "Gasto adicionado com sucesso"
    assert len(gastos) == 1

def test_valor_invalido():
    gastos.clear()
    resultado = adicionar_gasto(-5, "Erro")
    assert resultado == "Valor inválido"

def test_calcular_total():
    gastos.clear()
    adicionar_gasto(10, "A")
    adicionar_gasto(20, "B")
    assert calcular_total() == 30

def test_valor_invalido():
    resultado = adicionar_gasto(-10, "erro")
    assert resultado == "Valor inválido"