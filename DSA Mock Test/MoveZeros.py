def moveZeroes(nums):
    # Initialize two pointers, one for the current element and one for the position of the last non-zero element
    curr = 0
    last_non_zero = 0
    
    # Iterate through the array
    while curr < len(nums):
        # If the current element is non-zero, swap it with the last non-zero element
        if nums[curr] != 0:
            nums[curr], nums[last_non_zero] = nums[last_non_zero], nums[curr]
            last_non_zero += 1
        curr += 1
# Example 1
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Example 2
nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]
