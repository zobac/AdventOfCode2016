import hashlib


def question1(inputData):

    password = ''
    index = 0
    while len(password) < 8:
        current = bytearray(inputData + str(index), 'utf-8')
        digest = hashlib.md5(current).hexdigest()

        if digest[:5] == '00000':
            password += digest[5]

        index += 1

    print('Question1: %s itterations' %index)
    return password

def question2(inputData):

    password = [None, None, None, None, None, None, None, None]
    index = 0
    while not all(password):
        current = bytearray(inputData + str(index), 'utf-8')
        digest = hashlib.md5(current).hexdigest()

        if digest[:5] == '00000':
            try:
                ind = int(digest[5])
            except ValueError: # can't int hex a-f
                pass

            try:
                if password[ind] is None:
                    password[ind] = digest[6]
            except IndexError: # index out of range
                pass

        index += 1

    print('Question2: %s itterations' %index)
    return ''.join(password)



if __name__ == "__main__":

    inputData = "uqwqemis"
    print (question1(inputData))
    print (question2(inputData))
