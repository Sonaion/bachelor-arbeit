class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_iter(self):
        result = []
        result.append(self)
        if self.left is not None:
            left = self.left.pre_order_iter()
            result = result + left
        if self.right is not None:
            right = self.right.pre_order_iter()
            result = result + right
        return result


def helper(first, second, second_len=None):
    if len(first) == 0:
        return []

    if len(second) == 0:
        return []

    if second_len is None:
        return helper(first, second, len(second))

    result = [(first[0], second[0])]
    if len(second) == second_len:
        inner = helper(first, second[1:], second_len)
        outer = helper(first[1:], second, second_len)
        result = result + inner + outer
    else:
        inner = helper(first, second[1:], second_len)
        result = result + inner
    return result


def function(powerset):
    if len(powerset) == 0:
        return 0
    return powerset[0][0].value * powerset[0][1].value + function(powerset[1:])


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(helper(n.pre_order_iter(), n.pre_order_iter())))
