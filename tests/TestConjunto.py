import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_promedio_un_numero(self):
        c = Conjunto()
        c.agregar_numero(10)
        self.assertEqual(c.calcular_promedio(), 10)

    def test_promedio_varios_numeros(self):
        c = Conjunto()
        for n in [2, 4, 6, 8]:
            c.agregar_numero(n)
        self.assertEqual(c.calcular_promedio(), 5)

if __name__ == '__main__':
    unittest.main()