def firstUniqChar(s):
    char_count = {}  # Hashmap to store character count
    
    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first non-repeating character and return its index
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1  # If no non-repeating character is found, return -1
# Example 1
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

# Example 2
s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

# Example 3
s = "aabb"
print(firstUniqChar(s))  # Output: -1
