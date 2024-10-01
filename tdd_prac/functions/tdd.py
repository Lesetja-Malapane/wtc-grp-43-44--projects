
def sum_of_even(nums):
    answer = 0
    for number in nums:

        if number%2 == 0:
            answer += number

    return answer

# print(sum_of_even([9,5]))

def calculate_mediam(nums):
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
# print(calculate_mediam([1,2,3,4,5,6]))    

def find_missing_number(nums):

    nums.sort()
    
    for x in nums:
        if x == (nums.index(x) +1):
            continue
        else:
            x -= 1
            return x
            
# print(find_missing_number([3]))

def remove_duplicates(str):

    new_str = ""
    for char1 in str:
        if char1 not in new_str:
            new_str += char1
        else:
            continue
    return new_str
# print(remove_duplicates("programming"))

def first_non_repeating_char(str):

    for char in str:
        if str.count(char) > 1:
            continue
        else:
            return char

# print(first_non_repeating_char("pineapple"))