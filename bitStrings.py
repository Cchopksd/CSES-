number = int(input("Enter a number: "))

def Solution(data):
    arr = []
    binary = ""
    while data > 0:
        binary = str(data % 2) + binary
        data = data // 2
    return binary
    for x in range(number):
        print(x+1)
print(Solution(number))
