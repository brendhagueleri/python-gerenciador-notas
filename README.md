# Sistema de Gerenciamento de Notas

Sistema desenvolvido em **Python** para cadastrar estudantes, registrar notas, calcular médias e gerar relatórios de desempenho diretamente pelo terminal.

O projeto começou como um exercício de lógica de programação e foi sendo aprimorado conforme avancei nos estudos. A versão atual possui interação com o usuário, validações de dados, separação de responsabilidades em funções e testes unitários para as principais regras do sistema.

---

## Funcionalidades

O sistema permite:

- Cadastrar estudantes pelo terminal
- Registrar uma ou mais notas para cada estudante
- Aceitar notas com ponto ou vírgula, como `7.5` ou `7,5`
- Validar nomes vazios
- Validar notas entre `0` e `10`
- Impedir o cadastro de estudantes sem notas
- Calcular automaticamente a média
- Identificar a situação como **Aprovado** ou **Reprovado**
- Exibir relatório com estudantes, notas, média e situação
- Manter o programa em execução por meio de um menu interativo
- Tratar entradas inválidas sem encerrar o sistema inesperadamente

---

## Menu do sistema

Ao executar o programa, o seguinte menu é apresentado:

```text
===== GERENCIADOR DE NOTAS =====
1 - Cadastrar estudante
2 - Visualizar relatório
3 - Encerrar programa
```

O usuário pode cadastrar diferentes estudantes antes de visualizar o relatório.

---

## Exemplo de uso

Durante o cadastro:

```text
===== CADASTRO DE ESTUDANTE =====
Digite o nome do estudante: Brendha

Digite uma nota por vez.
Pressione Enter sem digitar nada para finalizar.

Nota 1: 8
Nota 2: 7,5
Nota 3: 9
Nota 4:

Estudante Brendha cadastrado com sucesso!
```

Ao visualizar o relatório:

```text
===== RELATÓRIO DE DESEMPENHO =====

Estudante: Brendha
Notas: 8.0, 7.5, 9.0
Média: 8.17
Situação: Aprovado
------------------------------
```

---

## Regras do sistema

### Nome do estudante

O nome:

- não pode estar vazio;
- não pode conter somente espaços;
- tem espaços extras removidos no início e no final.

### Notas

Cada nota:

- deve ser numérica;
- deve estar entre `0` e `10`;
- pode utilizar ponto ou vírgula como separador decimal.

Também é necessário cadastrar pelo menos uma nota para cada estudante.

### Aprovação

Por padrão:

- **Aprovado:** média maior ou igual a `7.0`
- **Reprovado:** média menor que `7.0`

A função responsável pela verificação também permite utilizar uma média mínima personalizada.

---

## Estrutura do projeto

```text
python-gerenciador-notas/
├── .gitignore
├── gerenciador_notas.py
├── test_notas.py
└── README.md
```

### `gerenciador_notas.py`

Contém as regras e o fluxo principal do sistema:

- cálculo de média;
- validação de nome;
- validação de notas;
- cadastro de estudantes;
- verificação de aprovação;
- entrada de dados;
- geração de relatório;
- menu interativo.

### `test_notas.py`

Contém os testes unitários utilizados para validar as principais regras do sistema.

---

## Testes

O projeto possui atualmente **15 testes unitários** utilizando a biblioteca `unittest` do Python.

Os testes verificam cenários como:

- cálculo correto da média;
- comportamento com lista de notas vazia;
- aprovação e reprovação;
- média mínima personalizada;
- notas nos limites `0` e `10`;
- notas abaixo de `0` ou acima de `10`;
- nomes válidos;
- nomes vazios;
- cadastro válido de estudante;
- tentativa de cadastro com nota inválida;
- tentativa de cadastro sem notas;
- relatório sem estudantes;
- conteúdo do relatório com estudante cadastrado.

Para executar os testes:

```bash
python -m unittest -v
```

Resultado esperado:

```text
Ran 15 tests

OK
```

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/brendhagueleri/python-gerenciador-notas.git
```

### 2. Acesse a pasta

```bash
cd python-gerenciador-notas
```

### 3. Execute o programa

```bash
python gerenciador_notas.py
```

Não é necessário instalar bibliotecas externas.

---

## Tecnologias e conceitos praticados

- Python
- `unittest`
- Funções
- Estruturas condicionais
- Laços de repetição
- Listas
- Dicionários
- Type hints
- Docstrings
- Tratamento de exceções
- Validação de dados
- Entrada e saída pelo terminal
- Separação de responsabilidades
- Testes unitários
- Git e GitHub
- Documentação de projeto

---

## Evolução do projeto

Este projeto começou com uma estrutura simples para cálculo de médias e geração de relatório.

Com o avanço dos estudos, fui voltando ao código e adicionando novas melhorias:

1. cadastro interativo de estudantes;
2. entrada dinâmica de notas;
3. validação de nomes;
4. validação de notas;
5. tratamento de entradas inválidas;
6. menu interativo;
7. proteção das regras de cadastro;
8. ampliação dos testes unitários;
9. melhoria da documentação.

Mais do que adicionar funcionalidades, a proposta dessa evolução foi praticar como regras simples podem ser separadas, testadas e organizadas para deixar o código mais previsível e fácil de manter.

---

## Status

✅ **Versão atual concluída e testada.**

O projeto continua aberto para futuras melhorias conforme novos conceitos forem estudados.