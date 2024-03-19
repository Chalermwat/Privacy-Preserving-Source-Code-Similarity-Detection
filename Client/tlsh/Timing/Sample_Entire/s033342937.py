class Node(object):
    def __init__(self, c):
        self.c = c
        self.left = None
        self.right = None

def print_node(node):
    print node.c
    if node.left != None:
        print_node(node.left)
    if node.right != None:
        print_node(node.right)

def calc_node(node):
    if node.c in ('+', '-', '/', '*'):
        if node.c == '+':
            return calc_node(node.left) + calc_node(node.right)
        if node.c == '-':
            return calc_node(node.left) - calc_node(node.right)
        if node.c == '*':
            return calc_node(node.left) * calc_node(node.right)
    else:
        return int(node.c)

def make_node(s):
    global pos
    node = Node(s[pos])
    if s[pos] in ('+', '-', '*'):
        pos += 1
        node.right = make_node(s)
        pos += 1
        node.left = make_node(s)
    return node

s = raw_input().split()
s.reverse()
#print s
pos = 0
n = make_node(s)
#print_node(n)
print "%d" % calc_node(n)