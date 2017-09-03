'''
Problem: Do you Know the Way to San Jose
Date: 01/Sep/2017
Author: Ruowei Chen
'''
import math ;

def readInput(maps, locations, requests):
	line = input().strip() ; 
	if line == "MAPS":
		line = input().strip() ; 
	while line != "LOCATIONS":
		p = line.split() ; 
		p[1:] = [float(i) for i in p[1:]] ; 
		maps[p[0]] = (p[1], p[2], p[3], p[4], abs((p[1]-p[3])*(p[2]-p[4]))) ; 
		line = input().strip() ; 
	if line == "LOCATIONS":
		line = input().strip() ; 
	while line != "REQUESTS":
		name, x, y = line.split() ; 
		x, y = float(x), float(y) ;
		locations[name] = (x,y) ;
		line = input().strip() ;
	if line == "REQUESTS":
		line = input().strip() ; 
	while line != "END":
		name, level = line.split() ; 
		level = int(level) ; 
		requests.append((name, level)) ; 
		line = input().strip() ; 
	return ; 

def isInside(locCoord, mapCoord):
	# locCoord: (x,y)
	# mapCoord: (x1, y1, x2, y2)
	x1, y1, x2, y2 = mapCoord ; 
	x, y = locCoord ;
	minX = min(x1, x2) ; 
	maxX = max(x1, x2) ; 
	minY = min(y1, y2) ; 
	maxY = max(y1, y2) ; 
	return x >= minX and x <= maxX and y >= minY and y <= maxY ; 

def lowerRightCorner(mapCoord):
	x1, y1, x2, y2 = mapCoord ; 
	return (max(x1, x2), min(y1, y2)) ; 

def centre(mapCoord):
	x1, y1, x2, y2 = mapCoord ; 
	return ((x1+x2)/2, (y1+y2)/2) ; 

def dist(coord1, coord2):
	return math.sqrt(pow(coord1[0]-coord2[0], 2) + pow(coord1[1]-coord2[1], 2)) ;

def getMapCoord(maps, mk):
	return maps[mk][:4] ; 

def diffRatio(maps, mk, target=0.75):
	x1, y1, x2, y2 = maps[mk][:4] ; 
	height = abs(y1-y2) ; 
	width = abs(x1-x2) ; 
	return abs(height/width - target) ; 

def process(maps, locations):
	result = dict() ;
	for lk in locations:
		mapList = [] ; 
		for mk in maps:
			if isInside(locations[lk], maps[mk][:4]) == True:
				mapList.append(mk) ;
		
		# sorting for least x-coord
		mapList = sorted(mapList, key=lambda mk: min(maps[mk][0], maps[mk][2])) ; 
		# sort for furthest away from lower right corner of map
		mapList = sorted(mapList, reverse=True,\
			key=lambda mk: dist(locations[lk], lowerRightCorner(getMapCoord(maps, mk)))) ; 
		# sort for closet to 0.75 height:width ratio
		mapList = sorted(mapList, key=lambda mk: diffRatio(maps, mk)) ; 
		# sort for closest to centre point
		mapList = sorted(mapList, key=lambda mk: \
			dist(locations[lk], centre(getMapCoord(maps, mk)))) ; 
		# sort for level of details
		mapList = sorted(mapList, reverse=True, key=lambda mk: maps[mk][4]) ; 

		result[lk] = mapList ; 
	return result ; 

def handleRequest(request, locs):
	name, level = request ; 
	result = name + " at detail level " + str(level) + " " ; 
	if name not in locs:
		result += "unknown location" ; 
	elif len(locs[name]) == 0:
		result += "no map contains that location" ; 
	else:
		mk = level-1 ; 
		if len(locs[name]) < level:
			mk = len(locs[name]) - 1 ; 
			result += "no map at that detail level; " ;
		result += "using " + locs[name][mk] ; 
	print(result) ; 
	return ; 

def work():
	maps = dict() ; # name -> tuple(x1, y1, x2, y2, area)
	locations = dict() ; # name -> tuple(x,y)
	requests = [] ; # tuple(name, level)
	
	readInput(maps, locations, requests) ; 
	locs = process(maps, locations) ;

	# debug
	'''
	print(maps) ; 
	print() ;
	print(locations) ;
	print() ; 
	print(locs) ; 
	print() ; 
	'''

	for r in requests:
		handleRequest(r, locs) ; 

	return ; 

def main():
	work() ;
	return ; 

if __name__ == "__main__":
	main() ;
