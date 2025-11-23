import winsound, time

t = int(input("Escreva o segundo: "))
time.sleep(t)
menssagem = "🎉🎊Feliz aniversário amor!🎉🎊"
edge = "✨" * (len(menssagem))

for i in range(3):
    winsound.Beep(1000, 300)
print(edge)
print(menssagem)
print(edge)
print("Que dias como esse se repitão mais vezes!")