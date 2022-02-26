## quick sort
## first to select the pivot value, saying last index
## create two pointers i and j, where i=low-1 and j=low
## moving j up to high-1(high is pivot index), 
## if nums[j]<=pivot, i++ and swap nums[i] and nums[j]
## at the end, swap nums[i] and pivot once again. 
## so now any index before pivot should be smaller value (not necessarily sorted)
## any index after pivot should be larger value. 

## the pivot selection is commonly first, last, middle. 
## simplest way just to select first and last, but ususally suffers worse performance
## select the middle usually ends up with better performance.
## in this example, we will select the last element as pivot

import random 

class QuickSort(object):
  def __init__(self, nums):
    self.nums = nums
  
  def quickSort(self):
    n = len(self.nums)
    self.recursion(self.nums, 0, n-1)

  def recursion(self, arr, low, high):
    if low < high:
      pivot = self.partition(arr, low, high)
      self.recursion(arr, low, pivot-1)
      self.recursion(arr, pivot+1, high)
  
  def partition(self, arr, low, high):
    i = low - 1
    pivot = high
    for j in range(low, high):
      if arr[j] < arr[pivot]:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1  ## make sure i need to be add 1 to finalize the swap and return the index


## simple test
if __name__ == '__main__':
  # nums = [40, 7, 45, 19, 2, 43, 45, 47, 44, 5, 20, 30, 13, 47, 13]
  nums = []
  for _ in range(15):
    nums += [random.randint(1, 50)]
  print(f'before sorting: {nums}')
  afterSort = QuickSort(nums)
  afterSort.quickSort()
  print(f'after sorting: {nums}')