'''
DFS
· n个点h为logn if it is highly balanced tree
· 时间&空间复杂度 O(V+E)V为顶点个数，E为边数
· 当发现有多重循环的时候，用递归实现层数不定的for循环

DFS可以解决的问题类型
1.组合类
  题号：17，18，425，135
2.排列类
  题号：10
3.二叉树

combination和permutation template difference:
  combination dfs 参数有一个index 意思是combination can contain 1,2..k 元素 而permutation里的元素数量是固定的

问题：
1.特殊情况处理时 not，is None，len == 0的区别与用法场景
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


#lintcode 425
KEYBOARD={
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz',
    }


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations

    #1.递归的定义
    ''' digits代表输入的数字
        index当前dfs要处理的数字 处理到了第几个数字 
        combination 目前为止得到的组合
        combinations 目前为止找到的所有完整组合的合集
    '''    
    def dfs(self, digits, index, combination, combinations):
    #递归的出口
        if len(digits) == len(combination): #也可以是len(digits) == index
            combinations.append(''.join(combination))
            return
    #递归的拆解 
        for letter in KEYBOARD[digits[index]]:
            combination.append(letter)
            print (combination)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()
           
          
#lintocode 90 k sum k（k固定）个元素的组合和为target k个数字的排序无所谓
def kSumII(self, A, k, target):
        A.sort()
        # 这里不排序也可以
        #需要排序的情况：1.有重复，排序可以让重复元素相邻好做操作 2.最后的combinations里的小list有排序要求
        combinations = []
        self.dfs(A, 0, k, target, [], combinations)
        return combinations
    def dfs(self, A, index, k, target, combination, combinations):
        #递归的出口
        if k == 0 and target == 0:
            combinations.append(list(combination))
            return 
        if k == 0 or target <= 0:
            return
        for i in range(index, len(A)):
            combination.append(A[i])
            self.dfs(A, i + 1, k - 1, target - A[i], combination, combinations)
            combination.pop()
            
#135 combination sum k（k不固定）个元素的组合和为target k个数字非降序
def combinationSum(self, candidates, remain_target):
        results = []
        if not candidates:
            return results
        #去重+排序
        sorted_candidates = sorted(list(set(candidates)))
        self.dfs(sorted_candidates, 0, remain_target, [], results)
        return results
    
    def dfs(self, nums, index, remain_target, combination, results):
        if remain_target == 0:
            results.append(list(combination))  
            return 
        for i in range(index, len(nums)):
            #减枝 当前这个数加进去都超过了 后面就更不用看了
            if remain_target < nums[i]:
                return 
            combination.append(nums[i])
            self.dfs(nums, i, remain_target - nums[i], combination, results)
            combination.pop()
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

            
#lintcode 10
'''去重逻辑：如果前面的b还没有选掉，就不能选择后面的b。否则，会造成重复'''





