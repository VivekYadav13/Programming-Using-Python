'''
A word processing system sometimes needs to shorten a word to make it fit on a line. Write a function that takes a string containing a single word and decides where to hyphenate it. A hyphen can occur before the endings: “ing,” “ed,” “ate,” “tion,” or “ment.” It could also occur after a prefix: “pre,” “post,” “para,” “pro,” “con,” or “com.” Otherwise, place a hyphen somewhere in the middle of the word. The function should return a tuple containing the first and second half of the word split at the hyphen.
'''

def replace_end(str):
    end = ['ed', 'ing', 'ment', 'ate', 'tion']
    for i in range(len(end)):
        if end[i] in str[len(str)-len(end[i]):]:
            str = str[:len(str)-len(end[i])] + '-' + end[i]
    return str


def replace_start(str):
    start = ['pre', 'post', 'para', 'pro', 'con', 'com']
    for i in range(len(start)):
        if start[i] in str[:len(start[i])]:
            str = start[i] + '-' + str[len(start[i]):]
    return str


string = input("Enter your word: ")
if replace_start(replace_end(string)) == string:
    string = string[:int(len(string)/2)] + '-' + string[int(len(string)/2):]
else:
    string = replace_start(replace_end(string))
print("Hyphenated word is:", string)
