print('half pyramid pattern of star:')
n=int(input('enter the number of rows:'))
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()

rows=int(input('please enter the total number of rows'))
number=1
print('floyd triangle')
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(number,end='')
        number=number+1
    print()