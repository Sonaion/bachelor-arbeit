class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_iter(self):
        stack = []
        result = []
        stack.append(self)

        while len(stack) != 0:
            node = stack.pop()
            result.append(node)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return result


def function(node):
    result = 0
    for current1 in node.pre_order_iter():
        for current2 in node.pre_order_iter():
            result += current1.value * current2.value
    return result


n = Node(2)
n.left = Node(1)
n.right = Node(3)
print(function(n))
