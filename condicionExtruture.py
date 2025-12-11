###idade = int(input("Escreva sua idade: "))

#if idade >= 18:
    #print("Você é de maior")
#elif idade == 17:
    #print("Só falta um ano para se tornar de maior")
#else:
    #print("você ainda é de menor!")

p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))

media = p1 + p2 
mediaF = media / 2
print(mediaF)
if mediaF >= 14:
    print("você não vai para o exame!")
elif mediaF == 10:
    print("Você vai para o exame!")
else:
    print("Você corre o risco de ir ao recurso!")


