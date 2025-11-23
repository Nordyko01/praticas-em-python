def derivada(f, t, h):
    return (f(t + h) -f (t))/h

#função posição
f = lambda t: t**3 - 6*t**2 + 9*t

# Tempo e incremento
t= 2
#Um valor de nossa escolha
h = 3


#Calcular a velocidade
velocidade = derivada(f, t, h)
print(f"t={t}s é {velocidade: .2f}m/s")