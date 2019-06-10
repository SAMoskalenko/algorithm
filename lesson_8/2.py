# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter, deque

class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def haffman_tree(string):

    string = Counter(string)

    string = deque(sorted(string.items(), key=lambda item: item[1]))

    while len(string) > 1:

        weight = string[0][1] + string[1][1]
        node = Node(left=string.popleft()[0], right=string.popleft()[0])

        for i, item in enumerate(string):
            if weight > item[1]:
                continue
            else:
                string.insert(i, (node, weight))
                break
        else:
            string.append((node, weight))

    return string[0][0]

code_table = dict()


def haffman_code(tree, path=''):

    if not isinstance(tree, Node):
        code_table[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


test_string = "Ехал грека через реку"

haffman_code(haffman_tree(test_string))

for i in test_string:
    print(code_table[i], end=' ')