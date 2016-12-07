import collections

def question1():

    with open('q6Input.txt', 'r') as f:
        inputData = f.readlines()

    return ''.join([collections.Counter(r).most_common()[0][0] for r in list(zip(*inputData))])


def question2():

    with open('q6Input.txt', 'r') as f:
        inputData = f.readlines()

    return ''.join([collections.Counter(r).most_common()[-1][0] for r in list(zip(*inputData))])


if __name__ == "__main__":

    print (question1())
    print (question2())
