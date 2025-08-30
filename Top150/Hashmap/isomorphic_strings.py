#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character
# while preserving the order of characters.
# No two characters may map to the same character,
# but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.


# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

from collections import defaultdict

def isIsomorphic( s, t):
    dic = defaultdict(str)
    rev_dic = defaultdict(str)

    for i in range(len(s)):
        if dic[s[i]] == "":
            dic[s[i]] = t[i]

        else:
            if dic[s[i]] != t[i]:
                return False

        if rev_dic[t[i]] == "":
            rev_dic[t[i]] = s[i]

        else:
            if rev_dic[t[i]] != s[i]:
                return False


    return True

t='foo'
s='bar'
print(isIsomorphic(s,t))

t='egg'
s='add'
print(isIsomorphic(s,t))

t='paper'
s='title'
print(isIsomorphic(s,t))

s ="badc"
t ="baba"
print(isIsomorphic(s,t))



#another solutuion

def isIsomorphic(s, t):
    # Create two arrays of size 256 (for ASCII characters)
    # -1 means "no mapping yet"
    map_s = [-1] * 256   # maps characters from s → t
    map_t = [-1] * 256   # maps characters from t → s

    # Loop through both strings by index
    for i in range(len(s)):
        # Convert characters to ASCII codes (so we can use them as array indices)
        cs, ct = ord(s[i]), ord(t[i])

        # Case 1: If both characters have not been mapped before
        if map_s[cs] == -1 and map_t[ct] == -1:
            # Create new mappings in both directions
            map_s[cs] = ct
            map_t[ct] = cs

        # Case 2: If there is an existing mapping but it does not match
        elif map_s[cs] != ct or map_t[ct] != cs:
            # Inconsistent mapping → not isomorphic
            return False

    # If loop finishes without inconsistencies, the strings are isomorphic
    return True
