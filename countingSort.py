import time

def counting_sort(arr, N):	
	C = [0] * N	
	
	for x in arr: C[x] += 1

	i = 0
	for a in range(N):          
		for c in range(C[a]): 			
			arr[i] = a
			i += 1


# -------------------- #




arr = [5, 125, 55, 105, 99, 42, 49, 1, 155, 45, 8, 9, 10]
print "\nUnsorted array:\n" + str(arr)
print "\n - SORTING (countingSort) - \n"
start_time = time.time()
counting_sort(arr, 200)	
print "Sorted array:\n" + str(arr) + "\n"
print("--- %s seconds ---" % (time.time() - start_time))
