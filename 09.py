import random

s='I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
words=s.split()
#print(words)
pp=''
for i in range(len(words)):
 if len(words[i])>4:
  kk=''.join(list(words[i][0])+random.sample(words[i][1:-1],(len(words[i])-2))+list((words[i])[-1]))
  pp += (kk + ' ')
 else:
  kk=''.join(words[i])
  pp += (kk + ' ')
print(pp)