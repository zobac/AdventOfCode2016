
import itertools

def getMissing(fullset, subset):
    l = fullset.copy()
    for i in subset:
        try:
            l.remove(i)
        except:
            pass
    return l[0]


def findsubsets(verticesList, size):
    return list(itertools.combinations(verticesList, size))



def question1():
    validCount = 0
    with open('q3Input.txt', 'r') as f:
        inputData = [line.split() for line in f.readlines()]

    for row in inputData:

        row = [int(c) for c in row]
        boo = False
        for ss in findsubsets(row, 2):
            if  ss[0] + ss[1] <= getMissing(row, ss):
                boo = True
                break

        if not boo:
            validCount += 1

    return validCount


def question2():

    validCount = 0
    with open('q3Input.txt', 'r') as f:
        inputData = list(zip(*[line.split() for line in f.readlines()]))

    for row in inputData:
        row = [int(c) for c in row]
        vertexList = [row[i:i + 3] for i in range(0, len(row), 3)]
        for v in vertexList:
            boo = False
            for ss in findsubsets(v, 2):
                if  ss[0] + ss[1] <= getMissing(v, ss):
                    boo = True
                    break

            if not boo:
                validCount += 1

    return validCount


if __name__ == "__main__":

    print (question1())
    print (question2())
