import re

COLUMNS = 50
ROWS = 6

getNums = re.compile(r'\d+')

def getInputs(string):
    return [int(n) for n in getNums.findall(string)]

class CrackedDisplay(object):

    def __init__(self):

        self._display = [[' ' for i in range(COLUMNS)] for j in range(ROWS)]


    def rect(self, width, height):

        for y in range(height):
            for x in range(width):
                self._display[y][x] = '#'


    def rotateRow(self, row, count):
        tempList = [' ' for i in range(COLUMNS)]

        for i in range(COLUMNS):
            tempList[(i + count)%COLUMNS] = self._display[row][i]
        self._display[row] = tempList


    def rotateColumn(self, column, count):
        tempList = [' ' for j in range(ROWS)]

        for i in range(ROWS):
            tempList[(i + count)%ROWS] = self._display[i][column]

        for i in range(ROWS):
            self._display[i][column] = tempList[i]


    def __str__(self):
        s = ''
        for row in range(ROWS):
            s += ''.join(self._display[row]) + '\n'
        return s

    def __repr__(self):
        s = ''
        for row in range(ROWS):
            s += ''.join(self._display[row]) + '\n'
        return s

    def getLitPixelCount(self):

        return sum(l.count('#') for l in self._display)

def question1():

    with open('q7Input.txt', 'r') as f:
        inputData = f.readlines()

    d = CrackedDisplay()

    for l in inputData:
        if 'rect' in l:
            width, height = getInputs(l)
            d.rect(width, height)
        elif 'row' in l:
            row, count = getInputs(l)
            d.rotateRow(row, count)
        else:
            column, count = getInputs(l)
            d.rotateColumn(column, count)

        print d

    return d.getLitPixelCount()





if __name__ == '__main__':

    #cd = CrackedDisplay()
    #cd.rect(3, 2)
    #cd.rotateColumn(1,1)
    #cd.rotateRow(0, 4)
    #cd.rotateColumn(1, 1)
    #print(cd)
    print(question1())
