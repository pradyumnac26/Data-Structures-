class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None :
            return None 
        root.right,root.left=self.invertTree(root.left),self.invertTree(root.right)
        return root
        
        
