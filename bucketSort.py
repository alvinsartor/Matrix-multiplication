
def bucket_sort(arr, N):	
	C = [0] * N	
	
	for x in arr: 	
		C[x] += 1
	
	total = 0
	for i in range(N):
		c2 = C[i]
		C[i] = total	
		total += c2
	
	
	for x in arr:
		arr[C[x]] = x
		C[x] += 1
	

# -------------------- #

arr = [5, 125, 55, 105, 99, 42, 49, 1, 155, 45, 8, 9, 10]
print "\nUnsorted array:\n" + str(arr)
print "\n - SORTING (bucketSort) - \n"
bucket_sort(arr, 200)	
print "Sorted array:\n" + str(arr) + "\n"
