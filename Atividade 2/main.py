from ConexaoBDD import ConexaoBDD
from Analise import Analise
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dados = ConexaoBDD("localhost", "root", "ADttgh2017$", "censo 2022")

resultado = dados.procura_banco_dados(["ï»¿Ano da pesquisa","PopulaÃ§Ã£o(pessoas)"],"crescimento populacional - brasil")

populacao = []
anos = []
anosLinear = []
listaPaths = []

for ano, pop in resultado:
    populacao.append(pop)
    anos.append(ano)
    anosLinear.append([ano])

analise = Analise(populacao,anosLinear,populacao)

listaPaths.append(analise.graficoRegressaoLinear(anosLinear, populacao))

listaPaths.append(Analise.gerarGraficoBoxPLot(populacao))

analise.gerarDocumento(listaPaths)
