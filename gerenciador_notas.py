estudantes = [
    {
        "nome": "Ana",
        "notas": [8.5, 7.0, 9.0]
    },
    {
        "nome": "Bruno",
        "notas": [6.0, 5.5, 7.0]
    },
    {
        "nome": "Carla",
        "notas": [9.5, 8.0, 10.0]
    },
    {
        "nome": "Diego",
        "notas": []
    }
]


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


def verificar_aprovacao(media: float, media_minima: float = 7.0) -> str:
    """
    Verifica se o estudante está aprovado ou reprovado com base na média.

    Argumentos:
    media (float): Média final calculada do estudante.
    media_minima (float): Valor mínimo necessário para aprovação. O padrão é 7.0.

    Retornos:
    str: Retorna "Aprovado" se a média for maior ou igual à média mínima,
    ou "Reprovado" caso contrário.
    """
    if media >= media_minima:
        return "Aprovado"

    return "Reprovado"


def gerar_relatorio(alunos: list[dict], media_minima_escola: float = 7.0) -> None:
    """
    Gera um relatório de desempenho dos estudantes.

    Argumentos:
    alunos (list[dict]): Lista de dicionários contendo nome e notas dos estudantes.
    media_minima_escola (float): Média mínima usada para definir aprovação.

    Retornos:
    None: A função não retorna valor, apenas imprime o relatório no terminal.
    """
    print("===== RELATÓRIO DE DESEMPENHO =====")

    for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]

        media = calcular_media(notas)
        situacao = verificar_aprovacao(media, media_minima_escola)

        print(f"Aluno: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("------------------------------")


if __name__ == "__main__":
    gerar_relatorio(estudantes, media_minima_escola=7.0)