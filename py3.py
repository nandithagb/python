s=input()
def printWords(s):
     
    # split the string
    s = s.split(' ')
     
    # iterate in words of string
    for word in s:
         
        # if length is even
        if len(word)%2==0:
            print(word)
 
 

printWords(s)