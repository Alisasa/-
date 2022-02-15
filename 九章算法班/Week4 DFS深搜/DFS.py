'''
DFS
· n个点h为logn if it is highly balanced tree
· 时间&空间复杂度 O(V+E)V为顶点个数，E为边数
· 当发现有多重循环的时候，用递归实现层数不定的for循环

DFS可以解决的问题类型
1.组合类
  题号：17，18
2.排列类
3.二叉树

'''
'''1.组合类'''
#lintcode 17. subset 没有重复数字
#方法一：
 def subsets(self, nums):
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, 0, [], results)
        return results
    #1.递归的定义
    def dfs(self, nums, k, subset, results):
        results.append(subset[:])
    #2.递归的出口 for i in rang(index, len(nums)) => for i in [index, size_of_nums - 1], 当index = size_of_nums时候就是退出，这就是出口条件。
    #3.递归的拆解
        for i in range(k, len(nums)):
            subset.append(nums[i])
            print(subset)
            self.dfs(nums, i + 1, subset, results)
            del subset[-1]
 #方法二：
           
#lintcode 18. subset 有重复数字


'''2.排列类
递归： 本质是n重循环
时间复杂度 O（N！*N）
'''
#lintcode 15#
def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        permutations = []
        self.dfs(nums, [], set(), permutations)
        return permutations
    # 1. 递归的定义：找到所有permutation开头的permutations
    def dfs(self,nums, permutation, visited, permutations):
        # 2. 递归的出口
        if len(nums) == len(permutation):
          #必须要深度copy
            permutations.append(list(permutation))
            return
        #3.递归的拆解
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, permutation, visited, permutations)
            visited.remove(num)
            permutation.pop()

            
