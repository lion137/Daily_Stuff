#!/usr/bin/python3
import operator as op


def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.getLeftChild())
        print(tree.getRootVal())
        inorder_traversal(tree.getRightChild())


def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.getLeftChild())
        postorder_traversal(tree.getRightChild())
        print(tree.getRootVal())


def iterative_reduce(xs, f, start):
    while True:
        if not xs:
            return start
        else:
            xs, f, start = xs[1:], f, f(start, xs[0])
    return xs


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            t = BinaryTree(newNode)
            self.leftChild = t
            t.parent = self
            # self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.parent = self
            t.leftChild = self.leftChild
            self.leftChild.parent = t
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            t = BinaryTree(newNode)
            self.rightChild = t
            t.parent = self
            # self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.parent = self
            t.rightChild = self.rightChild
            self.rightChild.parent = t
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getParent(self):
        return self.parent

    def setRootVal(self, obj):
        self.key.append(obj)

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


exp = ['[', 'a', 'a', '(', 'b', 'b', '(', 'c', 'c', ')', 'b', '(', 'd', 'd', '{', 'e', 'e', '}', ')', ')', 'a', ']']


class NaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.parent = None
        self.kids = None

    def insert(self, newNode):
        if self.kids:
            t = NaryTree(newNode)
            self.kids.append(t)
            t.parent = self
        else:
            t = NaryTree(newNode)
            self.kids = []
            self.kids.append(t)
            t.parent = self

    def setRootVal(self, obj):
        self.key.append(obj)

    def getRootVal(self):
        return self.key

    def getParent(self):
        return self.parent

    def getNthKid(self, i=-1): # return a child index i, the last one if i not specified
        return self.kids[i]


def buildNaryParseTree(lexp):
    e_tree = NaryTree([])
    cur = e_tree
    ctr = 0
    ctr1 = 0
    for token in lexp:
        if token == '<p>':
            cur.insert([])
            cur = cur.getNthKid()
            ctr += 1
            #if ctr1 is not 0:
             #   ctr1 -= 1
        elif token == '<title>':
            cur.insert([])
            cur = cur.getNthKid()
            ctr1 += 1
            #if ctr is not 0:
             #   ctr -= 1
        elif not token in ['<p>', '</p>', '<title>', '</title>'] and (ctr is not 0 or ctr1 is not 0):
            cur.setRootVal(token)
        elif token == '</p>':
            ctr -= 1
            #if ctr1 is 0:
            #    ctr1 += 1
            cur = cur.getParent()
        elif token == '</title>':
            ctr1 -= 1
            #if ctr is 0:
            #   ctr += 1
            cur = cur.getParent()
    return e_tree

def traverse(tree): # dfs over tree
    if tree:
        stk = []
        stk.append(tree)
        while len(stk) > 0:
            top = stk.pop()
            if top.kids:
                for child in top.kids:
                    stk.append(child)
            print(top.getRootVal())

    else:
        return None

def nary_tree_tolist(tree, lst): # convert tree to a list
    if tree:
        stk = []
        stk.append(tree)
        while len(stk) > 0:
            top = stk.pop()
            if top.kids:
                for child in top.kids:
                    stk.append(child)
            lst.append(top.getRootVal())
        return lst
    else:
        return None


def buil_n_ary_parse_tree(exp):
    e_tree = BinaryTree([])
    current = e_tree
    ctr = 0
    ctr1 = 0
    ctr2 = 0
    for token in exp:
        if token == '<p>':
            if ctr == 0:
                current.insertRight(['<p>'])
                current = current.getRightChild()
                ctr += 1
            else:
                ctr += 1
                current.insertLeft('<p>')
                current = current.getLeftChild()
        elif token == '<mark>':
            if ctr1 == 0:
                current.insertRight(['<mark>'])
                current = current.getRightChild()
                ctr1 += 1
            else:
                ctr1 += 1
                current.insertLeft([])
                current = current.getLeftChild()

        elif (not token in ['<p>', '</p>', '<mark>', '</mark>']) and ctr is not 0:
            current.setRootVal(token)
        elif token == '</p>':
            ctr -= 1
            current = current.getParent()
        elif token == '</mark>':
            ctr1 -= 1
            current = current.getParent()
    return e_tree

    # parse_tree = buil_n_ary_parse_tree(exp)
    # inorder_traversal(parse_tree)


def split_input_elements(xs):
    result = []
    for i in range(len(xs)):
        result.append(xs[i].rsplit())
    return result


def split_input_and_to_int(xs):
    def helper(ys):
        l = list(map(int, ys))
        return l

    l1 = list(map(helper, xs))
    return l1


with open('/home/lion/projects/python/blog_not_notebook/ternary_trees_html_parsing/html_example.txt') as f:
    lines = f.read().splitlines()
