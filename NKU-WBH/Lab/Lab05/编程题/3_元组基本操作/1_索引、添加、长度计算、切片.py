my_tuple = (1, 2, 3, 4, 5)

# 索引操作
print(my_tuple[0])  # 输出1
print(my_tuple[-1])  # 输出5

print("\n===================================================\n")

# 添加元素（元组是不可变的，不能直接添加元素，但可以通过创建新元组实现）
new_tuple = my_tuple + (6,)  # 创建一个新元组并添加元素
print(new_tuple)  # 输出: (1, 2, 3, 4, 5, 6)

print("\n===================================================\n")

# 长度计算
print(len(my_tuple))  # 输出: 5

print("\n===================================================\n")

# 切片操作
print(my_tuple[1:4])  # 输出: (2, 3, 4)
print(my_tuple[:3])  # 输出: (1, 2, 3)
print(my_tuple[3:])  # 输出: (4, 5)