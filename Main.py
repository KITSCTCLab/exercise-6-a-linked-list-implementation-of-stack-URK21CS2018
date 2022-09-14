class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    node = Node(data)
    self.next = self.head
    self.head = node

  def pop(self) -> None:
    # Write your code here
    t = self.head
    if t is not None:
      print(t.data)
      

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    t = self.head
    if t is not None:
      while t.next:
        t = t.next
        print(t.data)


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
