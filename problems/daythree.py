class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#A rather interesting problem - no parameters for how the string should look
#In fact, not many parameters at all; only the Node class was given.
#One test to pass:
'''
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

#Recursion seems to be the most intuitive way to accomplish both tasks
def serialize(node):
    #Perhaps a preorder traversal works best here?
    #Should be around O(n) time
    #Will have to join the list afterwards
    temp = []
    if node == None:
        temp.append("-")
        return temp
    temp.append(node.val)
    temp.extend(serialize(node.left))
    temp.extend(serialize(node.right))
    return temp

#TODO: Write an iterative version

node = Node(1, Node(2, Node(3), Node(4)), Node(5))
print(serialize(node))
