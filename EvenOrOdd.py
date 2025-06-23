def getNum():
    flag = True
    while flag == True:
        try:
            num = int(input('Tell me a number and I will tell you if it is even: '))
            flag = False
        except ValueError:
            print('Please enter a valid value')
    return num

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def value():
    num = getNum()
    even = isEven(num)
    if even == True:
        print(f'{num} is even')
    else:
        print(f'{num} not even')
    return

#main routine
value()