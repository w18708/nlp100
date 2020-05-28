st='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words=st.replace(".","").replace(".","'').split(" ")

list=[]
for i in words:
     k=len(i)
     list.append(k)
print(list)