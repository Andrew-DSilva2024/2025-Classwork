def getSubjects():
    subjects = ['Mathmatics', 'Enlgish', 'Biology', 'Physics', 'Religious-Education', 'Physical-Education', 'Comuputer-Science']
    for subject in subjects:
        print(subject)
    return subjects

def newSubjects():
    subjects = getSubjects()
    new_subjects = input('Any other subjects you would like to take: ')
    while new_subjects != '':
        new_subjects = new_subjects.title()
        subjects.append(new_subjects)
        new_subjects = input('Any other subjects you would like to take: ')
    return subjects

def allSubjects():
    subjects = newSubjects()
    subjects.sort()
    for subject in subjects:
        print(subject)
    return

#main
allSubjects()

