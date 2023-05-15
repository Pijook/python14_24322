class Element:
    def __int__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

    def __init__(self):
        self.data = None
        self.nextE = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = ""
        element = self.tail

        while element is not None:
            if result == "":
                result = element.data
            else:
                result = str(result) + ", " + str(element.data)
            element = element.nextE

        return result

    def get(self, e):
        index = 0

        element = self.tail
        while element is not None:
            if index == e:
                return element
            else:
                index = index + 1
                element = element.nextE

        return None

    def delete(self, e):
        previous = None
        element = self.tail

        while element is not None:
            if element == e:
                if previous is None:
                    self.tail = e.nextE
                else:
                    previous.nextE = e.nextE
                break
            else:
                previous = element
                element = element.nextE

    def append(self, e, func=None):
        if self.tail is None and self.head is None:
            self.tail = e
            self.head = e
            return None

        element = self.tail
        previous = None

        while element is not None:
            if func is not None:
                if func(e, element):
                    if previous is not None:
                        previous.nextE = e
                    e.nextE = element
                    break
                else:
                    previous = element
                    element = element.nextE
            else:
                if e.data >= element.data:
                    previous = element
                    element = element.nextE
                else:
                    if previous is not None:
                        previous.nextE = e
                    e.nextE = element

                    break

        if element is None:
            self.head.nextE = e
            self.head = e
