import commonFunctions
import time

def partition(arr, lo, hi):
	pivotVAL = arr[lo]
	i = lo + 1
	j = hi		
	done = False	
	
	while not done:
		while i <= j and arr[i] <= pivotVAL: i = i + 1
		while arr[j] >= pivotVAL and j >= i: j = j - 1
		
		if j < i: done = True			
		else: commonFunctions.swap(arr, i, j)
	commonFunctions.swap(arr, lo, j)	
	return j


def quick_sort(arr, lo, hi):		
	if lo > hi:
		return
	else:
		pivotPT = partition(arr, lo, hi)
		quick_sort(arr, lo, pivotPT - 1)
		quick_sort(arr, pivotPT + 1, hi)


def hat_quick_sort(arr): 
	quick_sort(arr, 0, len(arr) - 1)




# -------------------- #

arr = [5, 125, 55, 105, 99, 42, 49, 1, 155, 45, 8, 9, 10]
print "\nUnsorted array:\n" + str(arr)
print "\n - SORTING (quickSort) - \n"
start_time = time.time()
hat_quick_sort(arr)	
print "Sorted array:\n" + str(arr) + "\n"
print("--- %s seconds ---" % (time.time() - start_time))



