import unittest
import funciones_Cristinarey as funciones

class testCalculos(unittest.TestCase):
    def test_Multiplo(self):
        self.assertEqual(funciones.esMultiplo(25,20),5)
    
    def test_Max(self):
        self.assertTrue(funciones.calcularMax([1,4,6,9]) == 9)
    
    def test_Min(self):
        self.assertFalse(funciones.calcularMin([2,7,5,3]) == 7)
    
    def test_Mcm(self):
        self.assertNotEqual(funciones.minimoComunMultiplo(10,2),2)
    
    def test_duplicar(self):
        self.assertGreater(funciones.duplicar(5),5)
      
 

    






if __name__== '__main__':
    unittest.main()