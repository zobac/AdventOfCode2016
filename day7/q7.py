import re
import itertools

abba = re.compile(r'(?=(\w)(\w)\2\1)')
aba = re.compile(r'(?=(\w)(\w)\1)')
parethesisFilter = re.compile(r'\[.*?\]')

def checkValid(a, b):
    return a != b

def hasBAB(a, b, text):

    return '%s%s%s' %(b, a, b) in text

def question1():

    count = 0

    with open('q7Input.txt', 'r') as f:
        inputData = f.readlines()

    for l in inputData:

        parenthesisText = parethesisFilter.findall(l)
        potentialFails = itertools.chain.from_iterable([abba.findall(m) for m in parenthesisText])
        if any(checkValid(a, b) for a, b in potentialFails):
            continue

        if any(checkValid(a, b) for a, b in abba.findall(l)):
            count += 1

    return count


def question2():

    count = 0

    with open('q7Input.txt', 'r') as f:
        inputData = f.readlines()

    for l in inputData:
        parenthesisText = parethesisFilter.findall(l)

        for pt in parenthesisText:
            l = l.replace(pt, ' ')

        for (a, b) in aba.findall(l):
            if checkValid(a, b) and any([hasBAB(a, b, text) for text in parenthesisText]):
                print(parenthesisText)
                print(b,a,b)
                count += 1
                break

    return count


if __name__ == '__main__':

    print(question1())
    print(question2())
