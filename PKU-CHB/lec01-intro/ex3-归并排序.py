# merge sort
import random

def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    middle = int(len(data_list) / 2)
    left = merge_sort(data_list[:middle])
    right = merge_sort(data_list[middle:])
    merged = []

    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)
    return merged

# 随机产生数据集
data_list = [random.randint(1, 100) for _ in range(50)]
print(merge_sort(data_list))

#厕都
print("\n厕都首发球员:")
data_list2 = [16,4,23,22,11,2,8,39,10,7,21]
print(merge_sort(data_list2))
