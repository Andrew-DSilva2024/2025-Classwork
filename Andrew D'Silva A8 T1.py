def getTheNames():
    global names
    name = input('Enter a name: ').lower().strip()
    while name != '':
        if name in names:
            names[name] = names[name] + 1
        else:
            names[name] = 1
        name = input('Enter a name: ').lower().strip()
    return names

def printTheNames():
    global names
    print('Names annd ocurrences are: ')
    for name, occurence in names.items():
        print(f'{name} occured {occurence} times')

#main routine
names = {}
getTheNames()
printTheNames()