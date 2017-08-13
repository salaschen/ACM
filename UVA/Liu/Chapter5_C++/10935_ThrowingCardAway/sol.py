'''
Prob: UVA 10935 - Throwing cards away I
Date: 13/Aug/2017
Author: Ruowei Chen
'''
def work():
	n = int(input()) ; 
	if n == 0:
		return 1 ; 
	numList = [i for i in range(1, n+1)] ; 
	discard = [] ; 
	
	while len(numList) >= 2:
		discard.append(numList.pop(0)) ; 
		numList.append(numList.pop(0)) ; 

	result = "Discarded cards:" ; 
	if len(discard) == 0:
		result += "\n" ; 
	elif len(discard) == 1:
		result += " " + str(discard[0]) + "\n" ; 
	else:
		result += " " ; 
		for i in range(0, len(discard)-1):
			result += str(discard[i]) + ", ";
		result += str(discard[len(discard)-1]) + "\n"; 

	result += "Remaining card: " ; 
	result += str(numList[0]) ; 
	print(result) ; 
	return 0; 

def main():
	T = 0 ; 
	while work() == 0:
		T += 1 ; 
	return ; 

if __name__ == "__main__":
	main() ; 
