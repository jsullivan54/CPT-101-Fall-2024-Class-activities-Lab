#Johnathan Sullivan

#At one college, the tuition for a full-time student is $8,000 per semester. /
#It has been announced that the tuition will increase by 3 percent each year for the next 5 years. /
#This program will contain a loop that displays the projected semester tuition amount for the next 5 years./

tuition_ammount = 8000
for year in range (1,6):
    print(f'Tuition for year {year} is : $ {tuition_ammount:.2f}')
    tuition_ammount *= 1.03
