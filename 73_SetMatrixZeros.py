"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/3/1.
"""


class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		M = len(matrix)
		N = len(matrix[0])
		is_row = False

		for m in range(0,M):
			for n in range(0,N):
				if matrix[m][n] == 0:
					if m == 0 and n == 0:
						matrix[0][0] = 0
						is_row = True
					elif m == 0:
						matrix[0][0] = 0
					elif n == 0:
						is_row = True
					else:
						matrix[m][0] = 0
						matrix[0][n] = 0

		# row to 0
		for m in range(1,M):
			if matrix[m][0] == 0:
				for n in range(1,N):
					matrix[m][n] = 0

		for n in range(1,N):
			if matrix[0][n] == 0:
				for m in range(1,M):
					matrix[m][n] = 0

		if matrix[0][0] == 0:
				for n in range(1, N):
					matrix[0][n] = 0

		if is_row:
			for m in range(0,M):
				matrix[m][0] = 0
		return


if __name__ == '__main__':
    so =Solution()
    mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    so.setZeroes(mat)
    print(mat)
