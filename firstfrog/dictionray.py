#d = {}
#print(type(d))
'''
d2 = {'ashok':'boy','boy':'human','human':'becteria'}
#print(d2['ashok'])
d2['pawan'] = 'junk food '
d2['amar'] = 'soup'
del d2['amar']
print(d2)
'''

'''
other ways to create dict
#dict...............
a = {'name':'ashok',
    'unit':'1 jak rif',
    'coy':'alpha',
    'pl':3}
print(a)
'''
'''
#dict  list.................
b =[ ('name','ashok'),
     ('unit','1jak rif'),
     ('coy','alpha'),
     ('pl',3)]
print(b)
'''
'''
#swap-using for swap value........
a = 1
b = 2
a,b = b,a
print(a,b)
'''
'''
#default value for each keys........
keys = ['a','b','c']
defaultvalue = 0
d = dict.fromkeys(keys,defaultvalue)
print(d)
'''
'''
f = {'harry':'burger',
     'aman':'roti',
     'pawan':{'b':'maggie','c':'ice'}}
f.update({'harry':'maal'})
print(f.copy())
'''
'''
x = 10
z = int(input('enter value'))
if x>z:
     print('true')
elif x==z:
     print('=')
else:
     print('False')
'''
