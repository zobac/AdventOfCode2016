import re
from itertools import *
from sys import stdin
from collections import defaultdict


def question1():

    destinations = re.compile('to (\w+)')
    numbers = re.compile(r'(\d+)')
    getnumbers = lambda s: map(int, numbers.findall(s))

    bots = defaultdict(list)
    outputs = defaultdict(list)

    done = []

    with open('q10Input.txt', 'r') as f:
        lines = f.readlines()

    # Keep looping over lines until each rule has been resolved

    while len(done) < len(lines):
        for line in lines:
            # Skip lines we've already processed
            if line in done:
                continue

            # If it's a 'value' line we can always process it
            if line.startswith('value'):
                [v, bot] = getnumbers(line)
                bots[bot].append(v)
                # print 'added', v
                done.append(line)
                continue

            # Figure out who gets what
            [lowDest, highDest] = destinations.findall(line)
            [source, lDest, hDest] = getnumbers(line)

            # Get the numbers the bot carries
            ns = bots[source]

            # This satisfies question 1.  Bail out!
            if 61 in ns and 17 in ns:
                return(source)

            # If we don't have 2 numbers, then we haven't processed enough info yet,
            # come back later
            if len(ns) < 2:
                continue

            # Get low and high
            low = min(ns)
            high = max(ns)

            # Delegate our microchips
            if lowDest.startswith('out'):
                outputs[lDest].append(low)
            else:
                bots[lDest].append(low)
            if highDest.startswith('out'):
                outputs[hDest].append(high)
            else:
                bots[hDest].append(high)

            done.append(line)


def question2():

    destinations = re.compile('to (\w+)')
    numbers = re.compile(r'(\d+)')
    getnumbers = lambda s: map(int, numbers.findall(s))

    bots = defaultdict(list)
    outputs = defaultdict(list)

    done = []

    with open('q10Input.txt', 'r') as f:
        lines = f.readlines()

    # Keep looping over lines until each rule is done

    while len(done) < len(lines):
        for line in lines:
            # Skip lines we've already processed
            if line in done:
                continue

            # If it's a 'value' line we can always process it
            if line.startswith('value'):
                [v, bot] = getnumbers(line)
                bots[bot].append(v)
                # print 'added', v
                done.append(line)
                continue

            # Figure out who gets what
            [lowDest, highDest] = destinations.findall(line)
            [source, lDest, hDest] = getnumbers(line)

            # Get the numbers the bot is holding
            ns = bots[source]

            # If we don't have 2 numbers, then we haven't processed enough info yet,
            # come back later
            if len(ns) < 2:
                continue

            # Get low and high
            low = min(ns)
            high = max(ns)

            # Delegate our microchips
            if lowDest.startswith('out'):
                outputs[lDest].append(low)
            else:
                bots[lDest].append(low)
            if highDest.startswith('out'):
                outputs[hDest].append(high)
            else:
                bots[hDest].append(high)

            done.append(line)

    return outputs[0].pop() * outputs[1].pop() * outputs[2].pop()


if __name__ == "__main__":

    print(question1())
    print(question2())