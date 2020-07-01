class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, result = 0, 0
        count = {'a':0, 'b':0, 'c':0}
        for c in s:
            count[c] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            result += i
        return result


a = Solution()
s = "abcabc"
print(a.numberOfSubstrings(s))