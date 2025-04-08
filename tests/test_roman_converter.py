import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    
    # Pruebas de números simples
    def test_unidades(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(3), "III")

    # Pruebas con reglas de sustracción
    def test_sustraccion(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")

    # Pruebas de decenas
    def test_decenas(self):
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(20), "XX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(50), "L")

    # Números con varios símbolos mezclados
    def test_varios_simbolos(self):
        self.assertEqual(decimal_to_roman(58), "LVIII")
        self.assertEqual(decimal_to_roman(93), "XCIII")
        self.assertEqual(decimal_to_roman(141), "CXLI")
    
    # Máximo valor permitido
    def test_maximo(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

if __name__ == "__main__":
    unittest.main()
