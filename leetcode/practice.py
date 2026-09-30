print("hello!")
a = [9, 6, 0, 8, 1, 6]
print(sorted(a))
"hello"[::-1]

# Arithematic Operators:
# Addition : 3 + 2
# Subtraction : 3 - 2
# Multiplication : 3 * 2
# Division : 3 / 2
# Floor Division : 3 // 2
# Exponent : 3 ** 2
# Modulus : 3 % 2

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)
print(3**2)
print(3%2)
print(abs(-5))
print(round(3.75))
print(round(3.75, 1))


n_1 = '100'
n_2 = '200'
print(n_1 + n_2)

n_1 = int(n_1)
n_2 = int(n_2)
print(n_1 + n_2)


## List ##
print("--------------------List---------------------")

courses = ['Math', 'History', 'English']
print(courses)
print(courses[2])
print(courses[-1])  #last item in the list
print(courses[2:])

## add a item into the list
courses.append('art')
courses.insert(4, 'Korea')
courses.insert(0, 'physics')

courses_2 = ['Spanish', 'communication']

courses.insert(0, courses_2)
courses.extend(courses_2)   # extend : each individual items are added at the end of the list

courses.remove(courses_2)
courses.remove('Spanish')

courses.pop()   # pop : remove the last element in the list


## Sort the list ##
courses.reverse()    # reverse the list
courses.sort()  # string's in order alphabetically


nums = [4, 3, 6, 1, 9, 0]
nums.sort()

# sort in decending order
courses.sort(reverse=True)
nums.sort(reverse=True)

sorted_courses = sorted(courses)


## MIN, MAX, SUM ##
min(nums)
max(nums)
sum(nums)


# find the index of the item in the list
courses.index('Math')
'art' in courses
'Spanish' in courses

# for loop
for item in nums:   # print the elements in the list
    item

for index, course in enumerate(courses):    # print the the index and element in the list
    index, course

for index, num in enumerate(nums, start=1): # start with index 1
    index, num

# seperated by a certain value
course_str = ' - '.join(courses)
new_list = course_str.split(' - ')  # the list seperated by ' - ' turns into the original list


## mutable, immutable ##
# 1. mutable - list
list_1 = ['apple', 'banana', 'melon', 'cherry', 'orange']
list_2 = list_1

list_1[0] = 'water melon'   #replace the element of index 0 in list_1 into the other word

# 2. immutable - tuple
tuple_1 = ['red', 'yellow', 'blue', 'black']
tuple_2 = tuple_1

tuple_1[0] = 'purple'


## Sets ##
cs_courses = {'Data Structure', 'Machine Learning', 'Algorithm', 'Math'}
art_courses = {'Data Structure', 'Art', 'Algorithm', 'Design', 'Math'}


'Math' in cs_courses

cs_courses.intersection(art_courses)    # courses in common 
cs_courses.difference(art_courses)  # different course from art
art_courses.difference(cs_courses)  # different course from cs
cs_courses.union(art_courses)   # combine both courses


## Empty Lists, Tuples, Sets ##
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # it isn't rifght!!!!!! it is dict
empty_set = set()


print(cs_courses)
print(tuple_1)
print(tuple_2)
print(list_1)
print(list_2)
print(courses)
print(nums)
print(course_str)
print(new_list)