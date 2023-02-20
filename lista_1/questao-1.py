import math


class Client:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, name, score):
        new_client = Client(name, score)
        if self.tail:
            new_client.prev = self.tail
            self.tail.next = new_client
            self.tail = new_client
        else:
            self.head = self.tail = new_client
        self.size += 1

    def add_many(self, clients):
        if clients:
            curr_client = clients.head
            while curr_client:
                self.add(curr_client.name, curr_client.score)
                curr_client = curr_client.next

    def call_next(self):
        if not self.head:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def remove_last(self):
        if not self.tail:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def half_reverse(self):
        half_size = math.ceil(self.size / 2)
        half_queue = Queue()
        for i in range(half_size):
            half_queue.add(self.tail.name, self.tail.score)
            self.remove_last()
        return half_queue


class Cashier():
    def __init__(self):
        self.queue = Queue()
        self.balance = 0

    def call_next(self):
        self.balance += self.queue.head.score
        self.queue.call_next()


def main():
    cashier_1 = Cashier()
    cashier_2 = Cashier()
    stop_condition = False
    while not stop_condition:
        command_line = input().split(' ')
        # ENTROU
        if command_line[0] == 'ENTROU:':
            if command_line[2] == '1':
                cashier_1.queue.add(command_line[1], float(command_line[3]))
                print(f'{command_line[1]} entrou na fila 1')
            elif command_line[2] == '2':
                cashier_2.queue.add(command_line[1], float(command_line[3]))
                print(f'{command_line[1]} entrou na fila 2')
        # PROXIMO
        if command_line[0] == 'PROXIMO:':
            if command_line[1] == '1':
                if cashier_1.queue.head:
                    print(f'{cashier_1.queue.head.name} foi chamado para o caixa 1')
                    cashier_1.call_next()
                else:
                    half_reverse_cashier_2 = cashier_2.queue.half_reverse()
                    cashier_1.queue.add_many(half_reverse_cashier_2)
                    if cashier_1.queue.head:
                        print(
                            f'{cashier_1.queue.head.name} foi chamado para o caixa 1')
                        cashier_1.call_next()
            elif command_line[1] == '2':
                if cashier_2.queue.head:
                    print(f'{cashier_2.queue.head.name} foi chamado para o caixa 2')
                    cashier_2.call_next()
                else:
                    half_reverse_cashier_1 = cashier_1.queue.half_reverse()
                    cashier_2.queue.add_many(half_reverse_cashier_1)
                    if cashier_2.queue.head:
                        print(
                            f'{cashier_2.queue.head.name} foi chamado para o caixa 2')
                        cashier_2.call_next()
        # FIM
        if command_line[0] == 'FIM':
            stop_condition = True
            print('Caixa 1: R$ {:.2f}, Caixa 2: R$ {:.2f}'.format(
                cashier_1.balance, cashier_2.balance))


main()
