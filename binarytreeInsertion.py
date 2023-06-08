class BST:
    def __init__(self,key):
        self.key=key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data :
            if self.lchild:
                self.lchild.insert(data)
            else :
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node not found")

    # preorder traversal root- left-right
    def preorderTraversal(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorderTraversal()
        if self.rchild:
            self.rchild.preorderTraversal()   
    # left - root - right               
    def inorderTraversal(self):
        if self.lchild:
            self.lchild.inorderTraversal()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorderTraversal()  

    

    # post-order left-right-root
    def postTraversal(self):
        if self.lchild:
            self.lchild.postTraversal()
        if self.rchild:
            self.rchild.postTraversal() 
        print(self.key,end=" ")

       

    def deletion(self,data):
        if self.key is None:
            print("tree is empty")
            return
        
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print("given Node is not present in the tree")

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree

        elif data >  self.key:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print("given node is not present in the tree")

    # If key is same as root's key, then this is the node
    # to be deleted
                
        else:
            # Node with only one child or no child
            if self.lchild is None:
                temp = self.lchild
                self = None
                return temp

            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
            node = self.rchild
           #i am finding smallest element of given subtree i.e node and replacing it with root node
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deletion(node.key)
        return self

    def getheight(self):
        if self.lchild and self.rchild:
            return 1+ max(self.lchild.getheight(),self.rchild.getheight())
        elif self.lchild:
            return 1+ self.lchild.getheight()
        elif self.rchild:
            return 1+ self.rchild.getheight()
        else:
            return 1
    
    def getHeight(self):
        if self.key:
            return self.getheight()
        else:
            return 0
    

    


            

            


root = BST(50)
list1 = [17,76,9,23,54,14,19,72,12,67]
#root = BST(5)
#list1 = [3,8,1,4,9,2]
for i in list1:
    root.insert(i)
root.search(300)
print("preorder")
root.preorderTraversal()
print()
print('Inorder')
root.inorderTraversal()
print()
print('postorder')
root.postTraversal()
print()
print("after deletion 10")
root.deletion(10)
root.preorderTraversal()
print()
print("height is ",root.getHeight())



