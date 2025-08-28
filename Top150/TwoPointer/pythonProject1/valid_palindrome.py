# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.


# Given a string s, return true if it is a palindrome, or false otherwise.

# Example
# 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a
# palindrome.


# Example
# 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a
# palindrome.


# Example
# 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.

# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
#
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
# =======================================================  sol ====================================



# first remove all non alphapatic charachter
# second convert to lower case
# then from two pointer one in start and another on end
# compare quality


def isPalindrome( s):
    result = ''.join([c for c in s if c.isalnum()])
    result = result.lower()

    if result == ""  :
        return True

    for i in range(len(result)):
        if result[i] != result[-1 - i]:
            return  False

    return True

print(isPalindrome("race a car"))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(" "))
