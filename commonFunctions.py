
SHOW_SWAPS = True

def swap(arr, a, b):
	keep = arr[a]
	arr[a] = arr[b]
	arr[b] = keep
	if SHOW_SWAPS: print arr
