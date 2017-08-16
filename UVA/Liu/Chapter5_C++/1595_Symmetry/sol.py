'''
Python solution for the Symmery, ACM/ICPC Seoul 2004, UVa 1595.
Date: 16/Aug/2017 
Author: Ruowei Chen
'''

def getCentre(points):
	notFound = -20000 ; 
	result = notFound ; 
	points = sorted(points, key=lambda p: p[0]) ; 
	while len(points) > 0:
		if len(points) == 1:
			if result == notFound or result == points[0][0]:
				return points[0][0] ; 
			elif result != points[0][0]:
				return notFound ; 
		else: # list has at least two points.
			centre = (points[0][0] + points[len(points)-1][0])/2 ; 
			if result == notFound:
				result = centre ; 
			elif result != centre:
				return notFound ; 
			points.pop(0) ; 
			points.pop(len(points)-1) ; 
	return result ; 
	

def work():
	N = int(input()) ; 
	points = [] ;
	for i in range(0, N):
		x,y = [int(s) for s in input().split()] ; 
		points.append((x,y)) ; 

	points = sorted(points, key=lambda p: p[1]) ; 
# 	print(points) ; # debug
	
	cur = 0 ;
	centreX = -20000 ; # less than any possible centre point
	while cur < N:
		sameY = [] ; 
		curY = points[cur][1] ; 
		sameY.append(points[cur]) ; 
		cur += 1 ;
		while cur < N and points[cur][1] == curY:
			sameY.append(points[cur]) ; 
			cur += 1 ; 
		curCentre = getCentre(sameY) ; 
		if curCentre < -10000:
			print("NO") ;
			return ;  
		if centreX < -10000:
			centreX = curCentre ; 
		elif centreX != curCentre:
			print("NO") ; 
			return ;

	print("YES") ; 
	return ; 

def main():
	T = int(input()) ; 
	for i in range(0, T):
		work() ; 

if __name__ == "__main__":
	main() ; 
