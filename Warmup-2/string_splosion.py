""" 
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

"""

def string_splosion(str):
  i =len(str)
  string =""
  n=1
  
  while i!=0:
    l=str[0:n]
    string =string + l
    i=i-1
    n+=1
  return string
