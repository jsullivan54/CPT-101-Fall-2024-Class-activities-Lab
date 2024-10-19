#program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents./
#The formula for converting a temperature from Celsius to Fahrenheit is



#where F is the Fahrenheit temperature, and C is the Celsius temperature./
#Your program must use a loop to display the table.


for ctemp in range (0,21):
    fahr = (9/5)*ctemp + 32
    print(f'Celsius: {ctemp}\t\tFahrenheit: {fahr:.1f}')

