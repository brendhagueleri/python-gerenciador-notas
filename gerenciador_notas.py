estudantes = []


def calcular_media(notas: list[float]) -> float:
    """
    Calcula a média das notas de um estudante.

    Argumentos:
    notas (list[float]): Lista de notas do estudante.

    Retornos:
    float: Média calculada das notas. Retorna 0.0 caso a lista esteja vazia.
    """
    if not notas:
        return 0.0

    return sum(notas) / len(notas)


def validar_nota(nota: float) -> float:
    """
    Valida se uma nota está dentro do intervalo permitido.

    Argumentos:
    nota (float): Nota que será validada.

    Retornos:
    float: A própria nota quando estiver entre 0 e 10.

    Exceções:
    ValueError: Quando a nota for menor que 0 ou maior que 10.
    """
    if nota < 0 or nota > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

    return nota


def validar_nome(nome: str) -> str:
    """
    Valida e organiza o nome informado para o estudante.

    Argumentos:
    nome (str): Nome que será validado.

    Retornos:
    str: Nome sem espaços desnecessários no início ou no final.

    Exceções:
    ValueError: Quando o nome estiver vazio ou possuir somente espaços.
    """
    nome_formatado = nome.strip()

    if not nome_formatado:
        raise ValueError("O nome do estudante não pode estar vazio.")

    return nome_formatado


def cadastrar_estudante(
    alunos: list[dict],
    nome: str,
    notas: list[float],
) -> dict:
    """
    Cadastra um novo estudante após validar seu nome e suas notas.

    Argumentos:
    alunos (list[dict]): Lista em que o estudante será cadastrado.
    nome (str): Nome informado para o estudante.
    notas (list[float]): Lista de notas do estudante.

    Retornos:
    dict: Dicionário com o nome e as notas do estudante cadastrado.

    Exceções:
    ValueError: Quando o nome ou alguma nota forem inválidos.
    """
    nome_validado = validar_nome(nome)
    notas_validadas = [validar_nota(nota) for nota in notas]

    novo_estudante = {
        "nome": nome_validado,
        "notas": notas_validadas,
    }

    alunos.append(novo_estudante)

    return novo_estudante


def verificar_aprovacao(media: float, media_minima: float = 7.0) -> str:
    """
    Verifica se o estudante está aprovado ou reprovado com base na média.

    Argumentos:
    media (float): Média final calculada do estudante.
    media_minima (float): Valor mínimo necessário para aprovação.

    Retornos:
    str: Situação do estudante.
    """
    if media >= media_minima:
        return "Aprovado"

    return "Reprovado"


def solicitar_nome() -> str:
    """
    Solicita o nome do estudante até que um valor válido seja informado.
    """
    while True:
        nome = input("Digite o nome do estudante: ")

        try:
            return validar_nome(nome)
        except ValueError as erro:
            print(f"Erro: {erro}")


def solicitar_notas() -> list[float]:
    """
    Solicita as notas do estudante pelo terminal.

    O cadastro termina quando a pessoa pressiona Enter sem digitar uma nota.
    """
    notas = []

    print("\nDigite uma nota por vez.")
    print("Pressione Enter sem digitar nada para finalizar.")

    while True:
        entrada = input(f"Nota {len(notas) + 1}: ").strip()

        if entrada == "":
            if notas:
                return notas

            print("Cadastre pelo menos uma nota.")
            continue

        try:
            nota = float(entrada.replace(",", "."))
        except ValueError:
            print("Erro: digite uma nota numérica.")
            continue

        try:
            notas.append(validar_nota(nota))
        except ValueError as erro:
            print(f"Erro: {erro}")


def cadastrar_estudante_interativo(alunos: list[dict]) -> None:
    """
    Realiza o cadastro de um estudante por meio do terminal.
    """
    print("\n===== CADASTRO DE ESTUDANTE =====")

    nome = solicitar_nome()
    notas = solicitar_notas()

    estudante = cadastrar_estudante(alunos, nome, notas)

    print(f"\nEstudante {estudante['nome']} cadastrado com sucesso!")


def gerar_relatorio(
    alunos: list[dict],
    media_minima_escola: float = 7.0,
) -> None:
    """
    Gera um relatório de desempenho dos estudantes.
    """
    print("\n===== RELATÓRIO DE DESEMPENHO =====")

    if not alunos:
        print("Nenhum estudante cadastrado.")
        return

    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]

        media = calcular_media(notas)
        situacao = verificar_aprovacao(media, media_minima_escola)
        notas_formatadas = ", ".join(
            f"{nota:.1f}" for nota in notas
        )

        print(f"\nEstudante: {nome}")
        print(f"Notas: {notas_formatadas}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("------------------------------")


def exibir_menu() -> None:
    """
    Exibe as opções disponíveis no sistema.
    """
    print("\n===== GERENCIADOR DE NOTAS =====")
    print("1 - Cadastrar estudante")
    print("2 - Visualizar relatório")
    print("3 - Encerrar programa")


def executar_sistema() -> None:
    """
    Mantém o sistema em execução até que a opção de saída seja escolhida.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_estudante_interativo(estudantes)

        elif opcao == "2":
            gerar_relatorio(estudantes)

        elif opcao == "3":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    executar_sistema()