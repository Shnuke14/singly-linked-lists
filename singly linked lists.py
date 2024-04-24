class LinkedList:
  head = None
  
  class Node:
    element = None
    next_node = None

    def init(self, element, next_node = None):
      self.element = element
      self.next_node = next_node

  def append(self, element):
    if not self.head:
      self.head = self.Node(element)
      return element
    node = self.head

    while node.next_node:
      node = node.next_node

    node.next_node = self.Node(element)

    return element

  def assign(self, element, index):
    node = self.head
    i = 0

    while i < index:
      node = node.next_node
      i += 1

    node.element = element
    
  def insert(self, element, index):
    i = 0
    node = self.head
    prev_node = self.head

    while i < index:
      prev_node = node
      node = node.next_node
      i += 1

    prev_node.next_node = self.Node(element, next_node = node)
  
    return element

  def get(self, index):
    i = 0
    node = self.head
    prev_node = self.head

    while i < index:
      prev_node = node
      node = node.next_node
      i += 1

    return node.element

  def out(self):
    node = self.head

    while node.next_node:
      print(node.element)
      node = node.next_node
    print(node.element)

  def delete(self, index):
    if index == 0:
      self.head = self.head.next_node
    node = self.head
    i = 0
    prev_node = node

    while i < index:
      prev_node = node
      node = node.next_node
      i += 1

    prev_node.next_node = node.next_node
    element = node.element
    
    del node
    
    return element


  def get_length(self):
    if not self.head:
      return 0

    i = 1
    node = self.head

    while node.next_node:
      i += 1
      node = node.next_node

    return i
linked_list = LinkedList()

## Добавление новых элементов в список
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

## Удаление элемента по индексу
linked_list.delete(1)

## Вставка элемента
linked_list.insert(17, 1)

## Получение длины односвязного списка
print(linked_list.get_length())

print("\n")

## Замена элемента в списке по индексу
linked_list.assign(35, 2)

## Получение элемента по индексу
print(linked_list.get(2))

## Вывод списка
linked_list.out()