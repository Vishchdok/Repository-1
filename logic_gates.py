#Build logic gates in Python

# Elementary Logic Gates
# 1 or 2 Input Gates with 1 Output
"""def ANDgate(a,b):
	if a==1 and b==1:
		return 1
	else:
		return 0
		
def NOTgate(a):
	if a==1:
		return 0
	else:
		return 1

def ORgate(a,b):
	if a==b and a==0:
		return 0
	else:
		return 1"""

def NANDgate(a,b):
	if a==b and a==1:
		return 0
	else:
		return 1

def XORgate(a,b):
	if a==b:
		return 0
	else:
		return 1
