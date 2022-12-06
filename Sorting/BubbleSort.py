a = [7,4,6,8,1,5]

           
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    #a,b = b, a
def bubble1(a, a_times):
    p = False
    if(a_times == len(a)):
        return 1
    for i in range(0, len(a) - a_times):
        if(a[i + 1] < a[i]):
            p = True
            swap(a,i, i + 1)
    #times = times - 1
    a_times = a_times + 1
    if(p):
     bubble1(a, a_times)
    else:
        return 0
a_times = 1
bubble1(a, a_times)
print(a)
