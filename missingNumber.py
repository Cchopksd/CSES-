number = int(input())
number_list = [int(x) for x in input().split()]


def Solution(data, data_list):
    missing_number = []
    for i in range(data):
        i += 1
        if i not in data_list:
            missing_number.append(i)
    return missing_number


for x in Solution(number, number_list):
    print(x)
