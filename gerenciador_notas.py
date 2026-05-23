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
