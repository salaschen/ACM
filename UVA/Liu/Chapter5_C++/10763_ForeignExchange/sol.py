'''
Prob: python implementation for the UVA 10763 - Foreign Exchange problem
Date: 13/Aug/2017 
Author: Ruowei Chen
'''

def work():
	n = int(input()) ; 
	if n == 0:
		return 1 ; 
	record = dict() ; 
	for i in range(0, n):
		a,b = [int(s) for s in input().split()] ;
		if (b,a) not in record:
			if (a,b) not in record:
				record[(a,b)] = 1 ; 
			else:
				record[(a,b)] += 1 ; 
		else:
			record[(b,a)] = record[(b,a)] - 1 ; 
			if record[(b,a)] == 0:
				del record[(b,a)] ; 
	if len(record) == 0:
		print("YES") ; 
	else:
		print("NO") ; 
	return 0 ; 

def main():
	t = 0 ; 
	while work() == 0:
		t += 1 ; 

if __name__ == "__main__":
	main() ; 
