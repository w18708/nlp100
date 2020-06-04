s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
w=s.split()

word_list=list(w)
print(word_list)


n1={1,5,6,7,8,9,15,16,19}
data={}

n2=0
for name in word_list:
	n2+=1
	if n2 in n1:
		fi_name=name[0]
	else:
		fi_name=name[:2]
	data[fi_name]=n2
print(data)