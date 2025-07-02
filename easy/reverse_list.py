
nums = [1, 2, 3, 4, 5, 6, 7]


def reverse(nums: list[int], i: int, j: int) -> list[int]:
    
    if i >= j: return nums


    while i < j:
        nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j -= 1
    return nums


def reverse_list(nums: list[nums], k: int) -> list[nums]:
    
    i, j = 0, len(nums)-1

    nums = reverse(nums, i, j)
    nums = reverse(nums, i, k-1)
    nums = reverse(nums, k, j)

    return nums

print(nums)
print(reverse_list(nums, k=3))


# Bu masalada bizga ro'yxat beriladi va k int son beriladi k.lenght <= nums.lenght shundan k ta oxirgi elementini boshiga qo'yish kerak 
# Algoritimi birinchi keladigan yo'l bu oxiridan pop qilib boshiga insert qilish lekin bu juda sekin ishlaydi xamma elementni shift
# qilishga to'gri keladi ammo biz two pointer yordamida bu misolni hal qilsak boladi bitta funksya yozib olamiz ro'yxatni i-indexdan 
# j-indexgacha keyin ro'yxatni boshidan oxirigacha aylantiramiz va boshidan k ta aylantiramiz k-indexdan oxirigacha aylantiramiz masala 
# hal 
#








