def getNumbers():
    numbers = [20,36,12,24,20,48,74,353,23,98]
    return numbers

def findBiggest():
    numbers = getNumbers()
    for number in numbers:
        for i in numbers:
            if number < i:
                number = i
    print(number)
    return

#main
findBiggest()