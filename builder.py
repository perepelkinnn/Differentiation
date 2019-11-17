import re
import tree
import parse
from diff import *


pattern = re.compile(r'(^[0-9]*)([a-z]{0,1}$)')
pattern2 = re.compile(r'sin[a-z]{1}')
pattern3 = re.compile(r'cos[a-z]{1}')
pattern4 = re.compile(r'ln[a-z]{1}')


def build(node):
    func = None
    if node.value == '+':
        func = Sum(build(node.left),build(node.right))
    if node.value == '-':
        func = Sub(build(node.left),build(node.right))
    if node.value == '*':
        func = Sum(build(node.left),build(node.right))
    if node.value == '/':
        func = Sub(build(node.left),build(node.right))
    if node.value == 'sin':
        func = ComplexFunc(Sin(build(node.next)))
    if node.value == 'cos':
        func = ComplexFunc(Cos(build(node.next)))
    if node.value == 'ln':
        func = ComplexFunc(Ln(build(node.next)))
    if re.fullmatch(pattern, node.value):
        match = re.fullmatch(pattern, node.value)
        if match[1] and match[2]:
            func = Mul(Const(int(match[1])), Varriable(match[2]))
        elif match[1]:
            func = Const(int(match[1]))
        else:
            func = Varriable(match[2])
    if re.fullmatch(pattern2, node.value):
        match = re.fullmatch(pattern2, node.value)
        func = Sin(Varriable(match[0][-1]))
    if re.fullmatch(pattern3, node.value):
        match = re.fullmatch(pattern3, node.value)
        func = Cos(Varriable(match[0][-1]))
    if re.fullmatch(pattern4, node.value):
        match = re.fullmatch(pattern4, node.value)
        func = Ln(Varriable(match[0][-1]))
    return func


func = build(parse.build_tree('sin(2x+1)'))
b = func.diff()
print(b)