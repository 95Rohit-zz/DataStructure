def next_greatest_element(arr):
    li = []
    j = 0
    for i in arr:
        if len(li) == 0:
            li.append([i,j])
        elif i < li[len(li)-1][0]:
            li.append([i,j])
        else:
            arr[li[len]-1[1]] = i
            li.pop()
            li.append([i,j])
        j = j+1
    while li:
        arr[li[len]-1[1]] = -1
        li.pop()
    return arr
