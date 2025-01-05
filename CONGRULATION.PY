msg=input('enter your message')
print(msg.upper())
#storage value
tree1=98
tree2=94
tree3=95
tree4=92
tree5=11
#finding total of trees
sum=tree1+tree2+tree3+tree4+tree5
print('the sum of all the 5 trees is:',sum)
#finding the average of trees
average=sum/5
print('the average of all the tree is :',average)
#taking total amount as inout from user
amount=int(input('please enter amount for withdraw:'))
#calculating the number of notes of different denomination
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print('notes of 100 rupees',note_1)
print('notes of 50 rupees',note_2)
print('notes of 10 rupees',note_3)
#take marks as input from user
print('enter marks obtained in 4 subjects:')
math=int(input('maths:'))
english=int(input('english:'))
science=int(input('science:'))
hindi=int(input('hindi:'))
#let the calculate the percentage of the marks
sum=math+english+science+hindi
print('sum of math,english,science and hindi')
perc=(sum/400)*100
print(perc)
