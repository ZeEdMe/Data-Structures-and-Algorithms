def selctionsort(X):
    for i in range(len(X)):
        Min_Num = min(X[i:])
        current_index = i + X[i:].index(Min_Num)

        if current_index !=i:
            X[current_index],X[i] = X[i],X[current_index]
    return X

list1 = [6,40,98,152,654,23]

list2 = list1.sort()


print(list2)