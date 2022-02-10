'''
1.组合类
  题号：17，18
2.排列类

'''
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
