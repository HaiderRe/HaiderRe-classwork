rows,cols=(50,4)
arr=[[0 for i in range(cols)]for j in range(rows)]
total = [0,0,0,0]
for quarter in range(cols): 
    total[quarter] = 0
    for p in range(rows):
        total[quarter] = total[quarter] + arr[p][quarter]
    else:
        print(total[quarter])    