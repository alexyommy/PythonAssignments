# 1. Biggie Size
def biggie_size(list):
    for x in range(0, len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list
# print(biggie_size([-1,3,5,-5]))

# 2. Count Positives
def count_positives(list):
    positives = 0
    for x in range(0, len(list)):
        if list[x] > 0:
            positives += 1
    list[len(list)-1] = positives
    return list
# print(count_positives([-1,1,1,1]))
# print(count_positives([1,6,-4,-2,-7,-2]))

# 3. Sum Total
def sum_total(list):
    sum = 0
    for x in range(0, len(list)):
        sum += list[x]
    return sum
# print(sum_total([1,2,3,4]))
# print(sum_total([6,3-2]))

# 4. Average
def average(list):
    sum = 0
    for x in range(0, len(list)):
        sum += list[x]
    return sum/len(list)
# print(average([1,2,3,4]))

# 5. Length
def length(list):
    listLength = 0
    listLength = len(list)
    return listLength
# print(length([37,2,1,-9]))
# print(length([]))

# 6. Minimum
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for x in range(0, len(list)):
            if list[x] < min:
                min = list[x]
        return min
# print(minimum([37,2,1,-9]))
# print(minimum([]))

# 7. Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for x in range(0, len(list)):
            if list[x] > max:
                max = list[x]
        return max
# print(maximum([37,2,1,-9]))
# print(maximum([]))

# 8. Ultimate Analysis
def ultimate_analysis(list):
    result = {
        'sum_total':None,
        'average':None,
        'minimum':None,
        'maximum':None,
        'length':0
    }
    if len(list) == 0:
        return result
    else:
        result['sum_total']=0
        result['maximum']=list[0]
        result['minimum']=list[0]
    for x in list:
        if x > result['maximum']:
            result['maximum'] = x
        elif x < result['minimum']:
            result['minimum'] = x
        result['sum_total'] += x
        result['length'] += 1
    result['average'] = result['sum_total'] / len(list)
    return result
# print(ultimate_analysis([37,2,1,-9]))
# print(ultimate_analysis([]))

# 9. Reverse List
def reverse_list(list):
    half_len = int(len(list)/2)
    for x in range(half_len):
        list[x], list[len(list) - 1 - x] = list[len(list) - 1 - x], list[x]
    return list
# print(reverse_list([37,2,1,-9]))
# print(reverse_list([37,2,1,-9,4,9]))





