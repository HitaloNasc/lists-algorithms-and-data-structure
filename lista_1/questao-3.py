def pilhaImaculada(stack):
    for i in range(len(stack) - 1):
        if int(stack[i]) > int(stack[i + 1]):
            return False
    return True


def novaLocacao(stack, new_location):
    for i in range(len(stack)):
        if new_location <= stack[i]:
            stack.insert(i, new_location)
            return
    stack.append(new_location)


def main():
    locations = input().split(',')
    stack_location = [int(location) for location in locations]
    new_location = int(input())
    if pilhaImaculada(stack_location):
        novaLocacao(stack_location, new_location)
        print([str(location) for location in stack_location])
    else:
        print('A pilha está um caos.')


main()
