# T1 = ("Ahmad","Zeed","Abd")

T2 = (5.5,94,0)

# T3 = tuple([5 * x for x in range(0,5)])

# print(T3)

# # T3[0] = 1

# # print(T3)

# T4 = tuple("ZEED")

# print(T4)

# T5 = T1+T2+T3

# print(T5)

S1 = {"Ahmad","Zeed","Abd","Onion"}

print(S1)

S2 = set([2 * x for x in range(0,5)])

print(S2)

S3 = set([2 * x for x in range(0,10)])

print(S3)

# S3[0] = 1

# print(S3)

S4 = set("ZEED")

print(S4)

print(sum(S3))

print(S2.issubset(S3))

print(S2.union(S1))

print(S2.intersection(T2))