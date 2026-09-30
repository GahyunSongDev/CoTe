## looping - break, continue, inner for-loop,  ##

nums = [1, 'john', 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(10):
    i   # Start from 0

for i in range(1, 11):  # start from 1, end with 10
    i

x = 0

while x < 10:
    print(x)
    x +=1

while x < 10:
    if x == 5:
        break
    print(x)
    x +=1

while True:
    if x == 5:
        break
    print(x)
    x +=1