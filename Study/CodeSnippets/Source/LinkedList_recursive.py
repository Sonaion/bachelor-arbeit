class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


def function(node_list, odd=False):
    if node_list is None:
        return 0
    if not odd:
        return node_list.data + function(node_list.next, True)
    else:
        return function(node_list.next, False)


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
