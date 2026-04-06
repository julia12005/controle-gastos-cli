# Controle de Gastos CLI

[![CI Python](https://github.com/julia12005/controle-gastos-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/julia12005/controle-gastos-cli/actions/workflows/ci.yml)

## Nome do Projeto 
Controle de Gastos CLI

## Descrição

Aplicação simples em Python para controle de gastos pessoais via linha de comando (CLI).
Permite registrar despesas e visualizar o total gasto, ajudando no controle financeiro do dia a dia.

## Demonstração

### Sistema funcionando
![Sistema rodando](assets/sistema.png)

### Testes e qualidade de código
![Testes e lint](assets/testes.png)

---

## Problema

Muitas pessoas têm dificuldade em controlar seus gastos diários, o que pode levar a desorganização financeira e dívidas.

---

## Solução

Este projeto oferece uma forma simples e rápida de registrar gastos diretamente pelo terminal, sem necessidade de aplicativos complexos.

---

## Público-Alvo
- Estudantes, profissionais e qualquer pessoa que deseja organizar suas finanças pessoais.  
- Usuários que preferem soluções leves, sem aplicativos complexos.

---

## Funcionalidades

- Adicionar gasto com descrição e valor.  
- Listar todos os gastos registrados.  
- Consultar total de gastos.  
- Validação de entradas inválidas (ex: valor negativo ou campo vazio).

---

## Tecnologias utilizadas

* Python 3.11
* Pytest (testes automatizados)
* Ruff (linting de código)
* GitHub Actions (CI/CD)

---

## Estrutura do Projeto

```
controle-gastos-cli/
│
├── src/                # Código principal
│   ├── app.py
│   ├── main.py
|   └── __init__.py
│
├── tests/              # Testes automatizados
│   └── test_app.py
│
├── .github/workflows/  # CI (GitHub Actions)
│   └── ci.yml
|
├── assets/                # Print do código funcionando
│   ├── sistema.png
|   └── testes.png
│
├── README.md
├── requirements.txt
├── .gitignore
├── pytest.ini
├── ruff.toml
├── CHANGELOG.md
├── LICENSE
└── VERSION
```

---
## 📦 Requisitos e Dependências
- Python 3.11+  
- Instalar dependências:  
```bash
pip install -r requirements.txt
```
---

## Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/julia12005/controle-gastos-cli.git
cd controle-gastos-cli
```

---

### 2. Criar ambiente virtual (opcional, recomendado)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 4. Executar aplicação

```
python -m src.main
```

---
## Exemplos de Uso

### Adicionar gasto

```bash
> python -m src.main add
Escolha: 1
valor: 12.50
descrição: Lanche
Gasto adicionado com sucesso!
```

### Listar gastos

```bash
Escolha: 3
{'valor': 12.5, 'descricao': 'lanche'}
```

### Ver total

```bash
Escolha: 2
Total: R$ 12.5
```

---

## Rodar todos os testes

```
pytest
```

Testes cobrem:

* Caminho feliz: adicionar gasto válido
* Entrada inválida: valores negativos ou vazios
* Caso limite: soma de múltiplos gastos

---

## Rodar lint (verificação de código)

```
ruff check .
```

---

## Integração Contínua (CI)

O projeto utiliza GitHub Actions para:

* Rodar testes automaticamente
* Verificar qualidade do código com Ruff

---

## Versionamento Semântico

- Versão atual: 1.0.0
- Arquivo: VERSION
- Formato MAJOR.MINOR.PATCH:
 - MAJOR: mudanças grandes ou incompatíveis
 - MINOR: novas funcionalidades compatíveis
 - PATCH: correções menores

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE.

---

## Melhorias futuras

* Interface gráfica (GUI)
* Persistência de dados (salvar em arquivo ou banco de dados)
* Categorias de gastos
* Relatórios mensais

---

## Autora

Projeto desenvolvido por **Julia** como parte do bootcamp.

---

## Link do Repositório

https://github.com/julia12005/controle-gastos-cli
