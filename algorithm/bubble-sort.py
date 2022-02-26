
class BubbleSort(object):
  def __init__(self, nums):
    self.nums = nums
  
  def bubbleSort(self):
    n = len(self.nums)
    completed = False
    result = self.nums

    while not completed:
      cnt = 0
      for i in range(1, n):
        if result[i-1] > result[i]:
          result[i-1], result[i] = result[i], result[i-1]
        else:
          cnt += 1
      if cnt == n-1: completed = True
    
    return result

## simple test
if __name__ == '__main__':
  numbers = [2,6,3,5,1,10,8]
  example = BubbleSort(numbers)
  print(example.bubbleSort())
  