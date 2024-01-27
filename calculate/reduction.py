from common import MAX_REPEAT, MAX_LENGTH

def ski_calculator_reduce(term):
  reduced = True
  for i in range(len(term)):
    if (3 <= i) and (term[i-3:i+1] == "AAAS"):
      a = 1
      j = i+1
      while a != 0:
        if term[j] == "A":
          a += 1
        else:
          a -= 1
        j += 1    
      k = j
      a = 1
      while a != 0:
        if term[j] == "A":
          a += 1
        else:
          a -= 1
        j += 1
      l = j
      a = 1
      while a != 0:
        if term[j] == "A":
          a += 1
        else:
          a -= 1
        j += 1 
      term = term[:i-3] + "AA" + term[i+1:k] + term[l:j] + "A" + term[k:]
      reduced = False
      break
    if (2 <= i) and (term[i-2:i+1] == "AAK"):
      a = 1
      j = i+1
      while a != 0:
        if term[j] == "A":
          a += 1
        else:
          a -= 1
        j += 1    
      k = j
      a = 1
      while a != 0:
        if term[j] == "A":
          a += 1
        else:
          a -= 1
        j += 1
      term = term[:i-2] + term[i+1:k] + term[j:]
      reduced = False

    if (1 <= i) and (term[i-1:i+1] == "AI"):
      a = 1
      j = i+1
      while a != 0:
        if term[j] == "A":
          a += 1
        else:
          a -= 1
        j += 1
      term = term[:i-1] + term[i+1:]
      reduced = False
      break

  return term, reduced

def repeat_reduce(term, max_repeat=MAX_REPEAT, max_length=MAX_LENGTH):
  i = 0
  while i < max_repeat:
    term, reduced = ski_calculator_reduce(term)
    i += 1
    if reduced == True:
      return term

    if len(term) > max_length:  
      return None