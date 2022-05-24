from code_challenges.insertion_sort import insertion_sort


def test_two_elements():
  arr = [20,15]
  actual = insertion_sort(arr)
  expected = [15,20]
  assert actual == expected
