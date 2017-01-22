str_regex = '(https?:\/\/)?([a-z]+\d\.)?([a-z]+\.)?activeingredients\.[a-z]+(/?(work|about|contact)?/?([a-zA-z-]+)*)?/?'
str_regex1 = '(https?:\/\/)?([a-z]+\d\.)?([a-z]+\.)?activeingredients\.[a-z]+(/?[^\s"\.]*/?)*'
str_regex2 = '(https?:\/\/)?(www)?([a-z]+\.)?onet\.[a-z]+(/?[^\s"\.]*/?)*'
str_regex3 = '(https?:\/\/)?(www)?(wiadomosci+\.)?onet\.[a-z]+(/?[^\s"\.]*/?)*'

import urllib.request
from Stacks import Stack
import re
import functools
import operator as op
from nary_tree import *
url = 'http://www.activeingredients.com/
s = set()
List = []
url_list = []
def f_go(List, s, url):
    try:
        if url in s:
            return
        s.add(url)
        with urllib.request.urlopen(url) as response:
            html = response.read()
            #print(url)
        h = html.decode("utf-8")
        lst0 = prepare_expression(list(h))
        ntr = buildNaryParseTree(lst0)
        lst2 = nary_tree_tolist(ntr)
        lst3= functools.reduce(op.add, lst2, [])
        str2 = ''.join(lst3)
        List.append(str2)
        f1 = re.finditer(str_regex3, h)
      
        l1 = []
        for tok in f1:
            ind1 = tok.span()
            l1.append(h[ind1[0]:ind1[1]])
        for exp in l1:
            length = len(l1)
            if (exp[-1] == 'g' and exp[length - 2] == 'p' and exp[length - 3] == 'j')  or \
                (exp[-1] == 'p' and exp[length - 2] == 'n' and exp[length - 3] == 'g'):
                    pass
            else:
                f_go(List, s, exp, iter_cnt + 1, url_list)
    except:
        return

%time f_go(List, s, url1, 0, url_list)
print(url_list)
print("lwngth main list here",len(List))
print(list(set(List)))
#print("elements on beginning", List[0], List[1])#, List[2], List[3], List[4])
#str1 = ''.join(List[1:])
#print(List)

# html crawling functions and tree class

class NaryTree:
    """n ary tree, Python list as an array of children"""

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

    def getNthKid(self, i=-1):  # return a child index i, the first from right if i not specified
        return self.kids[i]


def buildNaryParseTree(lexp):
    e_tree = NaryTree([])
    stk = Stack()
    cur = e_tree
    ctr = 0
    ctr1 = 0
    ctr2 = 0
    for token in lexp:
        if token == '<p>':
            cur.insert([])
            cur = cur.getNthKid()
            ctr += 1 
            stk.push('<p>')
        elif token == '<title>':
            cur.insert([])
            cur = cur.getNthKid()
        elif token == '<p class=':
            cur.insert([])
            cur = cur.getNthKid()
            ctr2 += 1
            stk.push('<pclass>')
        elif not token in ['<p>', '</p>', '<title>', '</title>', '< p class='] and (ctr != 0 or ctr1 != 0 or ctr2 != 0):
            cur.setRootVal(token)
        elif token == '</p>':
            if stk.peek() == '<p>':
                ctr -= 1
            elif stk.peek() == '<pclass>':
                ctr2 -= 1
            stk.pop()
            cur = cur.getParent()
        elif token == '</title>':
            ctr1 -= 1
            cur = cur.getParent()
        
    return e_tree


def traverse(tree):  # dfs over tree
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


def nary_tree_tolist(tree):  # convert tree to a list
    if tree:
        lst = []
        stk = []
        stk.append(tree)
        while len(stk) > 0:
            top = stk.pop()
            if top.kids:
                for child in top.kids:
                    stk.append(child)
            if top.getRootVal() != []:
                lst.append(top.getRootVal())
        return lst
    else:
        return None

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
        if exp[i] == '<' and exp[i + 1] == 'h' and exp[i + 2] == '1' and exp[i + 3] == '>':
            exp[i] = '<h1>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'h' and exp[i + 3] == '1' and exp[i + 4] == '>':
            exp[i] = '</h1>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
        if exp[i] == '<' and exp[i + 1] == 'h' and exp[i + 2] == '2' and exp[i + 3] == '>':
            exp[i] = '<h2>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'h' and exp[i + 3] == '2' and exp[i + 4] == '>':
            exp[i] = '</h2>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
        if exp[i] == '<' and exp[i + 1] == 'h' and exp[i + 2] == '3' and exp[i + 3] == '>':
            exp[i] = '<h3>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'h' and exp[i + 3] == '3' and exp[i + 4] == '>':
            exp[i] = '</h3>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
        if exp[i] == '<' and exp[i + 1] == 'h' and exp[i + 2] == '4' and exp[i + 3] == '>':
            exp[i] = '<h4>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'h' and exp[i + 3] == '4' and exp[i + 4] == '>':
            exp[i] = '</h4>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
        if exp[i] == '<' and exp[i + 1] == 'h' and exp[i + 2] == '5' and exp[i + 3] == '>':
            exp[i] = '<h5>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'h' and exp[i + 3] == '5' and exp[i + 4] == '>':
            exp[i] = '</h5>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
        if exp[i] == '<' and exp[i + 1] == 'h' and exp[i + 2] == '6' and exp[i + 3] == '>':
            exp[i] = '<h6>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'h' and exp[i + 3] == '6' and exp[i + 4] == '>':
            exp[i] = '</h6>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
        if exp[i] == '<' and exp[i + 1] == 'm' and exp[i + 2] == 'e' and exp[i + 3] == 't' and exp[i + 4] == 'a' and \
                        exp[i + 5] == '>':
            exp[i] = '<meta>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
        if exp[i] == '<' and exp[i + 1] == '/' and exp[i + 2] == 'm' and exp[i + 3] == 'e' and exp[i + 4] == 't' and \
                        exp[i + 5] == 'a' and exp[i + 6] == '>':
            exp[i] = '</meta>'
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
        if exp[i] == '<' and exp[i+1] == 'p' and exp[i+2] == ' ' and exp[i+3] == 'c' and exp[i+4] == 'l' \
            and exp[i+5] == 'a' and exp[i+6] == 's' and exp[i+7] == 's' and exp[i+8] == '=':
            exp[i] = '<p class='
            exp[i + 1] = []
            exp[i + 2] = []
            exp[i + 3] = []
            exp[i + 4] = []
            exp[i + 5] = []
            exp[i + 6] = []
            exp[i + 7] = []
            exp[i + 8] = []
    for t in range(len(exp) - 1, -1, -1):
        if isinstance(exp[t], list):
            del (exp[t])
    return exp

