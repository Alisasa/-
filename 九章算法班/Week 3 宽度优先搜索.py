BFS使用场景：
（1）分层遍历，找所有方案（用非递归实现）
    简单图的最短路径 （复杂图还可以用Floyd，dijsktra解决，但这一般都要背可以不学。还有SPFA可以学学）
                    如果问最长路径的话BFS不可以做（一般不会考）
    （分层的意思是，路径有一定方向性，不能绕圈）
（2）连通块的问题(通过一个点找到所有点)    这个一般不用dfs做因为容易stack overflow
（3）扑拓排序(基于有向图), (先修课程问题），是排序，但排的是依赖性
以上3种都可以用dfs做，但最好用bfs做，因为用dfs会stack overflow
为什么BFS可以做最短路径？
图跟树不一样，图可能会有环。但BFS的时候，第二次访问到访问过的点，会获得一条更短路径呢？没有可能。
BFS是把所有走0步就能走到的点放到第一层，把所有走1步就能走到的点放第二层，所有走2步能走到的点放第三层。
所以BFS才可以算最短路径。
用哈希表来记录，每个节点访问情况（如果存在哈希表keys里，就说明访问过了；value记录的是到根的距离）
【拓扑排序】
入度：  in-degree
有向图： Directed Graph （这样才有依赖性）
必须没有环，才可以进行拓扑排序
一个图可能存在多个拓扑序，也可能不存在任何拓扑序
算法描述：
1.统计每个点的入度
2.将入度为0的点(不依赖于任何其他的点)，首先放到队列中去
3.不断从队列里拿出一个点，把这个点连向的点的入度都-1
4.然后把 新的入度为0的点，丢回队列中
重复3和4直到完，那些元素依次出队列(或进队列)的顺序就是拓扑排序
  A ->
        B    左边拓扑排序是 ACB 或 CAB 都是对的其实
  C ->       除非要求你输出的是 字典最小的拓扑排序 就是 ACB 了
            而如果要你按字典序输出的话，普通的queue就要换成priority queue了
问题的问法包括：
（1）求任意一个拓扑排序
（2）是否存在拓扑排序         （这个和上个问题用一份代码就可以解决 领扣616和127）
（3）是否存在且仅存在一个拓扑序 （queue的size要么是0或1，从来不会变成2   代码是领扣605）
（4）按字典序最小，来排拓扑序   （queue用priority queue）
 
                 
 # 通用模板：
 queue = collection.deque([node]) # 注意这里加入[] 里面是iterable，必须放一串东西，可以放tuple，string，list
 distance = {node : 0} #建立一个hash map， 去重；需要求距离的时候就加 不需要就不加
 
 while queue:
     node = queue.popleft()
     for neighbor in node.get_neighbors():
         if neighbor in distance:
             continue
         distance[neighbor] = distance[node] + 1
         queue.append(neighbor)
         
# N个点 M条边 时间复杂度 = O(N+M) 最坏O(N2)

#lintcode 618 给定一张 无向图，一个 节点 以及一个 目标值，返回距离这个节点最近 且 值为目标值的节点，如果不能找到则返回 NULL。
在给出的参数中, 我们用 map 来存节点的值
#套用模板
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            n = queue.popleft()
            if values[n] == target:
                return n
            for neighbor in n.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return None

#lintcode 137题 克隆图
#deep copy Vs shallow copy:完整的克隆；拷贝最上面一层
#main idea:寻找点、复制点、复制边
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
        #step1:找到所有点
        nodes = self.find_nodes_by_bfs(node)
        #step2:复制所有的点（建立映射关系）
        mapping = self.copy_nodes(nodes)
        #step3:复制所有的边
        self.copy_edges(nodes,mapping)

        return mapping[node]

    #step1:找到所有点
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)
        
    #step2:复制所有的点（建立映射关系）
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping
    #step3:复制所有的边
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            #旧点有哪些旧邻居，新点就有哪些新邻居
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
                
                
#lintcode 120题 单词接龙 给两个单词（start，end）一个字典，找出从start到end的最短转换序列，输出最短序列长度
#注意最短序列 -- BFS

def ladderLength(self, start, end, dict):
        # write your code here
        #注意要把end加进去 end有可能在有可能不在
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        distance = 0 

        while queue:
            distance += 1
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == end:
                    return distance
                for next_word in self.find_next_words(word, dict):
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)   
        return 0
'''如果dict里词过多 则会超时 时间复杂度 = N*L = 1000（dict里的词数量）*10（单词长度）
    def find_next_words(self, word, dict):
        next_words = []
        for next_word in dict:
            has_one_diff = False
            for i in range(len(word)):
                if (next_word[i] != word[i]):
                    if has_one_diff:
                        has_one_diff = False
                        break
                    has_one_diff = True
            if has_one_diff:
                next_words.append(next_word)
        return next_words '''
    #时间复杂度 26*L*L 比上面一种方法时间复杂度要小
    def get_next_words(self, word, dict):
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                new_word = left + char + right
                #注意有条件，如果这个单词在dict里，则加入next_words list，如果不在list就压根不用考虑此单词
                if new_word in dict:
                    next_words.append(new_word)
        return next_words    
              
