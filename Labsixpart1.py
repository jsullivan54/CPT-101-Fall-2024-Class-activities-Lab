#Johnathan Sullivan AKA Bruce_Wayne_Jung (My developer name) Lab6part1
#This program is for Bulk Shipping charges


#This program takes a preferred method of shipping, the miles being shipped, and calculates the total cost of shipping/
#including the milage fee. It displays to the user what they will pay for a given item and method of delivery

#Enter the preferred method of shipping below
shipping_method= input('Enter the shipping method you are using (1-Day or 2-Day) ')
#Enter the Weight of the package in lbs
weight= int(input('Enter the weight in lbs '))
#Enter the amount of miles it is being shipped
miles= int(input('How many miles is it being shipped? '))

if shipping_method == '1-Day' and weight <5 or weight ==5:
    rate = 11.50
    milage_cost = miles *  .07
    total_cost= rate * milage_cost

elif shipping_method == '2-Day' and weight <5:
    rate = 7.75
    milage_cost= miles * .05
    total_cost= rate * milage_cost

elif shipping_method == '1-Day' and weight >5 and weight <=20:
    rate = 17.00
    milage_cost= miles * .07
    total_cost= rate * milage_cost

elif shipping_method == '2-Day' and weight >5 and weight <=20:
    rate = 10.5
    milage_cost= miles * .05
    total_cost= rate * milage_cost

elif shipping_method == '1-Day' and weight >20 and weight <=50:
    rate = 26.00
    milage_cost= miles * .07
    total_cost= rate * milage_cost

elif shipping_method == '2-Day' and weight >20 and weight <=50:
    rate = 20.50
    milage_cost= miles * .05
    total_cost= rate * milage_cost

elif shipping_method == '1-Day' and weight >50:
    rate = 31.50
    milage_cost= miles * .07
    total_cost= rate * milage_cost

elif shipping_method == '2-Day' and weight >50:
    rate = 24.00
    milage_cost= miles * .05
    total_cost= rate * milage_cost

print()
print(f'Your Package Weighing {weight:.2f} lbs, Shipping {shipping_method:} Will Cost:')
print(f'Base Rate: ${rate:.2f}')
print(f'Milage: {miles:.2f}')
print(f'Total Cost ${rate * milage_cost:.2f}')






