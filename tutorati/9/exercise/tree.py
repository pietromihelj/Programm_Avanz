import random
from os import path, getcwd
from ctypes import cdll, c_bool, c_float, c_int, pointer, POINTER, Structure


class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.rigth = None
    self.left = None
    self.str = " "

  def search(self, key):
    if self.key == key:
      return self.value
    if self.rigth != None and self.key < key:
      return self.rigth.search(key)
    if self.left != None and self.key > key:
      return self.left.search(key)
    return None

  def insert(self, key, value):
      
      if self.key == key:
        self.value = value
      if self.key < key:
        if self.rigth is None:
          self.rigth = Node(key,value)
        else:
          self.rigth.insert(key,value)
      if self.key > key:
        if self.left is None:
          self.left = Node(key,value)
        else:
          self.left.insert(key,value)

  def __str__(self):
    s = f"{self.key}"
    if self.left is not None or self.rigth is not None:
      s = f"( {s} {str(self.left)} {str(self.rigth)})"
    return s

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def search(self, key):
    if self.root is None:
      return None
    return self.root.search(key)

  def insert(self, key, value):
    if self.root is None:
      self.root = Node(key, value)
    else:
      self.root.insert(key,value)

  def __str__(self):
    return self.root.__str__()


class CTreeNode(Structure):
  pass

CTreeNode._fields_ = [("key", c_int), ("value", c_float),
                      ("left", POINTER(CTreeNode)), ("right", POINTER(CTreeNode))]


class CTree:
  code = None

  def __init__(self):
    if CTree.code is None:
      CTree.code = cdll.LoadLibrary(path.join(getcwd(), "libtree.so"))
      CTree.code.insert.argtypes = [POINTER(CTreeNode), c_int, c_float]
      CTree.code.insert.restype = POINTER(CTreeNode)
      CTree.code.search.argtypes = [POINTER(CTreeNode), c_int, POINTER(c_float)]
      CTree.code.search.restype = c_bool
      CTree.code.destroy.argtypes = [POINTER(CTreeNode)]
    self.root = POINTER(CTreeNode)()

  def search(self, key):
    res = c_float()
    if CTree.code.search(self.root,c_int(key),pointer(res)):
      return res.value
    return None

  def insert(self, key, value):
    self.root = CTree.code.insert(self.root,c_int(key),c_float(value))

  def __str__(self):
    def print_node(node):
      if not node:
        return str(None)
      else:
          s = f"{node.contents.key}"
          if node.contents.left or node.contents.right:
            s = f"( {s} {print_node(node.contents.left)} {print_node(node.contents.right)})"
          return s
    return print_node(self.root)

  def __del__(self):
    CTree.code.destroy(self.root)


if __name__ == "__main__":
  pairs = [(random.randint(0, 30), random.random()) for _ in range(20)]
  searches = [random.randint(0, 30) for _ in range(10)]
  print("Python only:")
  bst = BinarySearchTree()
  for p in pairs:
    bst.insert(p[0], p[1])
  for k in searches:
    print(f"Searching for {k}: {bst.search(k)}")
  print(bst)
  # Decommentare per la parte extra
  print("Calling C:")
  cbst = CTree()
  for p in pairs:
    cbst.insert(p[0], p[1])
  for k in searches:
    print(f"Searching for {k}: {cbst.search(k)}")
  print(cbst)