# A class to store a BST node
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform the preorder traversal on a BST
def preorder(root):
 
    if root is None:
        return
 
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
 
# Recursive function to push nodes of a given binary search tree into a
# list in an inorder fashion
def pushTreeNodes(root, nodes):
 
    # base case
    if root is None:
        return
 
    pushTreeNodes(root.left, nodes)
    nodes.append(root)
    pushTreeNodes(root.right, nodes)
 
 
# Recursive function to construct a height-balanced BST from
# given nodes in sorted order
def buildBalancedBST(nodes, start, end):
 
    # base case
    if start > end:
        return None
 
    # find the middle index
    mid = (start + end) // 2
 
    # The root node will be a node present at the mid-index
    root = nodes[mid]
 
    # recursively construct left and right subtree
    root.left = buildBalancedBST(nodes, start, mid - 1)
    root.right = buildBalancedBST(nodes, mid + 1, end)
 
    # return root node
    return root
 
 
# Function to construct a height-balanced BST from an unbalanced BST
def constructBalancedBST(root):
 
    # Push nodes of a given binary search tree into a list in sorted order
    nodes = []
    pushTreeNodes(root, nodes)
    print(nodes)
 
    # Construct a height-balanced BST from sorted BST nodes
    return buildBalancedBST(nodes, 0, len(nodes) - 1)
def height(root):
 
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
 
# function to check if tree is height-balanced or not
 
 
def isBalanced(root):
 
    # Base condition
    if root is None:
        return True
 
    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)
 
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
            root.left) is True and isBalanced(root.right) is True:
        return True
 
    # if we reach here means tree is not
    # height-balanced tree
    return False
 
if __name__ == '__main__':
 
    root = Node(20)
    root.left = Node(15)
    root.left.left = Node(10)
    root.left.left.left = Node(5)
    root.left.left.left.left = Node(2)
    root.left.left.left.right = Node(8)
 
    root = constructBalancedBST(root)
 
    print('Preorder traversal of the constructed BST is ', end='')
    preorder(root)
 