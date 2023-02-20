def compare_front_verse(cover_list):
    cover_dict = {'FRONT': 'F', 'VERSE': 'V'}
    stack = []
    for i, cover in enumerate(cover_list):
        if cover == cover_dict['FRONT']:
            stack.append(i)
        elif cover == cover_dict['VERSE']:
            if not stack:
                return i
            else:
                stack.pop()
    if stack:
        return stack[0]
    else:
        return None


def main():
    try:
        cover_input = input()
        cover_list = [cover for cover in cover_input]
    except:
        cover_list = []

    compared = compare_front_verse(cover_list)
    if compared is None:
        print(f'Correto.')
    else:
        print(f'Incorreto, devido a capa na posição {compared + 1}.')


main()
