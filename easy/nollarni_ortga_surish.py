
nums = [1, 2, 0, 3, 0, 1, 3, 0, 7]

def moveZeroes(nums: list[int]) -> list[int]:
    count_zeroes = 0

    for i, num in enumerate(nums):
        if num == 0:
           count_zeroes += 1
        else:
            nums[i], nums[i - count_zeroes] = nums[i - count_zeroes], nums[i]

    return nums

print(nums)
print(moveZeroes(nums))

# time O(n)
# memory O(1)
# algoritm bu yerda nollarni ortga emas sonlarni chapga surish kerak nollar eslab qolinadi va agar son chiqsa nechta nol bo'lsa o'shancha
# chapga suriladi 



