#MAGIC DATES


MONTH= int(input('Please Enter a Month (in Numeric Form):'))

DAY= int(input('Please Enter a Day:'))

YEAR= int(input('Please Enter a Two-Digit Year:'))

Specialday= MONTH * DAY
if Specialday == YEAR:
    print('Your Date is Magic!!!')
else: print('Your date is MUNDANE!!!')