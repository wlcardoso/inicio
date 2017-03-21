print("Qual o seu sexo?")
sexo = input("Digite 'M' para masculino e 'F' para feminino: ")

if sexo == 'M':
	altura = (float(input("Qual sua altura? ")))
	pesoIdeal = (72.7 * altura) - 58 
elif sexo == 'F':
	altura = (float(input("Qual sua altura? ")))
	pesoIdeal = (62.1 * altura) - 44.7
else:
	print("Digite 'M' para masculino ou 'F' para feminino")

print ("Seu peso ideal é", pesoIdeal)
