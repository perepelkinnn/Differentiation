class Sum:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __str__(self):
        if type(self.u) is Zero and type(self.v) is Zero:
            return '{}'.format(0)
        elif type(self.u) is Zero:
            return '{}'.format(self.v)
        elif type(self.v) is Zero:
            return '{}'.format(self.u)
        if type(self.u) is Const and type(self.v) is Const:
            return '{}'.format(self.u.value + self.v.value)
        return '({}+{})'.format(self.u, self.v)

    def diff(self):
        return Sum(self.u.diff(), self.v.diff())


class Sub:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __str__(self):
        if type(self.u) is Zero and type(self.v) is Zero:
            return '{}'.format(0)
        elif type(self.u) is Zero:
            return '(-{})'.format(self.v)
        elif type(self.v) is Zero:
            return '{}'.format(self.u)
        if type(self.u) is Const and type(self.v) is Const:
            return '{}'.format(self.u.value - self.v.value)
        return '({}-{})'.format(self.u, self.v)

    def diff(self):
        return Sub(self.u.diff(), self.v.diff())


class Mul:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __str__(self):
        if type(self.u) is Zero or type(self.v) is Zero:
            return '{}'.format(0)
        if type(self.u) is Const and type(self.v) is Const:
            return '{}'.format(self.u.value * self.v.value)
        elif type(self.u) is Const:
            return '{}{}'.format(self.u, self.v)
        elif type(self.v) is Const:
            return '{}{}'.format(self.v, self.u)
        return '({}*{})'.format(self.u, self.v)

    def diff(self):
        return Sum(Mul(self.u.diff(), self.v), Mul(self.u, self.v.diff()))


class Div:
    def __init__(self, u, v):
        if type(v) is Zero:
            raise ZeroDivisionError
        self.u = u
        self.v = v

    def __str__(self):
        if type(self.u) is Zero:
            return '{}'.format(0)
        if type(self.u) is Const and type(self.v) is Const:
            return '{}'.format(self.u.value / self.v.value)
        elif type(self.u) is Const:
            return '{}/({})'.format(self.u, self.v)
        elif type(self.v) is Const:
            return '({})/{}'.format(self.u, self.v)
        return '(({})/({}))'.format(self.u, self.v)

    def diff(self):
        return Div(Sub(
            Mul(self.u.diff(), self.v),
            Mul(self.u, self.v.diff())),
            Mul(self.v, self.v))


class Zero:
    def __str__(self):
        return '{}'.format(0)

    def diff(self):
        return Zero()


class Const:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{}'.format(self.value)

    def diff(self):
        return Zero()


class Varriable:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return '{}'.format(self.char)

    def diff(self):
        return Const(1)


class PowerFunc:
    def __init__(self, power, arg):
        self.arg = arg
        self.power = power

    def __str__(self):
        return '{}^{}'.format(self.arg, self.power)

    def diff(self):
        if type(self.arg) is Zero or type(self.arg) is Const:
            return Zero()
        if type(self.arg) is Varriable:
            return Mul(Const(self.power),
                       PowerFunc(self.power - 1,  self.arg))
        return Mul(Mul(
            Const(self.power),
            PowerFunc(self.power - 1,  self.arg)),
            self.arg.diff())


class ExponentFunc:
    def __init__(self, base, arg):
        self.arg = arg
        self.base = base

    def __str__(self):
        return '{}^{}'.format(self.base, self.arg)

    def diff(self):
        if type(self.arg) is Zero or type(self.arg) is Const:
            return Zero()
        if type(self.arg) is Varriable:
            return Mul(self, ln(self.base))
        return Mul(Mul(self, self.arg.diff()), ln(Const(self.base)))


class ln:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'ln{}'.format(self.arg)

    def diff(self):
        if type(self.arg) is Zero or type(self.arg) is Const:
            return Zero()
        if type(self.arg) is Varriable:
            return Div(Const(1), self.arg)
        return Div(self.arg.diff(), self.arg)


class sin:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'sin{}'.format(self.arg)

    def diff(self):
        if type(self.arg) is Zero or type(self.arg) is Const:
            return Zero()
        if type(self.arg) is Varriable:
            return cos(self.arg)
        return Mul(cos(self.arg), self.arg.diff())


class cos:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'cos{}'.format(self.arg)

    def diff(self):
        if type(self.arg) is Zero or type(self.arg) is Const:
            return Zero()
        if type(self.arg) is Varriable:
            return Mul(Const(-1), sin(self.arg))
        return Mul(Mul(Const(-1), sin(self.arg)), self.arg.diff())
