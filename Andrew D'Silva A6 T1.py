def get_colours():
    colours = []
    print('Please enter 5 colours')
    for i in range(5):
        flag = True
        while flag:
            try:
                colour = input(f'Enter colour {i+1}: ')
                if len(colour) == 0:
                    print('ERROR: Please enter a colour')
                else:
                    colours.append(colour)
                    flag = False
            except ValueError:
                print('ERROR: Please enter a colour')
    return colours

def get_length():
    colours = get_colours()
    for colour in colours:
        print(f'{colour.title()} {len(colour)} characters')
    return

#main routine
get_length()