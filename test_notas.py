import unittest

from gerenciador_notas import (
    calcular_media,
    validar_nome,
    validar_nota,
    verificar_aprovacao,
)


class TestGerenciadorNotas(unittest.TestCase):
    """Testes unitários para validar as funções do sistema de notas."""

    def test_calcular_media_lista_preenchida(self):
        """Garante que a média é calculada corretamente com uma lista de notas válidas."""
        notas = [8.0, 7.0, 9.0]
        resultado = calcular_media(notas)
        self.assertAlmostEqual(resultado, 8.0)

    def test_calcular_media_lista_vazia(self):
        """Garante que uma lista vazia de notas retorne 0.0."""
        notas = []
        resultado = calcular_media(notas)
        self.assertEqual(resultado, 0.0)

    def test_verificar_aprovacao_aprovado(self):
        """Testa se médias maiores ou iguais a 7.0 retornam 'Aprovado'."""
        self.assertEqual(verificar_aprovacao(7.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(9.5), "Aprovado")

    def test_verificar_aprovacao_reprovado(self):
        """Testa se médias menores que 7.0 retornam 'Reprovado'."""
        self.assertEqual(verificar_aprovacao(6.9), "Reprovado")
        self.assertEqual(verificar_aprovacao(0.0), "Reprovado")

    def test_verificar_aprovacao_media_customizada(self):
        """Testa a aprovação usando uma média mínima diferente do padrão."""
        self.assertEqual(
            verificar_aprovacao(6.5, media_minima=6.0),
            "Aprovado",
        )
        self.assertEqual(
            verificar_aprovacao(5.9, media_minima=6.0),
            "Reprovado",
        )

    def test_verificar_aprovacao_media_minima_zero(self):
        """Testa o comportamento da aprovação quando a média mínima é 0.0."""
        resultado = verificar_aprovacao(0.0, media_minima=0.0)
        self.assertEqual(resultado, "Aprovado")

    def test_validar_nota_valida(self):
        """Testa notas válidas, incluindo os limites 0 e 10."""
        self.assertEqual(validar_nota(0.0), 0.0)
        self.assertEqual(validar_nota(7.5), 7.5)
        self.assertEqual(validar_nota(10.0), 10.0)

    def test_validar_nota_invalida(self):
        """Garante que notas menores que 0 ou maiores que 10 sejam rejeitadas."""
        with self.assertRaises(ValueError):
            validar_nota(-0.1)

        with self.assertRaises(ValueError):
            validar_nota(10.1)

    def test_validar_nome_valido(self):
        """Testa um nome válido e remove espaços desnecessários."""
        self.assertEqual(validar_nome("Ana"), "Ana")
        self.assertEqual(validar_nome("  Bruno  "), "Bruno")

    def test_validar_nome_vazio(self):
        """Garante que nomes vazios ou formados apenas por espaços sejam rejeitados."""
        with self.assertRaises(ValueError):
            validar_nome("")

        with self.assertRaises(ValueError):
            validar_nome("   ")


if __name__ == "__main__":
    unittest.main()