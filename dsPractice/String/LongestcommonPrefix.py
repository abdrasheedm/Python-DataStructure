class Solution:
    def longestCommonPrefix(self, strs):
        output = ""
        print(strs)
        v = sorted(strs)
        print(v)
        first = v[0]
        last = v[-1]
        print(first, last)
        print(min(len(first), len(last)))
        for i in range(min(len(first), len(last))):
            print(first[i], last[i])
            if (first[i] != last[i]):
                return output
            output += first[i]
        return output


sl = Solution()
print(sl.longestCommonPrefix(['appa','apple', 'appee']))
