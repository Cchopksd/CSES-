count = int(input())


loop = 0
result = {}
while loop < count:
    loop += 1
    lst = [int(x) for x in input().split()]
    for x in lst:
        print(x)
        result.append(x)

print(result)
# def Solution(data_list):
#     print(data_list)
#     for x in (data_list):
#         print(x)
#         return x


# print(Solution(array))
