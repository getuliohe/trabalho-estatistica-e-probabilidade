import math
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

pi = math.pi

def distribuicaoNormal(x, media=10, desvioPadrao=1):
    return (1 / (desvioPadrao * math.sqrt(2 * pi))) * np.exp(-0.5 * ((x - media) / desvioPadrao) ** 2)

desvioPadrao = 1
media = 10

intervaloInferior = float(input("Digite o limite inferior do intervalo: "))
intervaloSuperior = float(input("Digite o limite superior do intervalo: "))

probabilidade = integrate.quad(distribuicaoNormal, intervaloInferior, intervaloSuperior, args=(media, desvioPadrao))[0]

print(f'Probabilidade no intervalo [{intervaloInferior}, {intervaloSuperior}]: {probabilidade}')


x = np.linspace(5, 15, 1000)
y = distribuicaoNormal(x, media, desvioPadrao)

plt.plot(x, y, label='Distribuição Normal')

x_fill = np.linspace(intervaloInferior, intervaloSuperior, 1000)
y_fill = distribuicaoNormal(x_fill, media, desvioPadrao)
plt.fill_between(x_fill, y_fill, alpha=0.5, label=f'Área do intervalo [{intervaloInferior}, {intervaloSuperior}]')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()