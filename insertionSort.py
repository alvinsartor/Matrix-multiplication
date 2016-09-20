import commonFunctions

def inserion_sort(arr):		
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j - 1] > arr[j]:
			commonFunctions.swap(arr, j, j - 1)
			j = j - 1


	

# -------------------- #

arr = [5, 125, 55, 105, 99, 42, 49, 1, 155, 45, 8, 9, 10]
print "\nUnsorted array:\n" + str(arr)
print "\n - SORTING (inserionSort) - \n"
inserion_sort(arr)	
print "Sorted array:\n" + str(arr) + "\n"
