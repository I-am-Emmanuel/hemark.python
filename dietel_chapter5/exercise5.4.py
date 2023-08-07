arr = [[0, 0, 0],
       [0, 0, 0]]

lst = list(range(1, 7))

row, col = 2, 3
for r in range(row):
    for c in range(col):
        popped = lst.pop(0)
        #print(popped, end=' ')
        arr[r][c] = popped
print(arr)

#

