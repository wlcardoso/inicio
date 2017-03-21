## Este programa recebe uma idade como entrada e classifica o nadador conforme abaixo: ##

# Infantil A = 5 a 7 anos
# Infantil B = 8 a 11 anos
# Juvenil A = 12 a 13 anos
# Juvenil B = 14 a 17 anos
# Adultos = Maiores de 18 anos 

idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <=7:
	print ("Infantil A")
elif idade >= 8 and idade <= 11:
	print ("Infantil B")
elif idade == 12 or idade == 13:
	print ("Juvenil A")
elif idade >= 14 and idade <= 17:
	print ("Juvenil B")
elif idade > 17:	
	print("Maiores de 18 anos")
else:
	print("Sem categoria")

