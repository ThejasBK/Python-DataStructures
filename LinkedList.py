class Node:
    def __init__(self, data = None, Next = None):
        self.data = data
        self.Next = Next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
        else:
            itr = self.head
            while itr.Next:
                itr = itr.Next
            itr.Next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.Next
        return count

    def remove_at_location(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.Next
            return
        else:
            count = 0
            itr = self.head
            while count < index - 1:
                itr = itr.Next
                count += 1
            itr.Next = itr.Next.Next

    def insert_at_location(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_beginning(data)
        elif index == self.get_length():
            self.insert_at_end(data)
        else:
            count = 0
            itr = self.head
            while count < index - 1:
                count += 1
                itr = itr.Next
            itr.Next = Node(data, itr.Next)

    def insert_after_value(self, after_data, data):
        if self.head is None:
            print('Empty list')
            return
        itr = self.head
        while itr:
            if itr.data == after_data:
                itr.Next = Node(data, itr.Next)
                return
            itr = itr.Next
        print('Element not in list')

    def remove_by_value(self, value):
        if self.head is None:
            print('Empty list')
            return
        itr = self.head
        while itr:
            if itr.data == value:
                prev.Next = itr.Next
                return
            prev = itr
            itr = itr.Next
        print('Element not in list')

    def print(self):
        if self.head is None:
            print('Empty List')
            return
        itr = self.head
        while itr:
            print(itr.data, end = '-->')
            itr = itr.Next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(100)
    ll.insert_at_end(110)
    ll.insert_at_beginning(90)
    ll.insert_values([1, 2, 3, 4])
    ll.insert_at_location(50, 2)
    ll.insert_after_value(50, 60)
    ll.print()
    print()
    ll.remove_by_value(60)
    ll.print()
