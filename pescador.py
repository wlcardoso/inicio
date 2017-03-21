## Este programa calcula multa a ser paga por excesso no peso do peixe pescado ##

P = float(input("Qual o peso do peixe pescado? "))

k = 50
multi = 4

if (P > k):
	E = (P - k)
	M = E * multi
	print ("A multa a ser paga é de R$", M)
else:
	E = 0
	M = 0
	P = 0
	print ("E",E,"M",M,"P",P)
	

