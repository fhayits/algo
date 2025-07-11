
nums = [1,8,6,2,5,4,8,3,7]


def maxArea(nums: list) -> int:
    max_area = 0
    i, j = 0, len(nums)-1

    while i < j:
        curr_area = min(nums[i], nums[j]) * (j-i)
        max_area = max(max_area, curr_area)

        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
    return max_area




if __name__ == "__main__":
    print(maxArea(nums))



