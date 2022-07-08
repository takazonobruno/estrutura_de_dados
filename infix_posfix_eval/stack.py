class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class Stack():
    def __init__(self):
        self.top = None
        self.cont = 0

    def __str__(self):
        strStack = ""
        node = self.top
        while True:
            strPilha += str(node.value) + "\n"
            node = node.next
            if node == None:
                break
        return strStack

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, v):
        if self.isEmpty():
            self.top = Node(v)
            self.cont += 1
        else:
            new = Node(v, self.top)
            self.top = new
            self.cont += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        v = self.top.value
        self.top = self.top.next
        self.cont -= 1
        return v

    def stacktop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.top.value