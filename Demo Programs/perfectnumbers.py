'''
factors = [1,2,3,4,6]

sum = sum(factors)
total = 12

if sum == total:
	print(sum) 

elif sum < total: 
	print("abundant")

elif sum > total: 
	print("deficent")
'''
def getFactors(value): 
	factorList = []
	for f in range (1,value//2 + 1):
		if value % f == 0: 
			factorList.append(f)
	return factorList

def sumList(list):
	total = 0 
	for n in list: 
		total+= n
	return total

def printPerfect(number,factorTotal):
	if number == factorTotal:
		print(number)

#main 
for num in range (2,10001):
	factors = getFactors(num)
	factorSum = sumList(factors)
	printPerfect(num,factorSum)
print("List Complete")