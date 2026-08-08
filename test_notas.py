import unittest

from gerenciador_notas import (
    cadastrar_estudante,
    calcular_media,
    validar_nome,
    validar_nota,
    verificar_aprovacao,
)


class TestGerenciadorNotas(unittest.TestCase):
    """Testes unitários para validar as funções do sistema de notas."""

    def test_calcular_media_lista_preenchida(self):
        """Garante que a média seja calculada corretamente."""
        notas = [8.0, 7.0, 9.0]
        resultado = calcular_media(notas)
        self.assertAlmostEqual(resultado, 8.0)

    def test_calcular_media_lista_vazia(self):
        """Garante que uma lista vazia de notas retorne 0.0."""
        notas = []
        resultado = calcular_media(notas)
        self.assertEqual(resultado, 0.0)

    def test_verificar_aprovacao_aprovado(self):
        """Testa se médias maiores ou iguais a 7.0 retornam Aprovado."""
        self.assertEqual(verificar_aprovacao(7.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(9.5), "Aprovado")

    def test_verificar_aprovacao_reprovado(self):
        """Testa se médias menores que 7.0 retornam Reprovado."""
        self.assertEqual(verificar_aprovacao(6.9), "Reprovado")
        self.assertEqual(verificar_aprovacao(0.0), "Reprovado")

    def test_verificar_aprovacao_media_customizada(self):
        """Testa a aprovação com uma média mínima personalizada."""
        self.assertEqual(
            verificar_aprovacao(6.5, media_minima=6.0),
            "Aprovado",
        )
        self.assertEqual(
            verificar_aprovacao(5.9, media_minima=6.0),
            "Reprovado",
        )

    def test_verificar_aprovacao_media_minima_zero(self):
        """Testa a aprovação quando a média mínima é 0.0."""
        resultado = verificar_aprovacao(0.0, media_minima=0.0)
        self.assertEqual(resultado, "Aprovado")

    def test_validar_nota_valida(self):
        """Testa notas válidas, incluindo os limites 0 e 10."""
        self.assertEqual(validar_nota(0.0), 0.0)
        self.assertEqual(validar_nota(7.5), 7.5)
        self.assertEqual(validar_nota(10.0), 10.0)

    def test_validar_nota_invalida(self):
        """Garante que notas fora do intervalo sejam rejeitadas."""
        with self.assertRaises(ValueError):
            validar_nota(-0.1)

        with self.assertRaises(ValueError):
            validar_nota(10.1)

    def test_validar_nome_valido(self):
        """Testa um nome válido e remove espaços desnecessários."""
        self.assertEqual(validar_nome("Ana"), "Ana")
        self.assertEqual(validar_nome("  Bruno  "), "Bruno")

    def test_validar_nome_vazio(self):
        """Garante que nomes vazios ou formados por espaços sejam rejeitados."""
        with self.assertRaises(ValueError):
            validar_nome("")

        with self.assertRaises(ValueError):
            validar_nome("   ")

    def test_cadastrar_estudante_valido(self):
        """Garante que um estudante válido seja adicionado à lista."""
        alunos = []

        estudante = cadastrar_estudante(
            alunos,
            "  Brendha  ",
            [8.0, 9.0, 7.5],
        )

        self.assertEqual(estudante["nome"], "Brendha")
        self.assertEqual(estudante["notas"], [8.0, 9.0, 7.5])
        self.assertEqual(len(alunos), 1)
        self.assertEqual(alunos[0], estudante)

    def test_cadastrar_estudante_com_nota_invalida(self):
        """Garante que um estudante com nota inválida não seja cadastrado."""
        alunos = []

        with self.assertRaises(ValueError):
            cadastrar_estudante(
                alunos,
                "Ana",
                [8.0, 11.0],
            )

        self.assertEqual(alunos, [])


if __name__ == "__main__":
    unittest.main()