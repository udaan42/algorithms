##Given a string, find the length of the longest substring, which has no repeating characters

def non_repeat_substring(str):
  # TODO: Write your code here
  window_start,window_end = 0,0
  str_frequency= {}
  count = 0
  for window_end in range(len(str)):
    if str[window_end] in str_frequency:
      str_frequency[str[window_end]] += 1
    else:
      str_frequency[str[window_end]] = 1
    while any(v>1 for v in str_frequency.values()):
      str_frequency[str[window_start]] -= 1
      if str_frequency[str[window_start]] == 0:
        del str_frequency[str[window_start]]
      window_start += 1
    count = max(count, window_end - window_start + 1)

  return count
