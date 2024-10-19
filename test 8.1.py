student = 1
while student <= 3:
    total = 0
    for score in range (1, 4):
        score = int(input("Enter test score: "))
        total += score
    average = total/3
    print("student",student, "average: ", average)
    student += 1