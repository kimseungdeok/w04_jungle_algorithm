import sys
input = sys.stdin.readline
# 문자열로 받아서 리스트에 담는다.
# - 를 기준으로 split 해서 다시 리스트에 담고
# 리스트의 첫번째원소에 + 문자열이 있다면 그 첫번째원소만 + 으로 split하면서 정수로바꿔 계산후 다시 재할당
# for문 사용해서 result = 첫번쨰원소 + 나머지 원소

t = input().lstrip('0').rstrip()

nums = t.split('-')

nums[0] = nums[0].split('+')
value = list(map(int, nums[0]))
new_first_index = sum(value)
nums[0] = new_first_index

result = nums[0]

for i in range(1, len(nums)):
    seper = nums[i].split('+')
    seper = list(map(int, seper))
    sum_seper = sum(seper)
    nums[i] = sum_seper
    result = result - nums[i]

print(result)
