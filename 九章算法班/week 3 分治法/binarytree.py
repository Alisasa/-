



#lintcode 902 Kth Smallest Element in a BST
#方法1：recursion
def kthSmallest(self, root, k):
        # write your code here 中根遍历排序 找到第k个数
        res = []
        self.helper(root,res)
        return res[k-1]

    def helper(self,root,res):
        if not root:
            return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)
        
#方法2 iteration    
def kthSmallest(self, root, k):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        for i in range(k-1):
            node = stack.pop()
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return stack[-1].val

#lintcode 902 Closest Binary Search Tree Value
def closestValue(self, root, target):
        # write your code here
        if root is None:
            return None
        lower = self.lower_bound(root, target)
        upper = self.upper_bound(root, target)

        if lower is None:
            return upper.val
        if upper is None:
            return lower.val
        print(lower.val)
        print(upper.val)
        if (target - lower.val) <= (upper.val - target):
            return lower.val
        return upper.val
        

    #找到小于等于target的最大值
    def lower_bound(self, root, target):
        if root is None:
            return None
        if target < root.val:
            return self.lower_bound(root.left, target)
        #target >= root.val 已经是一个lower bound，记录下来并继续在左子树上寻找是否有更接近target的lower bound
        lower = self.lower_bound(root.right, target)
        return root if lower is None else lower

    #找到大于等于target的最小值
    def upper_bound(self, root, target ):
        if root is None:
            return None
        if root.val <= target:
            return self.upper_bound(root.right, target)
        # root.val > target 已经是一个upper bound，记录下来并继续在左子树上寻找是否有更接近target的upper bound
        upper = self.upper_bound(root.left, target)
        return root if upper is None else upper
    
