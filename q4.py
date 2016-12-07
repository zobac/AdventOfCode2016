import re
import collections
import string
import itertools

ALPHABET = list(string.ascii_lowercase)
splitPattern = re.compile('([a-z-]+)(\d+)\[(.+)\]')

def decryptChar(c, count):
    if c == " ":
        return c

    cycle = itertools.cycle(ALPHABET[ALPHABET.index(c):] + ALPHABET[:ALPHABET.index(c)])
    for _ in range(count):
        next(cycle)
    return next(cycle)


def getLegitNamesAndIds():
    legitNames = []

    with open('q4Input.txt', 'r') as f:
        inputData = f.readlines()

    for row in inputData:

        seemsLegit = True

        name, sectorId, checksum = splitPattern.match(row).groups()
        name = name.replace('-', '')

        counter = collections.Counter(name)
        sortedName = counter.most_common()

        for index, c in enumerate(checksum):

            if c not in counter:
                seemsLegit = False
                break

            if c == sortedName[index][0]:
                continue

            elif sortedName[index][1] == counter[c]:
                continue

            else:
                seemsLegit = False
                break

        if seemsLegit:
            legitNames.append((name, int(sectorId)))

    return legitNames


def question1():

    keyCode = 0
    for name, count in getLegitNamesAndIds():
        keyCode += count

    return keyCode


def question2():
    sectorId = None

    for name, count in getLegitNamesAndIds():

        decryptedName = ''

        for c in name:
            decryptedName += decryptChar(c, int(count))

        if 'northpole' in decryptedName:
            sectorId = count

    return sectorId


if __name__ == "__main__":

    print (question1())
    print (question2())
