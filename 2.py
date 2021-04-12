def sum_digits(value):
    val_re = 0
    while value != 0:
        val_re += value % 10
        value //= 10
    return val_re


cub_list = []
first_sum = 0
second_sum = 0

for i in range(1001):
    cub_list.append(i**3)

for j in cub_list:
    if (sum_digits(j)//7) == 0:
        first_sum += j

for j in cub_list:
    if (sum_digits(j+17)//7) == 0:
        second_sum += j

print(first_sum, second_sum)
