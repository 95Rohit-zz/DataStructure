# Given an array of strings, group anagrams together.


# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            temp = []
            for char in word:
                temp.append(str(ord(char)))
            temp = ''.join(sorted(temp))
            if temp in d:
                d[temp].append(word)
            else:
                d[temp] = [word]
        output = []
        for group in d:
            output.append(d[group])
        return output
