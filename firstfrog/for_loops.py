
list1 = [['harry',1],['larry',2],['carry',3],['marie',4]]
dict = dict(list1)
for item,lollypop in dict.items():
    for x in ['a','b','c']:
       print(item,'have',lollypop,x,'lollypop')


'''      
import time
print(dir(time))
'''
'''
# Iterate through a list
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)
'''
'''
# Break the loop at 'blue'
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        break
    print(x)
# Prints red green
'''
'''
# Skip 'blue'
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    if x == 'blue':
        continue
    print(x)
'''
'''
# Generate a sequence of numbers from 0 6
for x in range(7):
    print(x)
# Prints 0 1 2 3 4 5 6
'''