#!/usr/bin/python3 
import os 
import sys 
from he import ha

if sys.argv[1] == '-t' : 
	text1=sys.argv[2]
	if sys. argv[3]=='-ty' : 
	 text2=sys.argv[4] 
	 ali=ha()
	 print('**************'+'*'*len(ali.T(text1,text2)))
	 print('*your hash <'+ali.T(text1,text2)+'>*')
	 print('**************'+'*'*len(ali.T(text1,text2)))
	
	else : 
		print ('**************************************************')
		print ('*[*]you made a mistake for help enter ::: <-h>!!!*') 
		print ('**************************************************')
elif sys.argv[1] == '-d' : 
	t1=sys.argv[2] 
	if sys.argv[3] == '-w' : 
		t3=sys.argv[4]
		if sys.argv[5]== '-ty' : 
			t2=sys.argv[6]

			
			a3=ha()
			R=a3.RR(t3)
			i=1
			ir=R[0].rstrip("\n")

			while (t1 != a3.T(ir,t2)):
				if i == len(R)+1 :
					print('your hash not finde ') 
					break 
	
				ir=R[i].rstrip("\n")
				i+=1
			if i != len(R)+1:
				print ('************************'+'*'*len(R[i-1].rstrip('\n')))
				print ('* your hashe is //<<'+R[i-1].rstrip('\n')+'>> *')
				print ('************************'+'*'*len(R[i-1].rstrip('\n')))


		else : 
			print ('***************************************************')
			print ('*[*]you made a mistake for help enter ::: <-h>!!! *') 
			print ('***************************************************')
	else : 
		print ('***************************************************')
		print ( '*[*]you made a mistake for help enter ::: <-h>!!!*') 
		print ('***************************************************')
elif sys.argv[1]=='-h' : 
	print('*****************')
	print('*─────▄───▄     *')
	print('*─▄█▄─█▀█▀█─▄█▄ *')
	print('*▀▀████▄█▄████▀▀*')
	print('*─────▀█▀█▀     *')
	print('*****************')
	print('▒█░▒█ █▀▀█ █▀▀ █░░█ ▄▀▀▄===█▀▀█ █▀▀█ ▄█░ ')
	print('▒█▀▀█ █▄▄█ ▀▀█ █▀▀█ ▄▀▀▄===█▄▀█ █▄▀█ ░█░ ')
	print('▒█░▒█ ▀░░▀ ▀▀▀ ▀░░▀ ▀▄▄▀===█▄▄█ █▄▄█ ▄█▄ ')
	print('***************************************************************')
	print ('[*]hello your apparently you do not know to use the Hash8_001 \n[*]in the case of encryption// \n//(*)-t::the text you want to encrypt\n//(*)-ty::encryption type :example(md5,sha1,sha224,sha256,sha384,sha512)\n[*]in the case of decryption//\n//(*)-d::the text you want to encrypt\n//(*)-w::the path of wardlist(dictionary)\n//(*)-ty::encryption type :example(md5,sha1,sha224,sha256,sha384,sha512)') 
	print ('[*]example:: ')
	print ('//(*)example encryption :: < -t blacko -ty md5 >')
	print ('//(*)example dncryption :: < -d blacko -w /root/world.txt -ty md5 >')
else : 
	print('*****************')
	print('*─────▄───▄     *')
	print('*─▄█▄─█▀█▀█─▄█▄ *')
	print('*▀▀████▄█▄████▀▀*')
	print('*─────▀█▀█▀     *')
	print('*****************')
	print('▒█░▒█ █▀▀█ █▀▀ █░░█ ▄▀▀▄===█▀▀█ █▀▀█ ▄█░ ')
	print('▒█▀▀█ █▄▄█ ▀▀█ █▀▀█ ▄▀▀▄===█▄▀█ █▄▀█ ░█░ ')
	print('▒█░▒█ ▀░░▀ ▀▀▀ ▀░░▀ ▀▄▄▀===█▄▄█ █▄▄█ ▄█▄ ')
	print('***************************************************************')
	print ('[*]hello your apparently you do not know to use the Hash8_001 \n[*]in the case of encryption// \n//(*)-t::the text you want to encrypt\n//(*)-ty::encryption type :example(md5,sha1,sha224,sha256,sha384,sha512)\n[*]in the case of decryption//\n//(*)-d::the text you want to encrypt\n//(*)-w::the path of wardlist(dictionary)\n//(*)-ty::encryption type :example(md5,sha1,sha224,sha256,sha384,sha512)') 
	print ('[*]example:: ')
	print ('//(*)example encryption :: < -t blacko -ty md5 >')
	print ('//(*)example dncryption :: < -d blacko -w /root/world.txt -ty md5 >')
	

