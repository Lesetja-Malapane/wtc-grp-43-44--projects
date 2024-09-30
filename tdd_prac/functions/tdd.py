"functions file"

def sum_of_even(nums):
    answer = 0
    for number in nums:

        if number%2 == 0:

            answer += number
    return answer

# print(sum_of_even([9,5]))

def calculate_mediam(nums):
    # pass
    if len(nums) == 0:
        return None
    elif len(nums)%2 != 0:
        position = (len(nums)/2) - 0.5 #index starts at 0 (reason for -0.5 not +0.5 )
        position = int(position)
        return nums[position]
    else:
        position1 = (len(nums)/2) #index starts with 0
        position2 = (len(nums)/2) -1#index starts with 0
        position1 = int(position1)
        position2 = int(position2)
        value = (nums[position1] + nums[position2])/2
        return value
    
def remove_duplicates(str):

    new_str = ""
    for char1 in str:
        if char1 not in new_str:
            new_str += char1
        else:
            continue
    return new_str

def find_missing_number(nums):

    if 1 not in nums:
        return 1
    
    for num in nums:
        if num != (nums.index(num) +1):
            num -= 1
            break
        else:
            continue
    return num


print(find_missing_number([6,5,3,7,2,1]))

def first_non_repeating_char(word):

    for char in word:
        if word.count(char) > 1:
            continue
        else:
            break

    return char

print(first_non_repeating_char("levelar"))