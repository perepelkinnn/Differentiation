from tree import Node


def get_index_operator(line, operator):
    sum_brackets = cur_pos = 0
    for cur_char in line:
        if cur_char == ')':
            sum_brackets += 1
        elif cur_char == '(':
            sum_brackets -= 1
        elif sum_brackets == 0 and cur_char == operator:
            return cur_pos
        cur_pos += 1
    return -1


def get_index_first_operation(line):
    for op in ['+', '-', '*', '/', '^']:
        index = get_index_operator(line, op)
        if index != -1:
            return index
    return -1


def split_line(line):
    index = get_index_first_operation(line)
    if index != -1:
        return line[:index], line[index], line[index + 1:]
    return [None, line, None]


def check_open_bracket(line):
    return line[0] == '('


def check_close_bracket(line):
    return line[-1] == ')'


def check_brackets(line):
    return check_open_bracket(line) and check_close_bracket(line)


def remove_brackets(line):
    return line[1:-1]


def check_func(line):
    functions = ['sin(', 'cos(', 'ln(']
    for func in functions:
        if line.startswith(func) and check_close_bracket(line):
            return True

def get_func(line):
    functions = ['sin(', 'cos(', 'ln(']
    for func in functions:
        if line.startswith(func):
            return func[:-1], line[len(func):-1]



def fill_tree(line, node):
    left, mid, right = split_line(line)
    if left and right:
        node.value = mid
        node.init_children()
        fill_tree(left, node.left)
        fill_tree(right, node.right)
        return
    elif check_brackets(line):
        line = remove_brackets(line)
        fill_tree(line, node)
        return
    elif check_func(line):
        func, line = get_func(line)
        node.value = func
        node.init_child()
        fill_tree(line, node.next)
        return
    node.value = line


def build_tree(line):
    root = Node()
    fill_tree(line, root)
    return root