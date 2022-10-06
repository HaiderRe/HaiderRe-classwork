numbers = []
total = 0
for i in range(6):
    numbers.append(int(input("Enter Num:")))
    total = total + numbers[i]
#next _
for num in numbers[::-1]:
    print(num)
else: 
    print("Average is " + str(total/6))
    print("Total is " + str(total))