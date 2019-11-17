from tree import Node


class Sum(Node):
    def __init__(self, u, v):
        super().__init__(u, v)

    def __str__(self):
        return '({}+{})'.format(self.left, self.right)

    def diff(self):
        return Sum(self.left.diff(), self.right.diff())


class Sub(Node):
    def __init__(self, u, v):
        super().__init__(u, v)

    def __str__(self):
        return '({}-{})'.format(self.left, self.right)

    def diff(self):
        return Sub(self.left.diff(), self.right.diff())


class Mul(Node):
    def __init__(self, u, v):
        super().__init__(u, v)

    def __str__(self):
        return '({}*{})'.format(self.left, self.right)

    def diff(self):
        return Sum(Mul(self.left.diff(), self.right), Mul(self.left, self.right.diff()))


class Div(Node):
    def __init__(self, u, v):
        super().__init__(u, v)

    def __str__(self):
        return '({}/{})'.format(self.left, self.right)

    def diff(self):
        return Div(Sub(
            Mul(self.left.diff(), self.right),
            Mul(self.left, self.right.diff())),
            Mul(self.right, self.right))


class Const:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{}'.format(self.value)

    def diff(self):
        return Const(0)


class Varriable:
    def __init__(self, char='x'):
        self.char = char

    def __str__(self):
        return '{}'.format(self.char)

    def diff(self):
        return Const(1)


class PowerFunc:
    def __init__(self, power, arg):
        self.power = power
        self.arg = arg

    def __str__(self):
        return '({})^({})'.format(self.arg, self.power)

    def diff(self):
        if type(self.arg) is Const:
            return Const(0)
        return Mul(Const(self.power),
                   PowerFunc(self.power - 1,  self.arg))


class ExponentFunc:
    def __init__(self, base, arg):
        self.base = base
        self.arg = arg

    def __str__(self):
        return '({})^({})'.format(self.base, self.arg)

    def diff(self):
        if type(self.arg) is Const:
            return Const(0)
        return Mul(self, Ln(self.base))


class Ln:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'ln({})'.format(self.arg)

    def diff(self):
        if type(self.arg) is Const:
            return Const(0)
        return Div(Const(1), self.arg)


class Sin:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'sin({})'.format(self.arg)

    def diff(self):
        if type(self.arg) is Const:
            return Const(0)
        return Cos(self.arg)


class Cos:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'cos({})'.format(self.arg)

    def diff(self):
        if type(self.arg) is Const:
            return Const(0)
        return Mul(Const(-1), Sin(self.arg))


class ComplexFunc:
    def __init__(self, func):
        self.func = func

    def __str__(self):
        return '{}'.format(self.func)

    def diff(self):
        return Mul(self.func.diff(), self.func.arg.diff())
