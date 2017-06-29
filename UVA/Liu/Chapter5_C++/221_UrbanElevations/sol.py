
class Building:
	def __init__(self, line, ID):
		lst = [float(s) for s in line.split()]  ;
		self.x = lst[0] ;
		self.y = lst[1] ;
		self.w = lst[2] ; 
		self.d = lst[3] ; 
		self.h = lst[4] ;
		self.bid = ID ; 
	
	def __str__(self):
		result = "bld[{0:>3}]: x={1:>5} y={2:>5} w={3:>5} d={4:>5} h={5:>5}".format \
				(self.bid, self.x, self.y, self.w, self.d, self.h) ; 
		return result ; 


def cover(bld, mx):
	# check if the building has the mx inside
	return bld.x <= mx and (bld.x + bld.w) >= mx ; 

def visible(bld, mx, lst):
	# check if the building is visible at point mx
	if (not cover(bld, mx)):
		return False ; 
	for b in lst:
		if b.y < bld.y and b.h >= bld.h and cover(b, mx):
			return False ; 
	return True ; 

def work(c):
	num = int(input()) ; 
	if num == 0:
		return 1 ; # end of input
	bldList = [] ;
	for i in range(1, num+1):
		line = input() ; 
		bldList.append(Building(line, i)) ; 

	# get non-replicate x coordinates
	added = set() ; 
	xlist = []; 
	
	for b in bldList:
		if b.x not in added:
			added.add(b.x) ; 
			xlist.append(b.x) ; 
		if b.x+b.w not in added:
			added.add(b.x+b.w) ;
			xlist.append(b.x+b.w) ;
	xlist = sorted(xlist) ; 
#	print(xlist) ; # debug

	result = [] ;
	for i in range(0, len(bldList)):
		bld = bldList[i] ;
		for j in range(0, len(xlist)-1):
			mx = (xlist[j]+xlist[j+1])/2 ;
			if visible(bld, mx, bldList):
				result.append(bld.bid) ; 
				break ; 

	result = sorted(result, key=lambda indx: bldList[indx-1].y) ; 
	result = sorted(result, key=lambda indx: bldList[indx-1].x) ;
	if c > 1:
		print() ; 
	print("For map #%d, the visible buildings are numbered as follows:" % c) ; 
	strResult = str(result[0]) ; 
	for i in range(1, len(result)):
		strResult += " " + str(result[i]) ; 
	print(strResult) ; 


	# end of work function
	return 0 ;


def main():
	c = 1 ;
	while work(c) == 0 : 
		c += 1 ; 
	return 0 ;

if __name__ == "__main__":
	main() ; 
