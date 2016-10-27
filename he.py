#!/usr/bin/python3 

import hashlib 
import os 

class ha(object):
	
	
	def T(se,Q,T_P) :
			Q=Q.encode()
			HH=hashlib.new(T_P)
			HH.update(Q)
			return HH.hexdigest()
	
	def RR(se,t): 
		OP=open(t,'r')
		return OP.readlines()
		
	
