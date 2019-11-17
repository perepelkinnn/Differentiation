import unittest
from diff import *


def take_derivative(func):
    return str(func.diff())


class TestElementaryFunctions(unittest.TestCase):
    def test_cont(self):
        f = Const(5)
        self.assertEqual(take_derivative(f), '0')

    def test_varriable(self):
        f = Varriable()
        self.assertEqual(take_derivative(f), '1')

    def test_power_func_simple_arg(self):
        f = PowerFunc(4, Varriable())
        self.assertEqual(take_derivative(f), '4*x^3')

    def test_exponent_func_simple_arg(self):
        f = ExponentFunc(5, Varriable())
        self.assertEqual(take_derivative(f), '5^x*ln5')

    def test_ln_simple_arg(self):
        f = Ln(Varriable())
        self.assertEqual(take_derivative(f), '1/x')

    def test_sin_simple_arg(self):
        f = Sin(Varriable())
        self.assertEqual(take_derivative(f), 'cosx')

    def test_cos_simple_arg(self):
        f = Cos(Varriable())
        self.assertEqual(take_derivative(f), '-1*sinx')


class TestOperations(unittest.TestCase):
    def test_sum(self):
        f = Sum(Varriable(), Const(2))
        self.assertEqual(take_derivative(f), '1+0')

    def test_sub(self):
        f = Sub(Const(2), Varriable())
        self.assertEqual(take_derivative(f), '0-1')

    def test_mul(self):
        f = Mul(Sin(Varriable()), Cos(Varriable()))
        self.assertEqual(take_derivative(f), 'cosx*cosx+sinx*-1*sinx')

    def test_div(self):
        f = Div(Const(1), Varriable())
        self.assertEqual(take_derivative(f), '0*x-1*1/x*x')


if __name__ == '__main__':
    unittest.main()
