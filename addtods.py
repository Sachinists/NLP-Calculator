def add_element(string):
    path = '/Users/ChiefAmay/Desktop/calculator/addition.txt'
    addfile = open(path,'r')
    init = addfile.readlines()
    updated = ""
    string += "\n"
    if string not in init:
        addfile = open(path,'r')
        updated = addfile.read()
        updated +=string
        addfile = open(path,'w')
        addfile.write(updated)
    addfile.close()

def input_to_file():
    n = input('Enter number of test cases to add: ')
    for w in range(int(n)):
        question = input('Enter the question: ')
        answer = input('Enter the result: ')
        add_element(str(question+'\t'+answer))

##input_to_file()
