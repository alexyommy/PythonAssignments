# 1. Countdown
# def countdown(x):
#     empty_list = []
#     for x in range(x,-1,-1):
#         empty_list.append(x)
#     return empty_list
# a = countdown(5)
# print(a)

# 2. Print and Return
# def printAndReturn(list):
#     print (list[0])
#     return (list[1])
# print(printAndReturn([1,2]))

# 3. First Plus Length
# def first_plus_length(list):
#     return (list[0]+len(list))
# print(first_plus_length([1,2,3,4,5]))

#4. Values Greater than Second
# def values_greater_than_second(list):
#     newList=[]
#     greater_numbers=0
#     for x in range(0, len(list)):
#         if len(list)<2:
#             return False
#         elif list[x]>list[1]:
#             newList.append(list[x])
#             greater_numbers = greater_numbers + 1
#     print(greater_numbers)
#     return newList
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))

# 5. This Length, That Value
def length_and_value(a,b):
    newList=[]
    for x in range(0,a+1):
        newList.append(b)
    return newList
print(length_and_value(6,2))