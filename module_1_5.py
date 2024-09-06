immutable_var = 1, 'the', True, 12.3
immutable_var_1 = (1, 'the', True, 12.3)
immutable_var_2 = tuple([1, 'the', True, 12.3])
print(immutable_var)
print(immutable_var_2)
print(immutable_var_1)
immutable_var_1 = (1, 'the', True, 12.3) + (2,55)
print(immutable_var_1)
immutable_var_1 = (1, 'the', True, 12.3) * 2
print(immutable_var_1)
immutable_var_3 = (1, 'the', True, 12.3, [14, True])
print(immutable_var_3)
immutable_var_3[-1][1] = False
print(immutable_var_3)
mutable_list = [1,'str',16.1,False]
print(mutable_list)
mutable_list[1] = 'Great'
mutable_list[2] = 56.2
print(mutable_list)
