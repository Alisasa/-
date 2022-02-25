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

