'''
Python solution for the Uva 207 - PGA Money Prize
Date: 18/Jun/2017
'''
import functools
import math

class Player:
	# Player Constructor
	def __init__(self, nameStr, scoreStr, identity):
		self.name = nameStr ; 
		self.isDQ = False ;
		self.place = "" ; 
		self.money = -1.0 ;
		self.identity = identity ; 
		if self.name.count("*") != 0:
			self.isAmateur = True ; 
		else:
			self.isAmateur = False ; 
		self.scores = [] ;
		for i in range(0, 4):
			s = scoreStr[i*3:i*3+3]; 
			if s == "DQ":
				self.scores.append(9999) ; 
				self.isDQ = True ; 
			elif s.strip().isdigit() == False:
				self.scores.append(9999) ;
			else:
				self.scores.append(int(s)) ;
	def id(self):
		return self.identity ; 

	def isDQinFirstTwo(self):
		return self.scores[0] > 999 or self.scores[1] > 999 ; 

	def isDQinLastTwo(self):
		return (self.isDQinFirstTwo == False) and  self.isDQ ; 
	
	def __eq__(self, other):
		return self.name == other.name ;

	def total(self):
		return functools.reduce(lambda a,b: a+b, self.scores) ; 

	# For printing service
	def __str__(self):
		result = padWord(self.name.strip(), 21) ; # name
		result += padWord(str(self.place), 10) if self.isDQ == False \
				else padWord("", 10) ; 
		total = 0 ; 
		for i in range(0, 4):
			if self.scores[i] == 9999:
				result += padWord("", 5) ; 
			else:
				result += padWord(str(self.scores[i]), 5) ; 
				total += self.scores[i] ; 
		
		result += padWord("DQ", 2) if self.isDQ else padWord(str(total), 3) ; 
		if self.isDQ or self.isAmateur or self.money < 0.0:
			return result ; 
		result += " " * 7 ; 
		# result += padWord("DQ",10) if self.isDQ else padWord(str(total), 10)  ;
		money = "" ; 
		if self.money >=  0.0:
			spf = math.floor(self.money * 100000) ; 
			spf = spf / 100 ;
			'''
			if spf >=  6683894 and spf <= 6683896:
				result += " " + str(spf % 10 >= 5) ;  #debug
			'''
			if (spf % 10) >= 5:
				spf = math.floor((spf/10 + 1)) / 100 ;
			else:
				spf = spf / 1000 ; 
			m = "{:.2f}".format(spf) ; 
			m = " " * (9 - len(m)) + m ;
			money = "$" + m ;
		result += money ; 
		
#		result += " " + "{:.6f}".format(self.money) ; # debug
		return result ; 

def padWord(word, totalLen):
	result = word + " " * (totalLen-len(word)) ; 
	return result ; 


def makeRank(players, funcGetScore):
	curRank = 0 ; 
	curScore = 0  ; # lower than every one
	count = 1 ; 
	for i in range(0, len(players)):
		p = players[i] ; 
		if funcGetScore(p) == curScore:
			count +=1 ;
			p.place = str(curRank) ; 
		else:
			curRank += count ; 
			count = 1 ; 
			p.place = str(curRank); 
			curScore = funcGetScore(p) ; 
	return players ;

def allocateMoney(players, total, dist):
	curPos = 0 ; 
	curDist = 0 ; 
	
	while curPos < len(players) and curDist < len(dist):
		p = players[curPos] ; 
		# go down to find players
		count = 1 ; 
		pool = dist[curDist] ; 
		i = 1 ; 
		while (curPos+i < len(players) 
				and players[curPos+i].total() == p.total()):
			count += 1 ;
			i += 1 ; 
		
		# update the pool
		i = 1 ; 
		while (i < count and i+curDist < len(dist)):
			pool += dist[curDist+i] ; 
			i += 1 ; 
		curDist += i ; 

		for i in range(0, count):
			players[curPos+i].money = 0.010*total*pool/count ;
			if count >= 2:
				players[curPos+i].place += "T" ; 

		curPos += count ; 

	return players; 

def work():
	input() ; # skip the empty line.
	# Read in the prize money and allocation
	total = float(input()) ; 
	dist = [] ; 
	for i in range(0, 70):
		dist.append(float(input())) ; 
	
	# Read in the player data 
	players = [] ;
	numPlayer = int(input()) ;
	for i in range(0, numPlayer):
		line = input(); 
		nameStr = line[0:21] ; 
		scoreStr = line[21:] ; 
		players.append(Player(nameStr, scoreStr, i+1)) ; 

	# eliminate people who's disqualified within the 
	# first two rounds.
	first = filter(lambda s: s.isDQinFirstTwo() == False, players) ; 
	first = sorted(first, key=lambda player: player.name) ;
	first = sorted(first, key=lambda player: player.scores[0]+player.scores[1]) ;
	# determine the rank of in the first two round.
	first = makeRank(first, lambda p: p.scores[0]+p.scores[1]) ;
	first = filter(lambda s: int(s.place) <= 70, first) ;

	first = sorted(first, key=lambda player: player.name) ;
	first = sorted(first, key=lambda player: player.total()) ;
	first = makeRank(first, lambda p: p.total()) ; 

	# allocate the money to professional players
	moneyPlayers = [] ;
	for p in first:
		if p.isDQ == False and p.isAmateur == False:
			moneyPlayers.append(p) ; 

	nonMoneyPlayers = [] ; 
	for p in first:
		if p not in moneyPlayers:
			nonMoneyPlayers.append(p) ; 
	
	moneyPlayers = allocateMoney(moneyPlayers, total, dist) ; 

	players = moneyPlayers + nonMoneyPlayers ;
	players = sorted(players, key=lambda p: p.name) ; 
	players = sorted(players, key=lambda p: p.total()) ; 
	
	header = padWord("Player Name", 21) ; 
	header += padWord("Place", 10) ;
	for i in range(1, 5):
		header += padWord(("RD" + str(i)), 5) ;
	header += padWord("TOTAL", 10) ; 
	header += padWord("Money Won", 9) ;
	print(header) ; 
	print("-"*71) ;
	for p in players:
		print(p) ;

	return ; 

def main():
	n = int(input()) ; 
	for i in range(0, n):
		if i > 0:
			print() ; # empty line to separate the cases
		work() ; 

if __name__ == "__main__":
	main() ; 
