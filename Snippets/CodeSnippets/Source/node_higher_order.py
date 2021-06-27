class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_iter(self):
        result = [self]
        if self.left is not None:
            left = self.left.pre_order_iter()
            result = result + left
        if self.right is not None:
            right = self.right.pre_order_iter()
            result = result + right
        return result


def function(node):
    duos = product(node.pre_order_iter(), node.pre_order_iter())
    multiplies = map(lambda x: x[0].value * x[1].value, duos)
    return reduce(lambda x, y: x + y, multiplies)


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(n))
