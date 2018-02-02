import unittest
import calc

class TestCalc(unittest.TestCase):

    #Naming convention is required, it will only run the function if it starts with test
    def test_add(self):
        #result = calc.add(10,15)
        self.assertEquals(calc.add(10,15),25)
        self.assertEquals(calc.add(10,4),14)
        self.assertEquals(calc.add(1,-3),-2)

    def test_subtract(self):
        #result = calc.subtract(10,15)
        self.assertEquals(calc.subtract(10,15),-5)
        self.assertEquals(calc.subtract(10,4),6)
        self.assertEquals(calc.subtract(1,-3),4)

    def test_divide(self):
        #result = calc.divide(10,15)
        self.assertEquals(calc.divide(4,2),2)
        self.assertEquals(calc.divide(10,4),2.5)
        self.assertEquals(calc.divide(3,4),0.75)
        with self.assertRaises(ValueError):
        	calc.divide(10,0)

if __name__ == "__main__":
    unittest.main()
