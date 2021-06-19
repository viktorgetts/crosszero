def table_show():
    print(f"  0 1 2")
    for i in range(3):
        row = " ".join(table[i])
        print(f"{i} {row}")


def turn():
    while 1:

        x, y = input("Введите номер строки/номер столбца (например, 0/0) :").split('/')

        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if table[x][y] == ' ':
                return x, y
            else:
                print('Клетка занята!')
        else:
            print('Число вне диапазона!') 


def winner():
    for j in range(3):
        if table[j] == ['X', 'X', 'X']:
            print('Крестики победили!')
            return True
        elif table[j] == ['0', '0', '0']:
            print('Нолики победили!')
            return True

    check1 = []

    for k in range(3):
        if table[k][0] == 'X':
            check1.append('X')
        elif table[k][0] == '0':
            check1.append('0')

    if check1 == ['X', 'X', 'X']:
        print('Крестики победили!')
        return True
    elif check1 == ['0', '0', '0']:
        print('Нолики победили!')
        return True

    check2 = []

    for l in range(3):
        if table[l][1] == 'X':
            check2.append('X')
        elif table[l][1] == '0':
            check2.append('0')

    if check2 == ['X', 'X', 'X']:
        print('Крестики победили!')
        return True
    elif check2 == ['0', '0', '0']:
        print('Нолики победили!')
        return True

    check3 = []

    for m in range(3):
        if table[m][2] == 'X':
            check3.append('X')
        elif table[m][2] == '0':
            check3.append('0')

    if check3 == ['X', 'X', 'X']:
        print('Крестики победили!')
        return True
    elif check3 == ['0', '0', '0']:
        print('Нолики победили!')
        return True

    return False


table = [[' '] * 3 for i in range(3)]

counter = 0
while 1:
    counter += 1
    table_show()
    if counter % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = turn()

    if counter % 2 == 1:
        table[x][y] = 'X'
    else:
        table[x][y] = '0'

    if winner():
        break

    if counter == 9:
        print('Ничья!')
        break
