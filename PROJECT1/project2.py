x=5
if (type(x)is int):
    print('true')
else:
    print('false')
x=5.0
if type(type(x)is not float):
    print('true')
else:
    print('false')
x=20
y=20
if (x is y):
    print('x & y SAME IDENTITY')
Y=30
if (x is not y):
    print('x & y have different identity')

a=10
b=-10
#print bitwise right shift operator
print('a << 1=',a << 1)
print('b << 1=',b << 1)
a=5
b=-10
# print bitwise left shift operator
print('a << 1=',a << 1)
print('b << 1=',b << 1)

print('enter the marks obtained in 5 sub')
markone= int(input())
marktwo= int(input())
markthree= int(input())
markfour= int(input())
markfive= int(input())
tot=markone+marktwo+markthree+markfour+markfive
avg=tot/5
if avg>=91 and avg<=100:
    print('your grade is A1')
elif avg>=81 and avg<=91:
    print('your grade is A2')
elif avg>=71 and avg<=81:
    print('your grade is B1')
elif avg>=61 and avg<71:
    print('your grade is B2')
elif avg>=51 and avg<61:
    print('your grade is C1')
else:
    print('invalid')