'''
5. 2D ARRAY / List = MatriX : Mảng 2 chiều
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print('5. Matrix')
for index1, row in enumerate(range(len(matrix))):
    for index2, col in enumerate(range(len(matrix))):
        print(f'[{index1}][{index2}]:',matrix[row][col])

#Transfrom Matrix in List:
ran = range(len(matrix))
list_converted = [matrix[row][col]
                  for row in ran for col in ran]
print('5. ',list_converted)

#Combine columns with zip and * : lấy từng cột thành nhiều list
print('5. ',[x for x in zip(*matrix)])