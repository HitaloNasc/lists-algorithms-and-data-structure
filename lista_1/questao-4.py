class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


class SearchHistory:
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                self.tail.next = current_node
                current_node.prev = self.tail
                self.tail = current_node
                current_node.next = None
                return
            current_node = current_node.next

    def remove(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                return
            current_node = current_node.next

    def add(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev


def main():
    searchHistory = SearchHistory()

    stopCondition = False
    while not stopCondition:
        line = input().split(' ')
        operation = line[0]

        # ADD
        if operation == 'ADD':
            searchHistory.add(line[1])
        # REM
        elif operation == 'REM':
            searchHistory.remove(line[1])
        # EXIB
        elif operation == 'EXIB':
            searchHistory.display()
        # FIND
        elif operation == 'FIND':
            searchHistory.find(line[1])
        # END
        elif operation == 'END':
            stopCondition = True


main()
