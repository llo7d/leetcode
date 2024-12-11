class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""

        position = 1

        first_chars = []

        for i in range(len(strs)):
            first_chars.append(strs[i][position])

        print(first_chars)

        # shortest = min(strs, key=len)

        # for i in range(len(shortest)):
        #     for j in range(len(strs)):
        #         print(strs[j][i])


    
                

                
        print(prefix)
        return prefix

            
            
            
Solution().longestCommonPrefix(["flower","flow","flight"])
# Solution().longestCommonPrefix(["a"])
# Solution().longestCommonPrefix(["","b"])
# Solution().longestCommonPrefix(["ab", "a"]) # expected "a"
# Solution().longestCommonPrefix(["reflower","flow","flight"])


