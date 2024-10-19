#Johnathan Sullivan_aka_Bruce_Wayne-Jung

#A bug collector collects bugs every day for five days. /

#Write a program that keeps a running total of the number of bugs collected during the five days. /

#The loop should ask for the number of bugs collected for each day, and when the loop is finished, /

#the program should display the total number of bugs collected.
bug_total = 0
for day in range (5):
    num_bugs = int(input(f'Enter number of bugs collected for day {day+1}: '))
    bug_total += num_bugs
print(f'\nTotal bugs collected: {bug_total}')
print('=======================')





