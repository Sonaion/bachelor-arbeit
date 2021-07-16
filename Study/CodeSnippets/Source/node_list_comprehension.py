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
    multiplies = [x.value * y.value for x in node.pre_order_iter() for y in node.pre_order_iter()]
    total = 0
    scanned = [total := total + x for x in multiplies]
    return scanned[-1]


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(n))
