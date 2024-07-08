# Remove Outermost Parentheses
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#Input: s = "(()())(())"
#Output: "()()()"

#Input: s = "(()())(())(()(()))"
#Output: "()()()()(())"

#Input: s = "()()"
#Output: ""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ss = ''
        for i in s:
            if i == '(':
                if len(stack) > 0:
                    ss+=i
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    ss+=i
            
        return ss

#s = Solution()
#print(s.removeOuterParentheses('()()()'))


# Reverse Words in a String
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

#Input: s = "the sky is blue"
#Output: "blue is sky the"

#Input: s = "  hello world  "
#Output: "world hello"

#Input: s = "a good   example"
#Output: "example good a"

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words using whitespace as delimiter
        words = s.split()
        
        # Reverse the order of words
        words.reverse()
        
        # Join the reversed words with a single space as separator
        return ' '.join(words)
    

# Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

#Input: nums = [1,1,1], k = 2
#Output: 2

#Input: nums = [1,2,3], k = 3
#Output: 2

def subarraySum(self, nums, k):
    count = 0
    sum_dict = {0: 1}
    total_sum = 0
    for num in nums:
        total_sum += num
        if total_sum - k in sum_dict:
            count += sum_dict[total_sum - k]
        if total_sum in sum_dict:
            sum_dict[total_sum] += 1
        else:
            sum_dict[total_sum] = 1
    return count

#  Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3 -> The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1 -> The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3 -> The answer is "wke", with the length of 3

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a ={}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        
        return type(class_name, bases, a)

class Dog(metaclass = Meta):
    x = 8
    y = 5

    def hello(self):
        print('hi')

d = Dog()
d.X