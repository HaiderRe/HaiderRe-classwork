list1 =[34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
count = 0
list2 = []
for index in range(0, len(list1) -1):
 if(list1[index] >= 80 and list1[index] <=100):
    count = count + 1
print("number of integers in range 80-100" , count)
for i in range(0,len(list1) - 1): 
    if(not(list1[index] >= 80 and (list1[index] <=100))):
        list2.append(list1[index])
print(list2)           