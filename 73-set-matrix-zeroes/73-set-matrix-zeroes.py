class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		
		isCol = False
		for i in range(len(matrix)):
			if matrix[i][0] == 0:
				isCol = True
			for j in range(1,len(matrix[0])):
				if not matrix[i][j]:
					matrix[i][0] = 0
					matrix[0][j] = 0
		for i in range(1,len(matrix)):
			for j in range(1,len(matrix[0])):
				if not matrix[i][0] or not matrix[0][j]:
					matrix[i][j] = 0
		if not matrix[0][0]:
			for j in range(len(matrix[0])):
				matrix[0][j] = 0
		if isCol:
			for i in range(len(matrix)):
				matrix[i][0] = 0
			
			
	
					
		