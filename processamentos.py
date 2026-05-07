# Ajuste térmico

def ajuste_termico(n):
    if n > 150:
        n = n*1.08
    else:
        n = n*0.96
    return n


def classificacao_estabilidade(n):
    if n < 120:
        nivel_n = 1
        print("Pressão muito baixa. Risco de cristalização")

    elif n <= 180:
        nivel_n = 2
        print("Zona Verde - Estável")

    elif n <= 250:
        nivel_n = 3
        print("Zona Amarela - Oscilação")

    else:
        nivel_n = 4
        print("Zona vermelha - Crítica")

    return nivel_n

def tendencias(atual,pressao_anterior,pressao_ante_anterior):
    if atual > pressao_anterior > pressao_ante_anterior:   
        print("ALERTA! PRESSÃO EM ASCENSÃO...")
    elif atual < pressao_anterior < pressao_ante_anterior:
        print("ALERTA! PRESSÃO EM DECRÉSCIMO...")
