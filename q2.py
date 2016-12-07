
BUTTON_PAD = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
EVIL_BUTTON_PAD = [['', '', '1', '', ''], ['', '2', '3', '4', ''], ['5', '6', '7', '8', '9'], ['', 'A', 'B', 'C', ''], ['', '', 'D', '', '']]
Y = 0
X = 1

def getMove(c):

    if c in ['D', 'R']:
        move = 1
    else:
        move = -1

    if c in ['U', 'D']:
        axis = Y

    else:
        axis = X

    return (axis, move)


def question2a():
    code = []
    position = [1, 1]

    with open('q2Input.txt', 'r') as f:
        inputData = [line.strip() for line in f.readlines()]

    for row in inputData:
        for c in row:
            (axis, move) = getMove(c)
            if position[axis] + move < 0:
                position[axis] = 0
            elif position[axis] + move > 2:
                position[axis] = 2
            else:
                position[axis] += move

        code.append(BUTTON_PAD[position[0]][position[1]])


    return (''.join(code))


def question2b():

    code = []
    position = [2, 0]

    with open('q2Input.txt', 'r') as f:
        inputData = [line.strip() for line in f.readlines()]

    for row in inputData:
        for c in row:
            (axis, move) = getMove(c)
            if position[axis] + move < 0:
                position[axis] = 0
            elif position[axis] + move > 4:
                position[axis] = 4
            else:
                position[axis] += move

                if EVIL_BUTTON_PAD[position[0]][position[1]] == '':
                    position[axis] -= move

        code.append(EVIL_BUTTON_PAD[position[0]][position[1]])


    return (''.join(code))



if __name__ == "__main__":

    print (question2a())

    print (question2b())