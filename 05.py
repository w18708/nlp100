
def gram(target,n) : 
    cr = [target[x:x + n] for x in range(len(target) - (n - 1))] 
    return cr

s = "I am an NLPer"

s_word = s.split()

print(gram(s,1))
print(gram(s,2))
print(gram(s,3))

print(gram(s_word,1))
print(gram(s_word,2))
print(gram(s_word,3))