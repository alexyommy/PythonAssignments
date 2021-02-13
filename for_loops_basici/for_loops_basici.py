# 1. Basics
# for x in range(151):
#     print(x)

# 2. Multiples of 5
# for x in range(5, 1000):
#     if x % 5 ==  0:
#         print(x)

# 3. Counting, the Dojo Way
# for x in range(101):
#     if x % 10 ==0:
#         print("Coding Dojo")
#     elif x % 5 == 0:
#         print("Coding")
#     else:
#         print(x) 

# 4. Whoa. That Sucker's Huge
# sum = 0
# for x in range(1,500000,2):
#     sum += x
# print(x)

# 5. Countdown by Fours
# for x in range(2018,0,-4):
#     print(x)

# 6. Flexible Counter
def flexible_counter(lowNum, highNum, mult):
    for x in range(lowNum, highNum+1):
        if x % mult == 0:
            print(x)

flexible_counter(5,75,3)


