# Sistema de Gerenciamento de Notas

Sistema desenvolvido em **Python** para cadastrar estudantes, registrar notas, calcular médias e gerar relatórios de desempenho diretamente pelo terminal.

O projeto começou como um exercício de lógica de programação e foi sendo aprimorado conforme avancei nos estudos. A versão atual possui interação com o usuário, validações de dados, separação das responsabilidades em funções e testes unitários para as principais regras do sistema.

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
- Exibir um relatório com estudantes, notas, média e situação
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