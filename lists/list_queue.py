
def enqueue(list1, item):
    if( len(list1) == MaxSize + 1):
        print("MaxSize Of Queue Reached")
    else:
     list1.append(item)  
def dequeue(list1):
    if(len(list1) == 0):
        print("No elements in queue")
    else:
     global Start
     list1.pop(Start)
     Start = Start + 1

MaxSize = int(input("Enter The Maxsize of the queue"))
Start = 0 
End = 0
list1 = []
print(len(list1))
enqueue(list1, "shirts")
enqueue(list1, "socks")
dequeue(list1)
enqueue(list1, "shirtsss")
dequeue(list1)
print(list1)
