medial_cause=input('did you have a medial cause Y or N:')
atten=int(input('enter the attendance of the student:'))
if medial_cause=='Y':
    print('you are allowed')
else:
    if atten>=75:
        print('allowed')
    else:
         print('not allowed')