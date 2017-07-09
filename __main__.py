#Fabricio Junior
#Inicio: 08/07/2017
#Ultima Atualizacao: 09/07/2017

import os

os.system("color a")
os.system("cls")

def transformar(a, b, c, d):
	if(a == 1):
		at = True
	else:
		at = False

	if(b == 1):
		bt = True
	else:
		bt = False

	if(c == 1):
		ct = True
	else:
		ct = False

	if(d == 1):
		dt = True
	else:
		dt = False

	return(at, bt, ct, dt)


def desenhar(s1, s2, s3, s4, s5, s6, s7):
	if(s4 == True):
		print(" -- ")
	else:
		print("   ")

	if(s5 == True and s3 == True):
		print("|  |")
	elif(s5 == True and s3 == False):
		print("|")
	elif(s5 == False and s3 == True):
		print("   |")
	else:
		print(" ")

	if(s7 == True):
		print(" -- ")
	else:
		print("   ")

	if(s6 == True and s2 == True):
		print("|  |")
	elif(s6 == True and s2 == False):
		print("|")
	elif(s6 == False and s2 == True):
		print("   |")
	else:
		print(" ")

	if(s1 == True):
		print(" -- ")
	else:
		print("   ")


















print("="*50)

while(True):
	entrada = raw_input("DCBA: ")

	d = int(entrada[0])
	c = int(entrada[1])
	b = int(entrada[2])
	a = int(entrada[3])

	a, b, c, d = transformar(a, b, c, d)

	print("="*50)

	s1 = ((not d) and (((not a) and (b or ((not b) and (not c)))) or (a and ((b and not c) or (not b and c)))) or ((not a) and (not b) and (not c) and (d)))
	s2 = (a or (not b) or c or d)
	s3 = ((a and (b or (not b and not c))) or (not a and ((not b and not c) or ((b and not c) or (not b and c))))) or (not b and not c and not d)
	s4 = ((a and not d) and (c or (b and not c))) or ((not c) and ((not a and not d) or (not b and d)))
	s5 = ((not a and not b) and (not c or (c and not d))) or ((a and not b) and ((c and not d) or (not c and d))) or (not a and b and c and not d)
	s6 = (not a) and (not c and (not b or (b and not d)) or (b and c and not d))
	s7 = (not d and ((not a and (c or (b and not d))) or a and ((b and not c) or (not b and c)))) or (not b and not c and d)

	print(s1)
	print(s2)
	print(s3)
	print(s4)
	print(s5)
	print(s6)
	print(s7)

	print("="*50 + "\n")
	desenhar(s1, s2, s3, s4, s5, s6, s7)
	print("\n" + "="*50)








