import commonFunctions

def bubble_sort(arr):	
	i = 0
	while i < (len(arr) - 1):
		j = i + 1
		while j < len(arr):
			if arr[i] > arr[j]:
				commonFunctions.swap(arr, i, j)
			j = j + 1
		i = i + 1	
	


# -------------------- #

arr = [5, 125, 55, 105, 99, 42, 49, 1, 155, 45, 8, 9, 10]
print "\nUnsorted array:\n" + str(arr)
print "\n - SORTING (bubbleSort) - \n"
bubble_sort(arr)	
print "Sorted array:\n" + str(arr) + "\n"

