

def getTurn(d):
    if d == 'R':
        return 1
    return -1

def question1a():

    directions = [1, 1, -1, -1]
    orientation = 0 # start facing north
    location = [0, 0]

    # to store each point we've passed through
    visited = []

    with open('q1Input.txt', 'r') as f:
        inputData = [(s[0], int(s[1:])) for s in f.read().split(', ')]

    revisited = False
    for move, count in inputData:

        # spin the compass
        orientation += getTurn(move)
        if orientation < 0:
            orientation = 3
        elif orientation > 3:
            orientation = 0

        #set the new location
        location[orientation % 2] += directions[orientation] * count

    # how far away are we?
    return (abs(location[0]) + abs(location[1]))


def question1b():

    directions = [1, 1, -1, -1]
    orientation = 0 # start facing north
    location = [0, 0]

    # to store each point we've passed through
    visited = []

    with open('q1Input.txt', 'r') as f:
        inputData = [(s[0], int(s[1:])) for s in f.read().split(', ')]

    revisited = False
    for move, count in inputData:

        # spin the compass
        orientation += getTurn(move)
        if orientation < 0:
            orientation = 3
        elif orientation > 3:
            orientation = 0

        # store each point we visit
        for c in range(count):
            location[orientation % 2] += directions[orientation]

            # quit if we've been here before
            if (location[0], location[1]) in visited:
                revisited = True
                break

            visited.append((location[0], location[1]))

        # No really, quit if we've been here before
        if revisited:
            break

    return (abs(location[0]) + abs(location[1]))



if __name__ == '__main__':

    print (question1a())
    print (question1b())