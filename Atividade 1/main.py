import math
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

pi = math.pi

def distribuicaoNormal(x, media = 10, desvioPadrao = 1):
    return (1/(desvioPadrao*math.sqrt(2*pi)))* (np.exp((-(1/2))*((x - media)/desvioPadrao))**2)

desvioPadrao = 1
media = 10

intervaloInferior = float(input("Digite o limite inferior do intervalo: "))
intervaloSuperior = float(input("Digite o limite superior do intervalo: "))

probabilidade= integrate.quad(distribuicaoNormal,intervaloInferior, intervaloSuperior)[0]

print(probabilidade)

x = np.linspace(5, 15, 1000)
y = distribuicaoNormal(x)

plt.plot(x, y, label='Distribuição Normal')

# Destacando a área sob a curva no intervalo [a, b]
x_fill = np.linspace(intervaloInferior, intervaloSuperior, 1000)
y_fill = distribuicaoNormal(x_fill)
plt.fill_between(x_fill, y_fill, alpha=0.5, label=f'Área do intervalo [{intervaloInferior}, {intervaloSuperior}]')

plt.title('Distribuição Normal com Média 10 e Desvio Padrão 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()