import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size = self.size + 1
    return self
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      item = self.storage.remove_head()
      self.size = self.size - 1
    return item

  def len(self):
    return self.size
