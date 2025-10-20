nums = []
num_input = input()
origin_nums = num_input.split()
for i in range(len(origin_nums)):
    nums.append(int(origin_nums[i]))
nums.sort()
print(nums[0])