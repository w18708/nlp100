def  cipher(String):
		result=''
		for a in String:
			if a.islower():
				result+=chr(219-ord(a))
			else:
				result+=a
		return result
		
string ='Apple peN'

password=cipher(string)
print(password)

Decrytion=cipher(password)
print(Decrytion)