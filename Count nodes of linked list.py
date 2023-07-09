#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        temp = head_node.next
        cnt = 1
        while temp:
            cnt += 1
            temp = temp.next
        return cnt