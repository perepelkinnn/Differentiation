import unittest
from diff import *


class TestElementaryFunctions(unittest.TestCase):
    def test_zero(self):
        f = Zero()
        self.assertEqual(str(f.diff()), '0')

    def test_cont(self):
        f = Const(5)
        self.assertEqual(str(f.diff()), '0')

    def test_varriable(self):
        f = Varriable('x')
        self.assertEqual(str(f.diff()), '1')

    def test_power_func_simple_arg(self):
        f = PowerFunc(4, Varriable('x'))
        self.assertEqual(str(f.diff()), '4x^3')

    def test_exponent_func_simple_arg(self):
        f = ExponentFunc(5, Varriable('x'))
        self.assertEqual(str(f.diff()), '(5^x*ln5)')

    def test_ln_simple_arg(self):
        f = ln(Varriable('x'))
        self.assertEqual(str(f.diff()), '1/(x)')

    def test_sin_simple_arg(self):
        f = sin(Varriable('x'))
        self.assertEqual(str(f.diff()), 'cosx')

    def test_cos_simple_arg(self):
        f = cos(Varriable('x'))
        self.assertEqual(str(f.diff()), '-1sinx')


class TestOperations(unittest.TestCase):
    def test_sum(self):
        f = Sum(Varriable('x'), Const(2))
        self.assertEqual(str(f.diff()), '1')

    def test_sub(self):
        f = Sub(Const(2), Varriable('x'))
        self.assertEqual(str(f.diff()), '(-1)')

    def test_mul(self):
        f = Mul(sin(Varriable('x')), cos(Varriable('x')))
        self.assertEqual(str(f.diff()), '((cosx*cosx)+(sinx*-1sinx))')

    def test_div(self):
        f = Div(Const(1), Varriable('x'))
        self.assertEqual(str(f.diff()), '(((0-1))/((x*x)))')
