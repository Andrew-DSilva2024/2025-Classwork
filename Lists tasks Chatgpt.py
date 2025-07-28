'''Beginner-Level Questions
Create a List
Write a Python program to create a list of 5 integers and print it.

Access Elements
Given a list colors = ['red', 'green', 'blue'], print the first and last elements.

List Length
Write a function that takes a list and returns the number of items in it.

List Append
Create an empty list and append five numbers (input by user) to it.

Slicing
Given nums = [10, 20, 30, 40, 50], print a sublist containing the second to fourth elements.

🔸 Intermediate-Level Questions
List Comprehension
Use list comprehension to generate a list of squares of numbers from 1 to 10.

Sum of Elements
Write a function to calculate the sum of all the elements in a list.

Remove Duplicates
Write a Python function that removes duplicates from a list.

Count Occurrences
Given a list of words, count how many times a specific word appears.

Sort a List
Write a program to sort a list of strings in alphabetical order.

🔺 Advanced-Level Questions
Flatten Nested List
Write a function to flatten a nested list like [[1, 2], [3, 4], [5]] into [1, 2, 3, 4, 5].

Rotate List
Write a function to rotate a list to the right by k steps.

List Intersection
Write a function that returns the intersection of two lists (common elements).

Find Pairs with Target Sum
Given a list of integers, return all unique pairs that sum up to a specific target.

Custom Sort
Sort a list of tuples based on the second value in each tuple.
Example: [(1, 3), (2, 2), (3, 1)] → [(3, 1), (2, 2), (1, 3)]'''

#basic
def create_a_list():
    list = ['ighig', 'ffihf']
    print(list)

def access_elements():
    colours = ['red', 'green', 'blue']
    print(colours[0])
    print(colours[-1])

def list_length():
    list = ['red', 'green', 'blue', 'green']
    print(len(list))

def list_append():
    list = []
    for i in range(5):
        flag = True
        while flag:
            try:
                number = float(input('Enter a number: '))
                list.append(number)
                flag = False
            except ValueError:
                print('Please enter an a number in ineteger form')
    print(list)

def slicing():
    list = [10, 20, 30, 40, 50]
    sublist = []
    sublist.append(list[1])
    sublist.append(list[3])
    print(sublist)

#intermediate
def list_comprehension():
    list = []
    for i in range(10):
        i = i+1
        square = i*i
        list.append(square)
    print(list)

def andy_list_comprehension():
    list = []
    for number in range(10):
        i = 0
        while i != number + 1:
            if number == i*i:
                list.append(number)
            i += 1
    print(list)

def sum_of_elements():
    list = [1,5,7,3,4,5]

def rotate_a_list():
    list = [1,2,3,4,5]
    list1 = []
    max = len(list)
    flag = True
    while flag:
        try:
            shift = int(input('How much you want to move the list to the right: '))
            if shift >= max:
                print(f'Number has to be less than {max}')
            elif shift < 0:
                print('Number must be poitive')
            else:
                flag = False
        except ValueError:
            print('Please enter a number numerically (in numbers)')
    i = max - shift
    while i != max:
        list1.append(list[i])
        i += 1
    i = 0
    while i < max-shift:
        list1.append(list[i])
        i += 1
    print(list1)

def sort_tuples():
    tuples = [(3,1),(2,2),(1,3)]
    for number in range(len(tuples)):
        for i in range(len(tuples))
        if tuples[0][1] > 

#main routine
sort_tuples()