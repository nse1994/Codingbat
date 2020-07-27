"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""
def cat_cnt(str):
  cat_cntr=0
  for i in range(0,len(str)-1):
    # if str[i]=='c' and str[i+1]=='a' and str[i+2]=='t':
    if str[i:i+3]=='cat':
      cat_cntr+=1
  return cat_cntr

def dog_cnt(str):
  dog_cntr=0
  for i in range(0,len(str)-1):
    # if str[i]=='d' and str[i+1]=='o' and str[i+2]=='g':
    if str[i:i+3]=='dog':
      dog_cntr+=1
  return dog_cntr

def cat_dog(str):
  a = cat_cnt(str)
  b = dog_cnt(str)
  if a==b:
    return True
  else:
     return False