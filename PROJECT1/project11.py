n=int(input('enter the value of n:'))
print('number from {0} to {1} are'.format(n,1))
for i in range(n,0,-1):
    print(i)

msg=input('enter the message')
count=0
for c in msg:
    count=count+1
print('count=',count)
