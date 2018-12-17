import random
code = "spacewars"
space = 0

def encoding(code):
    global space
    print('code: ' + code)
    dictionary = {}
    for i in code:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
        space += 1
    print(dictionary)
    for i in dictionary:
        dictionary[i] = round(dictionary[i] / space, 3)
    print(dictionary)
    return dictionary

def decode(dictionary):
    output = ''
    for i in range(space):
        prob = round(random.randrange(0, 100, 1)/100, 3)
        selection = False
        while selection == False:
            select = 0
            for j in dictionary:
                select += dictionary[j]
                if select > prob:
                    output += j
                    selection = True
                    break
    return output


dict = encoding(code)

communication = False
messages_sent = 0
while communication == False:
    message = decode(dict)
    print('message received: ' + message)
    messages_sent += 1
    if message == code:
        communication = True
print('messages sent: ' + str(messages_sent))