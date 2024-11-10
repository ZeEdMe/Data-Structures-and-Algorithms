# arr1 = [2,5,3,32,62,100]
# i = 0

# while i <= len(arr1):
#     print(arr1[i])
#     i += 1

# import math

# arr2 = [Num for Num in range(0,pow(10,6)+1)]

# arr3 = [0.5 * Num for Num in arr2]

# arr4 = [Num for Num in arr3 if Num < 100.5]

# print(arr4)

# arr5 = ["blue","green","red"]
# arr6 = ["green","blue","red"]

# print(arr5 == arr6)

# print(arr5 != arr6)

# print(arr5 < arr6)

# print(arr6 < arr5)

# text = "Hello World".split()
# print(text)
# text2 = "30100501009210045".split("100")
# print(text2)

# def reverse(list):
#     result = []
    
#     for element in list:
#          result.insert(0,element)
    
#     return result

# list1 = [1,2,3,4,5,6]
# list2 = reverse(list1)

# print(list2)
# print(list1)

def search(list,key):
    for x in range(0,len(list)):
        if key == list[x]:
            return x

list1 = [1,2,3,4,5,6,7,8,9]
key = int(input("Enter A Number: "))

print(search(list1,key))