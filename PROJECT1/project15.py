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