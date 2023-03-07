import sys

def say_hello(num, lang):
    if lang == 'english':
        for i in range(num):
            print('Hello')
    elif lang == 'chinese':
        for i in range(num):
            print('你好')
    else:
        print('Unsupported language')

num = int(input("Please enter the  number:"))
lang = input("Please enter the language:")

say_hello(num, lang)

input("Press Enter to exit...")