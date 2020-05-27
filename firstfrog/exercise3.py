n1 = int(input('first number '))
n2 = int(input('second number '))
n3 = input('what you want' + '+,-,/,%,* ')
if n1==45 and n2==3 and n3=='*':
    print('555')
elif n1==3 and n2==45 and n3=='*':
    print('555')
elif n1 == 56 and n2 == 9 and n3 == '+':
    print('77')
elif n1==9 and n2==56 and n3=='+':
    print('77')
elif n1==56 and n2==6 and n3=='/':
    print('4')
elif n1==6 and n2==56 and n3=='/':
    print('4')
elif n3=='+':
    plus = n1 + n2
    print(plus)
elif n3=='-':
    minus = n1-n2
    print(minus)
elif n3=='/':
    devide = n1/n2
    print(devide)
elif n3=='*':
    multi = n1*n2
    print(multi)
elif n3=='%':
    percent = n1%n2
    print(percent)
else:'unpexted error!'