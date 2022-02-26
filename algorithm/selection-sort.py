## selection insertion
## divided into sorted and unsorted list. 
## each iteration select the min value from unsorted,
## and placed it into the min index of unsorted list. 

import random 

class SelectionSort(object):
  def __init__(self, nums):
    self.nums = nums
  
  def selectionSort(self):
    res = self.nums
    n = len(res)
    for i in range(n):
      minIdx = j = i
      while j < n:
        if res[j] < res[minIdx]:
          res[j], res[minIdx] = res[minIdx], res[j]
        j += 1
    return res


## simple test
if __name__ == '__main__':
  nums = []
  for _ in range(15):
    nums += [random.randint(1, 50)]
  print(f'before sorting: {nums}')
  afterSort = SelectionSort(nums)
  print(f'after sorting: {afterSort.selectionSort()}')