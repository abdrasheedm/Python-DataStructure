import copy

arra = [[1,2,3], [4,5,6], [6,7,8]]

new_arra = copy.deepcopy(arra)

print(arra, id(arra[0]))
print(new_arra, id(new_arra[0]))
