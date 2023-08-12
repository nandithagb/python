import difflib
def simi(str1,str2):
    res=difflib.SequenceMatcher(None,str1,str2)
    return res.ratio()
print("enter the two strings")
s1=input("enter the string 1")
s2=input("enter the string 2")
print("str1=",s1)
print("str2=",s2)
print(simi(s1,s2))