"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences 
(in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

def end_other(a,b):
  str = a.lower()
  str2 = b.lower()

  if len(str)>len(str2):
    length= len(str)-len(str2)
    test =str[length:]
    if test ==str2:
      return True
    return False
    
  else:
    length= len(str2)-len(str)
    test =str2[length:]
    if test ==str:
      return True
    return False
