import os
def cr_file():
    file = open('Holms.txt', 'w')
    file.write('Hello, Mr. Holmes')
    file.close()

def ch_file():
    file = open('Holms.txt', 'w')
    file.write('Hello, Mr. Sherlock Holmes!')
    file.close()

def add_to_file(path, s):
    try:
        file = open(path, 'a+')
        file.write(s)
        file.close()
    except FileNotFoundError:
        print('Невозможно открыть файл')

#cr_file()
#ch_file()
add_to_file('G:/PyProjects/FileWork/Holms.txt', 'Hello')
