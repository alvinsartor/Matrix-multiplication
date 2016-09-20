
def merge_sort(arr):
	if (len(arr) > 1):
		mid = len(arr)//2
		le = arr[:mid]
		ri =  arr[mid:]
		merge_sort(le)
		merge_sort(ri)		
		
		i=0
		j=0
		k=0
		# merging
		while i < len(le) and j < len(ri):
		    if le[i] < ri[j]:
		        arr[k]=le[i]
		        i+=1
		    else:
		        arr[k]=ri[j]
		        j+=1
		    k+=1

		while i < len(le):
		    arr[k]=le[i]
		    i+=1
		    k+=1

		while j < len(ri):
		    arr[k]=ri[j]
		    j+=1
		    k+=1


# -------------------- #

arr = [5, 125, 55, 105, 99, 42, 49, 1, 155, 45, 8, 9, 10]
print "\nUnsorted array:\n" + str(arr)
print "\n - SORTING (mergeSort) - \n"
merge_sort(arr)	
print "Sorted array:\n" + str(arr) + "\n"
