number = int(input())

def Solution(data):
    arr = [data]
    while data != 1:
        if (data%2) ==0:
            data = data // 2
        else :
            data = (data*3)+1
        arr.append(data)
    return arr

result = Solution(number)

print(" ".join(map(str, result)))
