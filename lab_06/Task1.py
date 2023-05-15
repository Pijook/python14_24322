import MyLinkedList

list = MyLinkedList.MyLinkedList()

element1 = MyLinkedList.Element()
element1.data = 1
element3 = MyLinkedList.Element()
element3.data = 17
element2 = MyLinkedList.Element()
element2.data = 3

list.append(element1, None)
list.append(element3, None)
list.append(element2, None)

print(list)

list.delete(element2)

print(list)