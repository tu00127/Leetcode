#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
""" python的queue使用
from collections import deque
deque()
1.添加到右端
append(x)
2.添加到左端
appendleft(x)
3.pop(x)
移除並返回最右邊的元素
4.popleft(x)
移除並返回最左邊的元素 """

"""python 正負無窮
float('inf') 
 """

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        row = len(mat)
        col = len(mat[0])
        direction = [(-1,0), (0, -1), (1, 0), (0, 1)]

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
                
        
        while q:
            x , y = q.popleft()
            for dir_x, dir_y in direction:
                new_x, new_y = x + dir_x, y + dir_y
                if 0 <= new_x < row and 0 <= new_y < col and mat[new_x][new_y] > mat[x][y] + 1:
                    mat[new_x][new_y] = mat[x][y] + 1
                    q.append((new_x, new_y))
        
        return mat

        
# @lc code=end

