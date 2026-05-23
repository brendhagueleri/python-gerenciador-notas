# Sistema de Gerenciamento de Notas

Sistema simples desenvolvido em Python para registrar estudantes, calcular médias, verificar aprovação e gerar um relatório de desempenho no terminal.

Este projeto foi criado como parte dos meus estudos em lógica de programação, estruturas de dados, funções, documentação e testes unitários.

---

## Objetivo

O objetivo do projeto é simular um sistema básico de gerenciamento acadêmico, permitindo trabalhar com dados de estudantes e aplicar regras simples de aprovação.

---

## Funcionalidades

- Armazenamento de estudantes em uma lista de dicionários.
- Registro de nome e notas de cada estudante.
- Cálculo da média individual.
- Verificação da situação do estudante como "Aprovado" ou "Reprovado".
- Geração de relatório no terminal.
- Tratamento de lista de notas vazia, retornando média `0.0`.
- Testes unitários para validar as principais regras do sistema.

---

## Tecnologias utilizadas

- Python
- unittest

---

## Estrutura do projeto

- `gerenciador_notas.py`: arquivo principal com os dados, funções de cálculo, verificação e relatório.
- `test_notas.py`: arquivo com testes unitários das funções principais.
- `README.md`: documentação do projeto.

---

## Como executar o projeto

No terminal, execute:

`python gerenciador_notas.py`

O sistema exibirá um relatório com o nome do estudante, a média calculada e a situação final.

---

## Como executar os testes

No terminal, execute:

`python -m unittest test_notas.py`

Os testes verificam:

- cálculo correto da média;
- comportamento com lista de notas vazia;
- aprovação com média padrão;
- reprovação com média abaixo do mínimo;
- aprovação com média mínima customizada;
- comportamento com média mínima igual a `0.0`.

---

## Conceitos praticados

- Listas e dicionários;
- Funções com responsabilidade única;
- Type hints;
- Docstrings;
- Condicionais;
- Laços de repetição;
- Testes unitários;
- Organização de projeto;
- Documentação técnica.

---

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei a separação de responsabilidades entre funções, a documentação do código com docstrings e a criação de testes para validar regras de negócio simples.

Também foi trabalhado o tratamento de um caso extremo: quando um estudante ainda não possui notas cadastradas. Nesse cenário, a função de cálculo retorna `0.0`, evitando erro de divisão por zero e deixando o sistema mais previsível.

---

## Status

Projeto finalizado como exercício acadêmico e adaptado para portfólio no GitHub.
