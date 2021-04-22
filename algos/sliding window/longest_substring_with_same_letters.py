#Longest Substring with Same Letters after Replacement



def length_of_longest_substring(str, k):
  # TODO: Write your code here
  window_start,window_end, max_freq_char_count = 0,0,0
  str_frequency= {}
  count = 0
  for window_end in range(len(str)):
    print(str[window_end])
    if str[window_end] in str_frequency:
      str_frequency[str[window_end]] += 1
    else: 
      str_frequency[str[window_end]] = 1
    max_freq_char_count = max(max_freq_char_count, str_frequency[str[window_end]] )
    print("Str Frequency:", str_frequency[str[window_end]])

    if (window_end - window_start + 1 - max_freq_char_count) > k:
      str_frequency[str[window_start]] -= 1
      window_start += 1
      
    count = max(count, window_end - window_start + 1)
  return count

 