print("slista z linii stringu wejsciowego ", lines)
print("dlugosc tej listy  ", len(lines))
lst1 = list(map(list, lines))
lst = iterative_reduce(lst1, op.add, [])
# lst2 = iterative_reduce(lst, op.add, '')
print("cale wejscie stokenizpowane i zlistowane ", lst)


# tags: html, head, body, meta, title, ul, h1, h2, li, a
def prepare_expression(exp):
    """takes a page as a list and make tags visible"""
    del_list = []
    l = len(exp)
    for i in range(l):
        if exp[i] == '<' and exp[i + 1] == 'p' and exp[i + 2] == '>':
            exp[i] = '<p>'
            exp[i + 1] = []
            exp[i + 2] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'p' and exp[i + 3] == '>':
            exp[i] = '</p>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i] == 'b' and exp[i + 2] == '>':
            exp[i] = '<b>'
            exp[i + 1] = []
            exp[i + 2] = []
        if exp[i] == '<' and exp[i] == '/' and exp[i + 2] == 'b' and exp[i + 3] == '>':
            exp[i] = '</b>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == 't' and exp[i + 2] == 'i' and exp[i + 3] == 't' and exp[i + 4] == 'l' and \
                        exp[i + 5] == 'e' and exp[i + 6] == '>':
            exp[i] = '<title>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 't' and exp[i + 3] == 'i' and exp[i + 4] == 't' and \
                        exp[i + 5] == 'l' and exp[i + 6] == 'e' and exp[i + 7] == '>':
            exp[i] = '</title>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
            exp[i + 7] = []

        if exp[i] == '<' and exp[i + 1] == 'i' and exp[i + 2] == '>':
            exp[i] = '<i>'
            del_list.append(i + 1)
            del_list.append(i + 2)
        if exp[i] == '<' and exp[i + 1] == 'e' and exp[i + 2] == 'm' and exp[i + 3] == '>':
            exp[i] = '<em>'
            del_list.append(i + 1)
            del_list.append(i + 2)
            del_list.append(i + 3)
        if exp[i] == '<' and exp[i + 1] == 'm' and exp[i + 2] == 'a' and exp[i + 3] == 'r' and exp[i + 4] == 'k' and \
                        exp[i + 5] == '>':
            exp[i] = '<mark>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'm' and exp[i + 3] == 'a' and exp[i + 4] == 'r' and \
                        exp[i + 5] == 'k' and exp[i + 6] == '>':
            exp[i] = '</mark>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
        if exp[i] == '<' and exp[i + 1] == 's' and exp[i + 2] == 'm' and exp[i + 3] == 'a' and exp[i + 4] == 'l' and \
                        exp[i + 5] == 'l':
            exp[i] = '<small>'
            del_list.append(i + 1)
            del_list.append(i + 2)
            del_list.append(i + 3)
            del_list.append(i + 4)
            del_list.append(i + 5)
        if exp[i] == '<' and exp[i + 1] == 'i' and exp[i + 2] == 'n' and exp[i + 3] == 's':
            exp[i] == '<ins>'
            del_list.append(i + 1)
            del_list.append(i + 2)
            del_list.append(i + 3)
    for t in range(len(exp) - 1, -1, -1):
        if isinstance(exp[t], list):
            del (exp[t])
    return exp
def prepare_expression1(exp):
    """takes a page as a list and make tags visible"""
    del_list = []
    l = len(exp)
    for i in range(l):
        if exp[i] == '<' and exp[i + 1] == 'p' and exp[i + 2] == '>':
            exp[i] = '<p>'
            exp[i + 1] = []
            exp[i + 2] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'p' and exp[i + 3] == '>':
            exp[i] = '</p>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == 't' and exp[i + 2] == 'i' and exp[i + 3] == 't' and exp[i + 4] == 'l' and \
                        exp[i + 5] == 'e' and exp[i + 6] == '>':
            exp[i] = '<title>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 't' and exp[i + 3] == 'i' and exp[i + 4] == 't' and \
                        exp[i + 5] == 'l' and exp[i + 6] == 'e' and exp[i + 7] == '>':
            exp[i] = '</title>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
            exp[i + 7] = []
    for t in range(len(exp) - 1, -1, -1):
        if isinstance(exp[t], list):
            del (exp[t])
    return exp

lst2 = prepare_expression1(lst)
print(
    "------------------------------------------------------------------------------------------------------------------")
print("wyloskane pare tokenow  ", lst2)
#tr = BinaryTree('')
#tr = buil_n_ary_parse_tree(lst2)
#ntr = NaryTree([])
ntr = buildNaryParseTree(lst2)
print("travers sparsowanego htmla: ")
#inorder_traversal(tr)
traverse(ntr)
lst3 = []
print(nary_tree_tolist(ntr, lst3))

'''
 l = []
    for line in sys.stdin:
        str(line)
        l.append(line.rstrip())
    print(l)
    l1 = split_input_elements(l)
    print(l1)
    #l2 = split_input_and_to_int(l1)
   # print(l2)
    # print(type(l[1]))
'''
