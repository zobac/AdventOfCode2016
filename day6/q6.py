from collections import Counter

def question1():

    with open('q6Input.txt', 'r') as f:
        inputData = f.readlines()

    return ''.join([Counter(row).most_common()[0][0] for row in list(zip(*inputData))])


def question2():

    with open('q6Input.txt', 'r') as f:
        inputData = f.readlines()

    return ''.join([Counter(row).most_common()[-1][0] for row in list(zip(*inputData))])


if __name__ == "__main__":

    print (question1())
    print (question2())
