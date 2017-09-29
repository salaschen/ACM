'''
Oil Deposits, UVa 572
Date: 29/Sep/2017
Author: Ruowei Chen
'''

def getNeighbours(m, n, cur):
	result = [] ; 
	for i in range(cur[0]-1, cur[0]+2):
		for j in range(cur[1]-1, cur[1]+2):
			if i >= 0 and i < m and j >= 0 and j < n:
				result.append((i,j)) ; 
	return result ; 

def walk(m, n, start, toSearch, land):
	queue = [start] ; 
	while len(queue) > 0:
		# print(queue) ; # debug
		cur = queue.pop() ;
		if land[cur[0]][cur[1]] == '*':
			continue ; 
		neighbours = getNeighbours(m, n, cur) ; 
		# print("neighbours", neighbours) ;  # debug
		for nei in neighbours:
			if nei in toSearch and land[nei[0]][nei[1]] == '@':
				queue.append(nei) ; 
				toSearch.remove(nei) ; 
	return ; 

def work():
	m, n = [int(s) for s in input().split()] ; 
	if m == 0:
		return 1 ; 
	land = [] ; 
	toSearch = set() ; 
	for i in range(0, m):
		line = input() ; 
		row = [] ; 
		for j in range(0, len(line)):
			toSearch.add((i,j)) ; 
			row.append(line[j]) ; 
		land.append(row) ; 
	# print(land) ; # debug

	num = 0 ; 
	while len(toSearch) > 0:
	#	print(toSearch) ; # debug
		cur = toSearch.pop() ; 
		if land[cur[0]][cur[1]] == '@':
			num += 1 ; 
			walk(m, n, cur, toSearch, land) ; 
	print(num) ; 
	return 0 ;

def main():
	T = 0 ; 
	while work() == 0:
		T = T + 1 ; 
	return ; 

if __name__ == "__main__":
	main() ;
