import unittest
import Calcular as c

class TestCalculadora(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')

    def setUp(self):
        print('setUp -> OK')

    def test_suma(self):
        result = c.sumar(8,78)
        self.assertEqual(result, 86)
        print('testSuma() -> OK')

    def test_resta(self):
        result = c.restar(10, 5)
        self.assertEqual(result, 5)
        print('testResta() -> OK')

    def test_doblar(self):
        result = c.doblar(4)
        self.assertEqual(result,8)
        print('testDoblar() -> OK')

    def test_multiplicar(self):
        result = c.multiplicar(3,8)
        self.assertEqual(result, 24)
        print('testMultiplicar() -> OK')

    def test_dividir(self):
        result = c.dividir(20,2)
        self.assertEqual(result, 10)
        print('testDividir() -> OK')

    def test_cuadrado(self):
        result = c.cuadrado(4)
        self.assertEqual(result, 16)
        print('testCuadrado() -> OK')

    def test_raiz(self):
        result = c.raiz(144)
        self.assertEqual(result, 12)
        print('testRaiz() -> OK')

    def test_es_par(self):
        result = c.es_par(8)
        self.assertEqual(result, 1)
        print('testEs_par() -> OK')

    def tearDown(self):
        print('tearDown() -> OK')

if __name__ == '__main__':
    unittest.main()