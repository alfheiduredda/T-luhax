import numpy as np

def Romberg(T):
	l = len(T)
	for i in xrange(1,l) : 
		for k in xrange(l-1,i-1,-1):
			T[k] = ((4**i)*(T[k-1])-T[k]) / (4**i - 1)
	return T[l-1]


print "virkar thetta?"
fall = lambda z: 1/z
a = 1
b = 2
n = 3
print
T = [0 for i in xrange(n)]
print(str(T))
for i in xrange(n):
	temp = fall(a) + fall(b)
	intervals = [(a + j*(b-a)/(2**i)) for j in xrange(1,2**i)]
	for j in intervals:
		temp += 2 * fall(float(j)/(2**i))
	T[i] = temp / 2**(i+1)
print str(T)
I = Romberg(T)
print str(I)

print "virkar thetta nuna?"