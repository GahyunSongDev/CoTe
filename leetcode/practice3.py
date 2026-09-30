## Conditionals and Booleans - If, Else and Elif Statement ##
if True:
    print('Conditional was True.')

language = 'C++'

if language == 'Java':
    print('Language is Java.')
elif language == 'Python':
    print('Language is Python')
else:
    print('No match')


user = 'Admin'
logged_in = True
logged_out = False

if user == 'Admin' or logged_out:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('please log in')
else:
    print('welcome.')

a = [1, 2, 3]
b = [1, 2, 3]
b = a

a == b  # return True
a is b  #return False becase these are two different objects in memory, and you can print out these locations with this build-in ID functon
id(a)
id(b)

id(a) == id(b)

