def merge_sort(arr):
  n = len(arr)
  # print(f'split {arr}')
  if n > 1:
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)
  
  return arr


def merge(left, right, arr):
  i = j = k = 0
  # print(f'merge: left {left}, right {right}')
  while i < len(left) and j < len(right):
    # print(f'smallest of {left[i:]} and {right[j:]}')
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    # print(f'appending {arr[k]}')
    k += 1
    # print(f'results in {arr[:k]}')
  if i == len(left):
    for x in range(j, len(right)):
      # print(f'append remaining entry {right[x]}')
      arr[k] = right[x]
      k += 1
  else:
    for x in range(i, len(left)):
      # print(f'append remaining entry {left[x]}')
      arr[k] = left[x]
      k += 1
  print(f'result of merge {arr}')


if __name__ == '__main__':
  nums = [8,4,23,42,16,15]
  merge_sort(nums)
  print(f'sorted {nums}')
