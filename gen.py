#!/usr/bin/python

import test9


f = open('liczby8.txt', 'w')


for i in range(10000):
	 a=test9.srd()
	 
	 z=str(a)
	 f.write(z)
	 f.write('\n')
	 
	 

f.close()