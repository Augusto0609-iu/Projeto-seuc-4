from processamentos import ajuste_termico, classificacao_estabilidade

qtde_leituras = 0
soma_leituras = 0
menor_pressao = 9999
qtde_leituras_zv = 0
qtde_consec_zverm = 0


qtde_total_leituras = int(
    input("Digite a quantidade total de leituras realizadas: "))

"""
while qtde_consec_zverm < 2:
    for i in range(1, qtde_total_leituras+1):
        pressao = int(input("Digite a pressão: "))
        pressao_ajustada = ajuste_termico(pressao)
        zona_pressao = classificacao_estabilidade(pressao_ajustada)

        if zona_pressao == 4:
            qtde_consec_zverm += 1
        else:
            qtde_consec_zverm == 0
        
"""

while qtde_consec_zverm != 2:
    if qtde_leituras != qtde_total_leituras:
        pressao = int(input("Digite a pressão: "))
        pressao_ajustada = ajuste_termico(pressao)
        zona_pressao = classificacao_estabilidade(pressao_ajustada)

        if zona_pressao == 4:
            qtde_consec_zverm += 1
        else:
            qtde_leituras += 1
            qtde_consec_zverm == 0
            soma_leituras += pressao
            if pressao < menor_pressao:
                menor_pressao = pressao
            if zona_pressao == 2:
                qtde_leituras_zv += 1

    print()

print('Travou')
