

import random


def swap(target):
	result=[]
	for word in target.split(' '):
		if len(word)<=4:
			result.append(word)
			
		else:
			cc_list=list(word[1:-1])
			random.shuffle(cc_list)
			result.append(word[0]+''.join(cc_list)+word[-1])
			
		return ' '.join(result)
target=input('>')

final=swap(target)
print(target)
print(final)