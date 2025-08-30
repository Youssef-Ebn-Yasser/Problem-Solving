#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
from collections import defaultdict

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".


# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false


# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

#================================ Sol ==================================





def get_word(w,s):
    s_word = ""
    for i in range(s,len(w)):
        if w[i] == " ":
            return s_word , i+1
        s_word += w[i]
    return  s_word , -1




def wordPattern(pattern, s):
    p_dic = defaultdict(str)
    s_dic = defaultdict(str)
    start_pos = 0

    for i in range(len(pattern)):
        w , start_pos =get_word(s,start_pos)

        # for case not the same lenght
        if (i == len(pattern) - 1 and start_pos != -1) or (i != len(pattern) - 1 and start_pos == -1):
            return False

        if p_dic[pattern[i]] == "":
            p_dic[pattern[i]] = w

        else :
            if p_dic[pattern[i]] !=  w:
                return  False

        if s_dic[w] == "" :
            s_dic[w] = pattern[i]

        else :
            if s_dic[w] !=pattern[i] :
                return False
    return True


# w , start_pos =get_word(s,0)
#
#
# print(w)
# print(start_pos)

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))


pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))


#another better one
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    p_to_w = {}
    w_to_p = {}

    for p, w in zip(pattern, words):
        # If pattern already mapped, must match word
        if p in p_to_w and p_to_w[p] != w:
            return False
        # If word already mapped, must match pattern
        if w in w_to_p and w_to_p[w] != p:
            return False
        # Create new mapping if not exists
        p_to_w[p] = w
        w_to_p[w] = p

    return True

