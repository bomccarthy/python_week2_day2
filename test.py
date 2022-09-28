l_1 = [1,11,14,5,8,9]
l_mine = []

for l in l_1:
    if l < 10:
        l_mine.append(l)
print(l_mine)

l_mine = [l for l in l_1 if l < 10]
print(l_mine)



l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

print(sorted(l_1 + l_2))

my_l = l_1 + l_2
my_l.sort()
print(my_l)