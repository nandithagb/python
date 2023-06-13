word=input()
s=word.split(" ")
for i in s:
  if len(i)%2==0:
    print(i)