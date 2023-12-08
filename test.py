import math
l = ['10','5','33','8','0']
print(sorted([int(i) for i in l], reverse = True))
l_int = [int(i) for i in l]
print(sorted(range(len(l_int)), key = lambda i: l_int[i], reverse = True)[:3])

a = math.log10(1)
print(a)