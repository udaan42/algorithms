# Permutation in a String

def find_permutation(str, pattern):
  # TODO: Write your code here
  window_start, window_end, i = 0,0,0
  result = []
  
  for window_end in range(len(str)):
    
    if str[window_end] in pattern:
      result.append(str[window_end])
      window_start = window_end + 1
      while i < len(pattern) - 1:
        if str[window_start] in pattern:
          result.append(str[window_start])
          window_start +=1 
          i += 1
        else:
          result.clear()
          break

    #print("length of result:", len(result))
    if len(result) == len(pattern):
      return True
            
  return False
