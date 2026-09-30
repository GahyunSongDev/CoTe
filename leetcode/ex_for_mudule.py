##import my_module when it's in the same dicr
#from my_module import find_index, test
#import sys  # when it's in different dirc
#sys.path.append('') 

import random
import math
import datetime
import calendar
import os
import antigravity

courses = ['History', 'Math', 'Physics', 'CompSci']

#index = find_index(courses, 'CompSci')
#print(index)
#print(test)

random_course = random.choice(courses)

rads = math.radians(90)

today = datetime.date.today()


print(os.__file__)
print(os.getcwd())
print(calendar.isleap(2023))
print(today)
print(rads)
print(math.sin(rads))
print(random_course)

