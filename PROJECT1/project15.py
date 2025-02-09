num=int(input('enter a number:'))
sum=0
length=len(str(num))
temp=num
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp//=10
if num==sum:
    print(num,'is an palindrome')
else:
    print(num,'is not an palindrome')

n=int(input('enter the number'))
a=0
print(a)
b=1
print(b)
for c in range(n-2):
    c=a+b
    a=b
    b=c