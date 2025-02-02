medial_cause=input('did you have a medial cause Y or N:')
atten=int(input('enter the attendance of the student:'))
if medial_cause=='Y':
    print('you are allowed')
else:
    if atten>=75:
        print('allowed')
    else:
         print('not allowed')

units=int(input('please enter the number of unit you consumed:'))
if (units<50):
    amount=units*2.60
    surcharge=25
elif(units<=100):
    amount=130+((units-50)*3.25)
    surcharge=35
elif(units<=200):
    amount=130+162.50+((units-100)*5.26)
    surcharge=45
else:
    amount=130+162.50+526+((units-200)*8.45)
    surcharge=75
total=amount+surcharge
print('electricity bill-%2f'%total)