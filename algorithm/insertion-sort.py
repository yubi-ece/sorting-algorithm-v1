## insertion sort divided into sorted and unsorted parts. 
## each iteration insert one value from unsorted, and insert it into the sorted list. 
import random

class InsertionSort(object):
  def __init__(self, nums):
    self.nums = nums

  def insertionSort(self):
    res = self.nums
    n = len(self.nums)
    for i in range(n):
      key = res[i]   ## key is the value to be inserted
      j = i - 1
      while j>=0 and res[j]>key:
        res[j+1] = res[j]
        j -= 1
      res[j+1] = key
    return res

## simple test
if __name__ == '__main__':
  # nums = [12, 11, 13, 5, 6]
  nums = []
  for _ in range(15):
    nums += [random.randint(1,50)]
  print(f'before sorting: {nums}')
  example = InsertionSort(nums)
  print(f'after sorting: {example.insertionSort()}')