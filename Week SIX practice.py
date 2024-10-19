#This is Week SIX Pracitce
#This program allows a user to enter and number and display the ROMAN numeral for this

#NAMED CONSTANTS

NUMBER=int(input('Enter a number 1-10:'))

if NUMBER>10:
    print(f'Error!')
elif NUMBER==10:
    print(f'Your Number in Roman: X')
elif NUMBER==9:
    print(f'Your Number in Roman: IX')
elif NUMBER==8:
    print(f'Your Number in Roman:VIII')
elif NUMBER==7:
    print(f'Your Number in Roman:VII')
elif NUMBER==6:
    print(f'Your Number in Roman:VI')
elif NUMBER==5:
    print(f'Your Number in Roman:V')
elif NUMBER==4:
    print(f'Your Number in Roman:IV')
elif NUMBER==3:
    print(f'Your Number in Roman:III')
elif NUMBER==2:
    print(f'Your Number in Roman:II')
elif NUMBER == 1:
    print(f'Your Number in Roman:I')