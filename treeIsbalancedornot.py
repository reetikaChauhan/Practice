class Solution:
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
    def isBalanced(self,root) -> bool:
        if root is None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if(abs(lh-rh)<=1 and self.isBalanced(root.left) is True and self.isBalanced(root.right)) is True:
            return True
        return False   

            