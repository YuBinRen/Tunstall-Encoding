#select a letter only once per message.
#considered a 474% improvement, not accounting for entropy

import random
secure_random = random.SystemRandom()
code = "spacewars"
space = 0
dictionary = {}

def encoding(code):
    global space
    global dictionary
    print('code: ' + code)
    for i in code:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
        space += 1
    return dictionary

def decode():
    temp = dictionary.copy()
    output = ''
    key = []
    for i in temp:
        key.append(i)
    for i in range(space):
        while True:
            try:
                select = secure_random.choice(key)
                temp[select] -= 1
                if temp[select] <= 0:
                    temp.pop(select)
                output += select
                break
            except:
                continue
    return output

encoding(code)
print(dictionary)

communication = False
messages_sent = 0
while communication == False:
    message = decode()
    print('message received: ' + message)
    messages_sent += 1
    if message == code:
        communication = True
print('messages sent: ' + str(messages_sent))