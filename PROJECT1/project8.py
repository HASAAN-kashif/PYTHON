a = 1
b = 2
c = 3
print("Before swapping:", a, b, c)
a, b, c = c,b, a
print("After swapping:", a, b, c)

age=int(input('enter your age'))
if 10>=age<=20:
    print('you are allowed to enroll')
else:
    print('you are not allowed to enroll')