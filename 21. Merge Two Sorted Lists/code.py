# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        # Check the inverse, if its smaller, move it to the end instead of checking if its bigger
        # 
        

        # first combine the list.
        combined_list = list1 + list2

        print(combined_list)

        # sorted list
        sorted_list = [0]

        for i in combined_list:
            print(i)


            if i <= sorted_list[-1]:
                sorted_list.append(i)

            else:
                sorted_list.append



        sorted_list.pop(0)
        
        print("Sorted List: " , sorted_list)

        # If the i is bigger than the last in new_list, add it, else add it to other list?


sol = Solution()
sol.mergeTwoLists([1,2,4],[1,3,4])