a=12
b=10
c=0
if a and b and c:
     print('all the number has boolean value as true')
else:
     print('all the number has boolean value as false')

a=10
b=-10
c=0
if a>0 or b>0:
     print("either the number is greater than 0")
else:
     print('no number is greater than 0')
if b>0 or c>0:
     print('either the number is greater than 0')
else:
     print('no number is greater than 0')

a=10
b=12
c=12
print(a!=b)
print(b!=c)
a="python"
b="coding"
if a!=b:
     print(a,'and',b,'are different')
a=4
b=5
if(a==1)!=(b==5):
     print('hello')
a=int(input('enter the number'))
if a%2!=0:
     print(a,'is not an even number,')

height=float(input('enter your height in m'))
weight=float(input('enter your weight in kg'))
BMI=weight/height**2
print('your BMI is',BMI)
if BMI<=18.4:
     print('you are underweight,')
elif BMI<=24.9:
     print('you are healthy,')
elif BMI<=29.9:
     print('you are over weight,')