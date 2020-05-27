'''
#calculater who add two str & escape sequence
n1 = input('enter first\n\'s number ')
n2 = input('enter secend number ')
t = print(float(n1)+float(n2))
'''
'''
#str sliceing
a = 'hello world'
print(a[5:1:-1])
'''
'''
#list and tuple
b = [1,2,'hlo',(3+4j),'abc',1.3]#mixed data type list
print(b)
'''
'''
#List Comprehension
c = [] #basic
c.append(1)
c.append(2)
c.append(3)
print(c)
'''
'''
#range()function
d = []
for x in range(5):
    d.append(x**2)
    print(d)
'''
'''
#tuple
t = (1,2,3,4,4.2,'abc')
print(t)
'''
'''
#dictionary
d = {'a':1,
'b':2,
     'c':3}
print(d)
'''
'''
#dict with for loop key and value
w = \
    {
    'a':1,
    'b':2,
    'c':3
}
for x,y in w.items():
    print(x,y)
'''
'''
#if else & elif('short hand')
a = 1;b = 2
if a>b: print(type('b is greater than \'a\''))
elif a==b:  print('equal')
else:   print('\'a \' is less than b')
'''
'''
a=12;b=22;print('a') if a > b else print('b')
'''
'''
a=1;b=2;print('A') if a > b else print('B')
'''
'''
#array
array = ['hello','world']
x = array[0]
print(x)
'''
'''
#test
tup = 0,1,2
lst = [tup]
lst.append(3)
lst.pop(0)
print(len(lst))
'''

#test
num = 0
for i in range (5,0,-1):
    num += i > num
print(num)

