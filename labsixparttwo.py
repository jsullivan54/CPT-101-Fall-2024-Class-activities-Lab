
#Johnathan Sullivan AKA Bruce_Wayne_Jung

#lab6part2 Flowchart Program

#This program takes a basic input from the end user and display an output according to their selection


#This is where the program begins
print(f'Hello, Mr. Wayne_Jung.')
#letter a
letter_a= int(input('Please Enter a Number for Letter A:'))
#Letter b
letter_b= int(input('Please Enter a Number for Letter B:'))
#letter c
letter_c= int(input('Please Enter a Number for Letter C:'))

#Now let's see which is greater, or determine which should be printed to Mr.Wayne_Jung

if letter_a  > letter_b and letter_a > letter_c:
    print(letter_a)

else letter_a < letter_c:
    print(letter_c)

if letter_a < letter_b and letter_b > letter_c:
    print(letter_b)

else letter_b < letter_c:
    print(letter_c)


