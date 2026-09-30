## Functions ##

def hello_func():
    print('hello, functions!')

def hello_func():
    return 'Hello Functons!'

def hello_func(greeting):   # In order to use this function, you need one arguement when you use that.
    return f'{greeting} Functions.'

def hello_func(greeting, name):
    return f'{greeting}, {name} :) Nice to meet you ! '


hello_func('Hey', 'Allie')
hello_func().upper()

def student_info(*args, **kwargs):  # as many parameters as you want
    print(args) # values without name as tuple
    print(kwargs)   #values with name as dictionary

courses = ['Math', 'Art', 'History']
info = {'name': 'Jone', 'age': 29}

student_info(*courses, **info)

student_info('Math', 'Art', name = 'Allie', age = 30 )