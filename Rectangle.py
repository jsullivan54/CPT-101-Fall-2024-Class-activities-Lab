# Area of a Rectangle

RECw1= int(input('Please Enter Your 1st Width:'))
RECl1= int(input('Please Enter Your 1st Length:'))
RECw2= int(input('Please Enter Your 2nd Width:'))
RECl2= int(input('Please Enter Your 2nd Length:'))


REC1area= RECw1 * RECl1
REC2area= RECw2 * RECl2


if REC1area > REC2area:
    print('Rectangle 1 is bigger than rectangle 2')
elif REC2area > REC1area:
    print('Rectangle 2 is bigger than rectangle 1')
else:
    print('Both rectangles have the same area')