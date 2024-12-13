class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""

        position = 0

        first_chars = []

        shortest = min(strs, key=len)

        
        for i in range(len(strs)):
            # Extra string counter for second character and so on
            for j in range(len(strs[i])):

                print(strs[i][j], strs[i+1][j])
                # If index is out of range, return prefix stop

                

        print(prefix)
        return prefix


    



            
            
Solution().longestCommonPrefix(["flower","flow","flight"])
# Solution().longestCommonPrefix(["a"])
# Solution().longestCommonPrefix(["","b"])
# Solution().longestCommonPrefix(["ab", "a"]) # expected "a"
# Solution().longestCommonPrefix(["reflower","flow","flight"])


