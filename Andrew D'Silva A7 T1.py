def getWords():
    words = []
    flag = True
    while flag:
        line = input('Enter a word: ')
        line = line.rstrip()
        if line != '':
            if ' ' in line:
                print('ERROR: Enter only one word at a time!')
            elif line.lower() not in words:
                words.append(line.lower())
        else:
            flag = False
    return words

def printSummary():
    if len(words) == 1:
        print(f'You know {len(words)} unique word!')
    else:
        print(f'You know {len(words)} unique words!')
    return

#main routine
global words
words = getWords()
printSummary()