def getNum():
    flag = True
    while flag:
        try:
            number = int(input('Input a number to find its factorial: '))
            if number < 0:
                print('Number must be larger or equal to 0')
            else:
                flag = False
        except ValueError:
            print('Number must be whole and numerical')
    return number

def findFactorial(number):
    factorial_number = 1
    for i in range(number):
        i += 1
        factorial_number = factorial_number * i
    return factorial_number

def showFactorial(factorial_number):
    print(f'The factorial is {factorial_number}')

    
#main routine
num = getNum()
fact_num = findFactorial(num)
showFactorial(fact_num)