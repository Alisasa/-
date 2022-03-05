'''
数据结构三种考法：
1.问某种数据结构的基本原理并要求实现（北美考的少）
2.使用某一个数据结构实现需求
3.多个数据结构配合在一起使用，实现需求（我们主要学这个）

知识回顾
set:
set 无重复，且无序 应用：去重，快速查找
set(iterable) 装入可迭代的对象，例如list/tuple/string
set0 = set() set1={1,2,3} set3=set([1,2,3])注意这里加了中括号因为里面的对象需要iterable一串数据
set2 = set('hello') output: {'o', 'h', 'e', 'l'} --> 装入的是具体的每个字母
set4 = set((1,True,'hello')) output:{1, 'hello'}  --> 1和true是一样的
set.add()
set.remove() 如果4不存在于set中，报错
set.discard() 如果4不存在于set中，不报错，set不变
1 in set
len(set
for val in set:

dict:
dict0 = {} dict = dict() dict1 ={'name' :'amy', 'age':'21'} 
特点 key:value 无重复key，value可重复复，无序，通过key找到value
添加元素 dict[1] = 'jan' dict['age']=21
删元素 dict.pop(1) dict.pop('age') 删除key 然后value就一起删除了
取元素dict.get(1) dict.get('age')
查找key O(1) 1 in dict 查找value O(n) 21 in dict.value()
大小O（1） len(dict)
遍历 for key in dict: for value in dict.values(): for key, value in dict.items()

Heap堆
最小堆（最小元素在堆顶）和最大堆（最大元素在堆顶），堆是一个完全二叉树
python:heapq
堆的底层实现结构一般是数组

基本操作：
构建堆 (heapify) O(N)
遍历堆 O(NlogN)
add O(logN)
pop O(logN)只能移除栈顶元素
remove 理论上可以实现O(logN)需要写程序去实现 heapq O(logN)
min or max O(1)

给定一个数组A[]
堆顶为 A[i]
左孩子为 A[i * 2 + 1]
有孩子 A[i * 2 + 2]

堆是一种数据结构，它通常有三种方法：push， pop 和 top。其中，“push”添加新的元素进入堆，“pop”删除堆中最小/最大元素，“top”返回堆中最小/最大元素。
把一个无序整数数组变成一个堆数组。如果是最小堆，每个元素A[i]，我们将得到A[i * 2 + 1] >= A[i]和A[i * 2 + 2] >= A[i]

1. sift up 对于每个元素A[i]，比较A[i]和它的父亲结点的大小，如果小于父亲结点，则与父亲结点交换。交换后再和新的父亲比较，重复上述操作，直至该点的值大于父亲。
时间复杂度分析：对于每个元素都要遍历一遍，这部分是 O(n)，每处理一个元素时，最多需要向根部方向交换 logn次。因此总的时间复杂度是 O(nlogn)
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father
            
    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
2.sift down
算法思路：
初始选择最接近叶子的一个父结点，与其两个儿子中较小的一个比较，若大于儿子，则与儿子交换。
交换后再与新的儿子比较并交换，直至没有儿子。
再选择较浅深度的父亲结点，重复上述步骤。
时间复杂度分析
这个版本的算法，乍一看也是 O(nlogn)， 但是我们仔细分析一下，算法从第 n/2 个数开始，倒过来进行 siftdown。也就是说，相当于从 heap 的倒数第二层开始进行 siftdown 操作，倒数第二层的节点大约有 n/4 个， 这 n/4 个数，最多 siftdown 1次就到底了，所以这一层的时间复杂度耗费是 O(n/4)，然后倒数第三层差不多 n/8 个点，最多 siftdown 2次就到底了。所以这里的耗费是 O(n/8 * 2), 倒数第4层是 O(n/16 * 3)，倒数第5层是 O(n/32 * 4) ... 因此累加所有的时间复杂度耗费为：
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...
然后我们用 2T - T 得到：
2 * T(n) = O(n/2) + O(n/4 * 2) + O(n/8 * 3) + O(n/16 * 4) ...
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...
2 * T(n) - T(n) = O(n/2) +O (n/4) + O(n/8) + ...
= O(n/2 + n/4 + n/8 + ... )
= O(n)
因此得到 T(n) = 2 * T(n) - T(n) = O(n)


import sys
import collections
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftdown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1    #A[i]左儿子的下标
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2    #选择两个儿子中较小的一个
            if A[son] >= A[k]:
                break
                
            temp = A[son]
            A[son] = A[k]
            A[k] = temp
            k = son
    
    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.siftdown(A, i)

堆排序
运用堆的性质，我们可以得到一种常用的、稳定的、高效的排序算法————堆排序。堆排序的时间复杂度为O(n*log(n))，空间复杂度为O(1)，堆排序的思想是：对于含有n个元素的无序数组nums, 构建一个堆(这里是小顶堆)heap，然后执行extractMin得到最小的元素，这样执行n次得到序列就是排序好的序列。
如果是降序排列则是小顶堆；否则利用大顶堆。

'''

#lintcode 685
def firstUniqueNumber(self, nums, number):
        # Write your code here

        #建立一个dict去装所有的数字以及数字出现的次数
        counter = {}
        #便利这个数组，记录每个数字出现的个数
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1
        
        #遍历dict找到第一个出现一次的数组
        for num in nums:
            if counter[num] == 1:
                return num

