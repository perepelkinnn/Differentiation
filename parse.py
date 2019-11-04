def get_index_operator(line, operators):
    for cur_operators in range(len(operators)):
        num_open_brackets = 0
        cur_pos = len(line) - 1
        while cur_pos >= 0:
            if line[cur_pos] == ')':
                num_open_brackets += 1
            elif line[cur_pos] == '(':
                num_open_brackets -= 1
            elif num_open_brackets == 0 and line[cur_pos] in operators[cur_operators]:
                if (line[cur_pos] not in '+-') or (
                    cur_pos != 0 and is_right_sign(
                        line[cur_pos - 1], operators, cur_operators+1)):
                    return cur_pos
            cur_pos -= 1
    return -1


def is_right_sign(char, operators, index):
    while index < len(operators):
        if char in operators[index]:
            return False
        index += 1
    return True


def fill_tree(line, node):
    op_index = get_index_operator(line, operators_by_reverse_order)
    if op_index != -1:
        node.value = line[op_index]
        node.left = Node()
        node.right = Node()
        fill_tree(line[:op_index], node.left)
        fill_tree(line[op_index + 1:], node.right)
    else:
        if line and line[0] == '(' and line[-1] == ')':
            fill_tree(line[1:-1], node)
            return
        node.value = line


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
