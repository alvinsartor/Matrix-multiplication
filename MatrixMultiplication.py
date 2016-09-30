def multiplication(m1, m2):
	res = []
	
	rM1 = len(m1)	
	cM1 = len(m1[0])	
	rM2 = len(m2)
	cM2 = len(m2[0])

	if (cM1 != rM2):
		print "the matrices are not compatibles -> [" + str(rM1) + ":" + str(cM1) + "] vs [" + str(rM2) + ":" + str(cM2) + "]"	
	else:			
		for r in range(0, rM1):
			tmpR = [0] * cM2	
			for c in range(0, cM2):
				val = 0
				for i in range(0, cM1):
					val += m1[r][i] * m2[i][c]
				tmpR[c] = val
			res.append(tmpR)
	return res	


m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8]]


print multiplication(m1,m2)
