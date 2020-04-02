matrix = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
my_box = []
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        my_box.append(matrix[row][column])
        my_box = sorted(my_box)
i = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        matrix[row][column] = my_box[i]
        i += 1

print(matrix)