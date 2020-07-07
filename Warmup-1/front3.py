"""Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front."""
def front3(str):
  if len(str)==0:
    return str
  elif 1<len(str)<3:
    return str[0:2]+str[0:2]+str[0:2]
  else:
    return(str[0:3]+str[0:3]+str[0:3])
