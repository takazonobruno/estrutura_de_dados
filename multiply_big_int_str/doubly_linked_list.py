class No:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self.size = 0

    def empty(self):
        if self.begin is None:
            return True
        else:
            return False

    def add_begin(self, value):
        no = No(value)
        if self.empty():
            self.begin = self.end = no
        else:
            no.next = self.begin
            self.begin.prev = no
            no.prev = None
            self.begin = no
        self.size += 1

    def add_end(self, value):
        no = No(value)
        if self.empty():
            self.begin = self.end = no
        else:
            self.end.next = no
            no.prev = self.end
            no.next = None
            self.end = no
        self.size += 1

    def insert_indice(self, i, value):
        half = int(self.size / 2)
        if i > self.size:
            raise IndexError("Invalid memory position")
        elif i == self.size:
            self.add_end(value)
        elif i == 0:
            self.add_begin(value)
        else:
            if i <= half:
                no = No(value)
                chain = self.begin
                cont = 0
                while cont < (i - 1):
                    chain = chain.next
                    cont += 1
                no.next = chain.next
                chain.next.prev = no
                chain.next = no
                no.prev = chain
            else:
                no = No(value)
                chain = self.end
                cont = self.size
                while cont > i:
                    chain = chain.prev
                    cont -= 1
                no.next = chain.next
                chain.next.prev = no
                chain.next = no
                no.prev = chain
        self.size += 1

    def remove_begin(self):
        if self.empty():
            raise TypeError("List is empty!")
        elif self.size == 1:
            self.begin = None
            self.end = None
        else:
            self.begin = self.begin.next
            self.begin.prev = None
        self.size -= 1

    def remove_end(self):
        if self.empty():
            raise TypeError("List is empty!")
        elif self.size == 1:
            self.remove_begin()
        else:
            self.end = self.end.prev
            self.end.next = None
        self.size -= 1

    def remove_index(self, i):
        if self.empty():
            raise TypeError("List is empty!")
        elif i == 0:
            self.remove_begin()
        elif i == self.size - 1:
            self.remove_end()
        else:
            chain = self.begin
            cont = 0
            while cont < i - 1:
                chain = chain.next
                cont += 1
            aux = chain.next
            chain.next = aux.next
            aux.next.prev = chain
            None
            self.size -= 1

    def remove_value(self, value):
        if self.size == 0:
            return None
        chain = self.begin
        cont = 0
        while chain.data != value:
            chain = chain.next
            cont += 1
        self.remove_index(cont)

    def pop_begin(self):
        value = self.begin.data
        self.remove_begin()
        return value

    def pop_end(self):
        value = self.end.data
        self.remove_end()
        return value

    def display(self):
        current = self.begin
        while True:
            print(current.data, end=" ")
            current = current.next
            if current is None:
                break
