class linkedListNode:
    def __init__(self,value=0,nextNode=None):
        self.value=value
        self.nextNode = nextNode

class linkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self,value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                print('Node',node)
                print('currentNode.nextNode',currentNode.nextNode)
                break
            currentNode = currentNode.nextNode
            print("currentNode",currentNode)

    def PrintlinkedList(self):
        currentNode = self.head
        count = 0
        while currentNode is not None :
            print(currentNode.value , "->",end="")
            currentNode = currentNode.nextNode
            count = count+1
        print("None")
        print("count is",count)

    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.nextNode is not None):
                fast_ptr = fast_ptr.nextNode.nextNode
                slow_ptr = slow_ptr.nextNode
            print("The middle element is: ", slow_ptr.value)   

    def detectloop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while (fast_ptr  and fast_ptr.nextNode  and slow_ptr):
            fast_ptr = fast_ptr.nextNode.nextNode
            slow_ptr = slow_ptr.nextNode
            if(fast_ptr == slow_ptr):
                print("loop detected") 
                self.removeLoop(slow_ptr)
                return 1        
        return 0         

                
           
           

    # Function to remove loop
    # loop node-> Pointer to one of the loop nodes
    # head --> Pointer to the start node of the
    # linked list
    def removeLoop(self, loop_node):
        # Set a pointer to the beginning of the linked
        # list and move it one by one to find the first
        # node which is part of the linked list
        ptr1 = self.head
        while(1):
            # Now start a pointer from loop_node and check
            # if it ever reaches ptr2
            ptr2 = loop_node
            while(ptr2.nextNode != loop_node and ptr2.nextNode != ptr1):
                ptr2 = ptr2.nextNode

            # If ptr2 reached ptr1 then there is a loop.
            # So break the loop
            if ptr2.nextNode == ptr1:
                break

            ptr1 = ptr1.nextNode

        # After the end of loop ptr2 is the lsat node of
        # the loop. So make next of ptr2 as NULL
        ptr2.nextNode = None    

    ## reversing linked list
    def reverseLoop(self):
        prev = None
        currentNode = self.head 
        print('hi')
        while currentNode != None:
            nextNode = currentNode.nextNode
            currentNode.nextNode = prev
            prev = currentNode
            currentNode = nextNode
        self.head = prev    


    ## using recursion reversing linked list  
    def reverseLinkedlist(self):
        if self.head == None:
            return
        self.reverseUtil(self.head,None)

    def reverseUtil(self,currentNode,prev):
        if currentNode is None:
            self.head = prev
            return

        nextNode = currentNode.nextNode
        currentNode.nextNode = prev
        prev = currentNode
        currentNode = nextNode
        self.reverseUtil(currentNode,prev)

    ## print kth element from end

    def findKthElement(self,k):
        currentNode = self.head
        count = 0
        while currentNode is not None :
            currentNode = currentNode.nextNode
            count = count+1
        print("count is",count)
        if k > count :
            print("value is greater then length of linked list")
            return
        newK = count - k + 1
        print(newK)
        kthNode = self.head
        for i in range(newK-1):
            print('i',i)
            kthNode = kthNode.nextNode
        print("value",kthNode.value)    


ll = linkedList()
ll.PrintlinkedList()
ll.insert("3")
ll.PrintlinkedList()
ll.insert("44")
ll.PrintlinkedList()
ll.insert("55")
ll.PrintlinkedList()
ll.insert("57")
ll.PrintlinkedList()
#ll.findKthElement(1)
# ll.reverseLinkedlist()
# ll.PrintlinkedList()
ll.printMiddle()
# ll.detectloop()
# ll.head.nextNode.nextNode.nextNode.nextNode = ll.head.nextNode.nextNode
# ntt = ll.head.nextNode.nextNode.nextNode
# print('valuee',ntt.value)
# ll.detectloop()
# print("value afterr",ll.head.nextNode.nextNode.nextNode.nextNode)
# ll.detectloop()


                                   
