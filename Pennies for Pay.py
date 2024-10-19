#Johnathan Sullivan_aka_Bruce_Wayne-Jung
#This program calculates the amount of money a person would earn over a period of time if his or her salary is /
#one penny the first day, two pennies the second day, and continues to double each day. /
#The program asks the user for the number of days. Displays a table showing what the salary was for each day, /
#then shows the total pay at the end of the period. /
#The output will be displayed in a dollar amount, not the number of pennies.

# Ask the user to enter the number of days


day_salary = .01
num_day = int(input('Number of Days to Double Salary: '))
for day in range (1,num_day+1):
    print(f'on day {day} your salary is:${day_salary:.2f}')
    day_salary *=2