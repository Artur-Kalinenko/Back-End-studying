try:
    some_file = open('test2.txt', 'r')
    content = some_file.read()
    some_file.close()
    print('File text: ', content)
except FileNotFoundError:
    print('File was not found')