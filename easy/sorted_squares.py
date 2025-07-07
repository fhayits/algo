
def sortedSquare(nums: list) -> list:
    n = len(nums)-1
    result = [0] * (n+1)
    i, j = 0, n
    pos = n

    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result[pos] = nums[j] ** 2
            j -= 1
        else:
            result[pos] = nums[i] ** 2
            i += 1

        pos -= 1
    
    return result
    




nums = [-4, -1, 0, 3, 10]
print(nums)
print(sortedSquare(nums))

