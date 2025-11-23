import winsound, time

t = int(input("Escreva o segundo: "))
time.sleep(t)

for i in range(3):
    winsound.Beep(1000, 300)
print("Final do Alarme!")