#lintcode 433题 岛屿数量 如果0就是海洋 1是岛屿 求岛屿数量
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        #set记录某点是否被bfs过
        visited = set()
        #len(grid)代表有几行row； len(grid[0])代表有几列colum；两个for就能遍历grid里所有的点
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #如果grid=True（是1）并且这个点没有被访问过，遍历他周围的点找到所有相连的1
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands

    def bfs(self, grid, x, y, visited):
        DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        queue = collections.deque([(x,y)])
        visited.add((x,y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.isvalid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                
    #判断一个点是否可以被bfs 
    def isvalid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        #如果出界，返回false
        if not(0 <= x < n and 0 <= y < m):
            return False
        #如果访问过，返回false
        if (x, y) in visited:
            return False
        #如果是1，则为true，如果是0，则为false
        #逻辑表达式里非 0 元素为真
        return grid[x][y]

#lintcode 598僵尸矩阵 给一个二维网格grid，2代表墙，1代表僵尸， 0代表人类，僵尸每天可以感染上下左右的人，但不能穿墙，将所有人类感染为僵尸需要多久，如果不能感染所有人则返回 -1。
#和岛屿那一题思路一致
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
from collections import deque

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # 特殊情况处理
        if not grid or not grid[0]:
            return -1
        day = 0
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #如果grid = True（是1）且这个点没有遍历过，遍历周围的点并把周围的点变成0
                if grid[i][j] == 1:
                    queue.append((i, j))
        day = self.bfs(grid, queue, 0)
        #感染完所有的人后，看grid里还有没有0，如果有，返回-1，如果没有，返回day
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1
        return day   

    def bfs(self, grid, queue, day):
        while queue:
            day += 1
            size = len(queue)
            for k in range(size):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    next_x, next_y = x + dx, y + dy
                    if not self.is_valid(grid, next_x, next_y):
                        continue
                    grid[next_x][next_y] = 1
                    queue.append((next_x, next_y))
        return day - 1

    def is_valid(self,grid, x, y):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y <m):
            return False
        if grid[x][y] != 0:
            return False
        return True

#lintcode 611题 骑士的最短路线
DIRECTION = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # 注意这里如何加入deque ([()])加入一个可迭代的需要外面加[],list,tuple,不能加单独的字符串
        queue = collections.deque([(source.x, source.y)])
        distance_dict = {(source.x, source.y) : 0}
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance_dict[(x, y)]
            #遍历8个不同方向
            for delta_x, delta_y in DIRECTION:
                next_x = x + delta_x
                next_y = y + delta_y
                #如果这些方向不合法/已经加入到dict里，忽略、继续
                if not self.isvalid(grid, next_x, next_y) or (next_x, next_y) in distance_dict:
                    continue
                #加入queue，加入dict里
                queue.append((next_x, next_y))
                distance_dict[(next_x, next_y)] = distance_dict[(x, y)] + 1
        return -1
    def isvalid(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        #超过范围了，false
        if not(0 <= x < m and 0 <= y < n):
            return False
        #有1障碍物时为false
        return not grid[x][y]                
               
 #lintcode 630题 骑士最短路径 与上题相似，初始点（0，0）要到达（n-1，m-1）并且只能从左到右的走，即偏移量只有4个，0为空，1为有障碍物
 #设置偏移量
DIRECTIONS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        n = len(grid)
        m = len(grid[0])
        print(n, m)
        #特殊情况处理
        if not grid or not grid[0]:
            return -1
        #把起点加入queue
        queue = collections.deque([(0,0)])
        #做一个dict把起点和对应的distance加入
        visited = {(0,0) : 0} 
        while queue:
            x, y = queue.popleft()
            if (x, y) == (n-1, m-1):
                return visited[(x, y)]
            #遍历起点能到达的所有点
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                print((next_x, next_y))
                #如果这个点不valid或者已经在visited里面（遍历过）则继续
                if not self.is_valid(grid, next_x, next_y) or (next_x, next_y) in visited:
                    continue
                #否则，加入queue和vistied，继续遍历这些点，看是否能到达终点
                queue.append((next_x, next_y))
                visited[(next_x, next_y)] = visited[(x, y)] + 1
        return -1

    def is_valid(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        if not(0 <= x < n and 0 <= y <m):
            return False
        return grid[x][y] == 0

 #lintcode 178 给出 n 个节点，标号分别从 0 到 n - 1 并且给出一个 无向 边的列表 (给出每条边的两个顶点), 写一个函数去判断这张｀无向｀图是否是一棵树
 class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        #树的定义 # of node = # of edges + 1
        if len(edges) != n - 1:
            return False
        #邻接表
        neighbors = {i:[] for i in range(n)}
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        print(neighbors)
        visited = {}
        queue = collections.deque([0])
        visited[0] = True
        print(visited)
        
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            print(neighbors[cur])
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)
        print(visited)
        return len(visited) == n

#127 拓扑排序 经典方法 可以当作模板
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        #define indegree with dict
        indegree = dict((i,0) for i in graph)
        print(indegree)
        #求出每个node有几个箭头指向它
        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1          

        
        queue = collections.deque()
        for i in graph:
            #0个箭头指向的node加入queue
            if indegree[i] == 0:
                queue.append(i)
        #result and bfs       
        result = []        
        while queue:
            node = queue.popleft()
            result.append(node)
            for j in node.neighbors:
                indegree[j]-=1
                if indegree[j] == 0:
                    queue.append(j)            
        return result
 #616 
 class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        #建立邻接表
        edges = {i:[] for i in range(numCourses)}
        degree = [0] * numCourses
        for i, j in prerequisites:
            edges[j].append(i)
            degree[i] += 1
        print(edges)
        print(degree)
        queue = collections.deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        num_choose = 0
        result = []
        while queue:
            cur_cos = queue.popleft()
            result.append(cur_cos)
            num_choose += 1
            for next_cos in edges[cur_cos]:
                degree[next_cos] -= 1
                if degree[next_cos] == 0:
                    queue.append(next_cos)
        return result if num_choose == numCourses else []
