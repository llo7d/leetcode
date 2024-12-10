class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = ""

        # if len(strs) == 1:
        #     return strs[0]

        for i in range(len(strs)-1):
            # Return the string with the shortest length
            if len(strs[i]) < len(strs[i+1]):
                prefix = strs[i]
            else:
                prefix = strs[i+1]

            for j in range(len(prefix)):
                if prefix[j] == strs[i][j]:
                    prefix = prefix[j]
                else:
                    prefix = ""
                    return prefix



        print(prefix)

        
        # This loops trough all the strings in the list
        # for i in range(len(strs)): 
        #     prefix_list.append(strs[i][:2])
        #     # This loops trought individual strings
        #     # for j in range(len(strs)):
        #         # print(strs[i][:2])

        # print(prefix_list)

        # if len(prefix_list) == 1:
        #     return prefix_list[0]
        
        # for i in range(len(prefix_list)-1): # Subtract 1 to avoid index out of range
        #     if prefix_list[i] != prefix_list[i+1]:
        #         prefix = ""
        #         return prefix
            
        #     prefix = prefix_list[0]

        # print(prefix)
        # return prefix

            
            
            
# Solution().longestCommonPrefix(["flower","flow","flight"])
# Solution().longestCommonPrefix(["a"])
# Solution().longestCommonPrefix(["","b"])
Solution().longestCommonPrefix(["reflower","flow","flight"])


