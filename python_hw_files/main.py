arr1 = ['Dragon', 'world', 2, 3, 4, 23, 25, 13, 'BMW', 12, 13, 'arra']

arr2 = []
arr3 = []

for i in arr1:
    if isinstance(i, str):
        arr2.append(i)
    else:
        arr3.append(i)

arr3.sort()

arr2 = sorted(arr2, key=len)

writefile = open('test1.txt', 'w')

for i in arr2:
    writefile.write(str(i) + ' ')

for i in arr3:
    writefile.write(str(i) + ' ')
