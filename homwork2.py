
# Homework Wednesday


# Excercise 1

# lista = [1,2,3,4]
# listb = [5,6,7,8]
# c = [a * b for a, b in zip(lista, listb)]

# print(c)


# Excercise 2

a = [[1,3],[2,4]]
b = [[5,2], [1,0]]
c = []

for index1 in range(len(a)):
    small_list = []
    for number in range(len(a[index1])):
        new_number = a[index1][number] + b[index1][number]
        small_list.append(new_number)
    c.append(small_list)
print(c)
