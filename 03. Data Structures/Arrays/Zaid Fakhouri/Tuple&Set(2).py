# S1 = ("Ahmad","Zeed","Abd")

# S2 = (5.5,94,0)

# S3 = tuple([5 * x for x in range(0,5)])

# print(S3)

# # S3[0] = 1

# # print(S3)

# S4 = tuple("ZEED")

# print(S4)

# S5 = S1+S2+S3

# print(S5)

S1 = {"Ahmad","Zeed","Abd"}

print(S1)

S2 = set([2 * x for x in range(0,5)])

print(S2)

S3 = set([5 * x for x in range(0,10)])

print(S3)

# S3[0] = 1

# print(S3)

S4 = set("ZEED")

print(S4)

S5 = S3 or S2 or S1

print(S5)

print(sum(S3))