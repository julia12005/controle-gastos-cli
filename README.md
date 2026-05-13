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
## Novidades da Entrega Intermediária

- Integração com API pública de cotação USD-BRL.
- Consulta da cotação atual do dólar.
- Conversão de valores em dólar para reais.
- Testes de integração automatizados.
- Evolução utilizando GitHub Issues, Branches e Pull Requests.
- Publicação do projeto via GitHub Pages.

---

## Deploy

Acesse a aplicação publicada:

https://julia12005.github.io/controle-gastos-cli/

---

## Funcionalidades

- Adicionar gasto com descrição e valor.  
- Listar todos os gastos registrados.  
- Consultar total de gastos.  
- Validação de entradas inválidas (ex: valor negativo ou campo vazio).
- Consultar cotação atual do dólar.
- Converter valores em dólar para reais.

---

## Tecnologias utilizadas

* Python 3.11
* Pytest (testes automatizados)
* Ruff (linting de código)
* GitHub Actions (CI/CD)

---

## API Utilizada

O projeto utiliza a API pública AwesomeAPI para consulta de cotação de moedas em tempo real.

Endpoint utilizado:

https://economia.awesomeapi.com.br/json/last/USD-BRL

---

## Estrutura do Projeto

```
controle-gastos-cli/
│
├── src/                # Código principal
│   ├── app.py
│   ├── main.py
|   ├── api_cotacao.py
|   └── __init__.py
│
├── tests/              # Testes automatizados
│   ├── test_app.py
|   └── test_api_cotacao.py
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

### 3. Executar aplicação

```
python -m src.main
```

---
## Exemplos de Uso

### Adicionar gasto

```bash
> python -m src.main
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
### Consultar cotação do dolar

```bash
Escolha: 4
{Cotação atual do dólar: US$ 1,00 = R$ 5.02
Digite um valor em dólar para converter: 10
US$ 10.00 equivale a R$ 50.25}
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
* Integração com API pública de cotação
* Conversão de dólar para real

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

- Versão atual: 1.1.0
- Arquivo: VERSION
- Formato MAJOR.MINOR.PATCH:
 - MAJOR: mudanças grandes ou incompatíveis
 - MINOR: novas funcionalidades compatíveis
 - PATCH: correções menores

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE.

---

## Fluxo de Desenvolvimento

Nesta entrega intermediária, o desenvolvimento foi realizado seguindo práticas utilizadas no mercado:

- Criação de Issue no GitHub
- Desenvolvimento em branch separada
- Integração com API pública
- Testes automatizados
- Integração contínua com GitHub Actions
- Pull Request para merge na branch principal

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
