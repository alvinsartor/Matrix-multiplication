
def FW(M):
	length = len(M)
	for i in range(0,length):
		for j in range(0,length):
			for k in range(0,length):
				if W[j][k] > W[j][i] + W[i][k]:
					W[j][k] = W[j][i] + W[i][k]
	return M
