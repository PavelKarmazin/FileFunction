def cr_file(text):
    file = open('Holms.txt', 'w')
    file.write(text)
    file.close()

def ch_file():
    L = []
    file = open('Holms.txt', 'a+')
    for line in open('Holms.txt', 'r'):
        L.append(line)
    a = L[0]
    newString = a[ :11] + "Sherlock " + a[11:] + "!"
    file = open('Holms.txt', 'w')
    file.write(newString)
    file.close()
            

def add_to_file(path, s):
    try:
        file = open(path, 'a+')
        file.write(s)
        file.close()
    except FileNotFoundError:
        print('Невозможно открыть файл')

cr_file('Hello, mr. Holmes')
ch_file()
#add_to_file('G:/PyProjects/FileWork/Holms.txt', 'Hello')
