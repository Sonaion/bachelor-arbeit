from functools import reduce
from itertools import accumulate


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            tmp = self.current
            self.current = self.current.next
            return tmp


def function(node_list):
    filtered_list = [node.data for (idx, node) in enumerate(node_list) if idx % 2 == 0]
    total = 0
    scanned = [total := total + x for x in filtered_list]
    return scanned[-1]


node1 = Node(2)
node2 = Node(5)
node3 = Node(7)
node4 = Node(4)
node5 = Node(1)
node6 = Node(3)
node7 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(function(node1))
