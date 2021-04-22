# Longest Subarray with Ones after Replacement

def length_of_longest_substring(arr, k):
  # TODO: Write your code here
  window_start,window_end = 0,0
  count = 0
  int_freq = {}
  for window_end in range(len(arr)):
    if arr[window_end] not in int_freq:
      int_freq[arr[window_end]] = 1
    else:
      int_freq[arr[window_end]] += 1
    if int_freq.get(0) > k:
      int_freq[arr[window_start]] -= 1
      window_start += 1
    
    count = max(count, window_end - window_start + 1)
  return count
