"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    next_node = Node(value)
    
    if self.tail == None:
      self.head = next_node
      self.tail = next_node
    else:
      self.tail.set_next(next_node)
      self.tail = next_node
    
    return self

  def remove_head(self):
    if self.head == None:
      return None
    elif self.head == self.tail:
      header = self.head.get_value()
      self.head = None
      self.tail = None
    else:
      header = self.head.get_value()
      self.head = self.head.get_next()
    return header

  def contains(self, value):
    node = self.head
    while node != None:
      item = node.get_value()
      if item == value:
        return True
      else:
        node = node.get_next()
    return False

  def get_max(self):
    if self.head == None:
      return None
    else:
      max_value = self.head.get_value()
      node = self.head.get_next()
      while node != None:
        item = node.get_value()
        if item > max_value:
          max_value = item
        node = node.get_next()
    return max_value
