#test for branch user

a = 6
b = 5


print("{} & {} = {}".format(a, b, (a&b)))
print("{} ^ {} = {}".format(a, b, (a^b)))
print("{} | {} = {}".format(a, b, (a|b)))
# & : bit끼리 연산 and연산 -둘중에 하나라도 0이면 0
# & : bit 끼리 exvlusive or 연산 -둘이 같으면 0 다르면 1 
# | : bit 끼리 or연산 -둘중 하나라도 1이면 1 
