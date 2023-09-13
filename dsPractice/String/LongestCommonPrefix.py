class Solution:
    def longestCommonPrefix(self, strs ):
        ans = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans

s = Solution()
# strs = ["a"]
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))
["flower","flow","flight"]

#
# rs = ['fly', 'flow', "flew"]
# #
# print(rs[0][:3])
# for i in range (1, 2):
#     print(i)
# if 'fly' in rs:
#     print('yes')
# else:
#     print('no')
#
