s='paraparaparadise'
s1='paragraph'

def gram(t,num) :
    cr = [t[n:n+num] for n in range(len(t)+1-num)]
    return cr

k=gram(s,2)
print(k)
h=gram(s1,2)
print(h)

uni=k|h
int_sec=k&h
dif=k-h
print(uni)
print(int_sec)
print(dif)
print('se'in k)
print('se'in h)