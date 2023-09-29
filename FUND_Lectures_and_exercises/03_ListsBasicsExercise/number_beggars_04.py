numbers_list = [int(x) for x in input().split(", ")]
beggars = int(input())

beggars_sum_final = [0] * beggars

for i in range(len(numbers_list)):
    num = numbers_list[i]
    beggar_idx = i % beggars
    beggars_sum_final[beggar_idx] += num

print(beggars_sum_final)

