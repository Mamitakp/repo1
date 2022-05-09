list1=[[1,2,3],[4,5,6],[7,8,9]]
final_list = []
row_1 = []
row_2 = []
row_3 = []
for i in range(len(list1)):
    row_1.append(list1[i][0])

for i in range(len(list1)):
    row_2.append(list1[i][1])

for i in range(len(list1)):
    row_3.append(list1[i][2])

final_list.append(row_1)
final_list.append(row_2)
final_list.append(row_3)

print(final_list)


