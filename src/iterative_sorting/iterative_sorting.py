# TO-DO: Complete the selection_sort() function below
def selection_sort(A):
    # loop through n-1 elements
    for i in range(0, len(A) - 1):
        curr_idx = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(A)):
            if A[curr_idx] > A[j]:
                curr_idx = j

        # TO-DO: swap
        # Your code here

        if curr_idx != i:
            A[curr_idx], A[i] = A[i], A[curr_idx]

    print ("Sorted array") 
    for i in range(len(A)): 
	    print("%d" %A[i]), 
    return A
# Traverse through all array elements 
# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(A): <---- I tired using my JS solution transcribed into Python... this didn't work at all
#     # Your code here
#     for i in range(len(A)):
#         if i >0:
#             i-=1
#         for j < i:
#             j=0
#             if j > i:
#                 j+=1
#         if A[j] > A[i]:
#             temp_value = A[j]
#             A[j] = A[j+1]
#             A[j+1] = temp_value
#     return A
def bubble_sort(A):
    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    n = len(A)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if A[i - 1] > A[i]:
                swap(i - 1, i)
                swapped = True
                    
    return A

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
