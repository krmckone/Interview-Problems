# WIP

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def print_tree(node):
    if not node:
        return 
    else:
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

def serialize(node):
    if not node:
        return ''
    else:
        return node.val + ' ' + serialize(node.left) + serialize(node.right)

def deserialize(str):
    list_str = str.split(' ')
    return list_str
        

node = Node('root', Node('left', Node('left.left')), Node('right'))


print(deserialize(serialize(node)))