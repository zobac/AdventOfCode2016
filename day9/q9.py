import re
import itertools

markerInputs = re.compile(r"\d+")

def getMarkerInputs(marker):

    return [int(i) for i in markerInputs.findall(marker)]

notStart = lambda c : c != '('
notEnd = lambda c : c != ')'

def question1():
    
    decompressedLength = 0

    with open('q9Input.txt', 'r') as f:
        # no need to read each line individually
        # create an iterator of the data so we can track where we are
        # as we read through it
        inputData = iter(''.join([l.strip() for l in f.readlines()]))

    try:
        while True:

            # read until we hit a '(' char
            decompressedLength += len(list(itertools.takewhile(notStart, inputData)))

            # extract the marker and the marker data
            marker = ''.join(itertools.takewhile(notEnd, inputData))
            (sub, repeat) = getMarkerInputs(marker)

            # activate the marker
            decompressedLength += len(list(itertools.islice(inputData, sub))) * repeat

    except ValueError:
        # reached end of iterator
        pass

    return decompressedLength


def question2(inputData):

    decompressedLength = 0
    
    try:
        while True:

            # read until we hit a '(' char
            decompressedLength += len(list(itertools.takewhile(notStart, inputData)))

            # extract the marker and the marker data
            marker = ''.join(itertools.takewhile(notEnd, inputData))
            (sub, repeat) = getMarkerInputs(marker)

            # activate the marker recursively
            decompressedLength += question2(itertools.islice(inputData, sub)) * repeat

    except ValueError:
        # reached end of iterator or maximum recursion, time unstack
        return decompressedLength


if __name__ == "__main__":

    print(question1())
    
    with open('q9Input.txt', 'r') as f:
    # no need to read each line individually
    # create an iterator of the data so we can track where we are
    # as we read through it
        inputData = iter(''.join([l.strip() for l in f.readlines()]))

    print(question2(inputData))
