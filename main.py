from processamentos import ajuste_termico, classificacao_estabilidade
import colorama

qtde_leituras = 0
soma_pressao_ajustada = 0
menor_pressao = 9999
qtde_leituras_zverde = 0
qtde_consec_zverm = 0
pressao_digitada = False

print("\n")
print("========== REFINARIA DELTA 9 ==========")
print("*** Bem vindo ao SEUC-4 ***")

qtde_total_leituras = int(
    input("\nPara começar, digite a quantidade total de leituras realizadas: "))

while qtde_consec_zverm < 2 and qtde_leituras < qtde_total_leituras:

    pressao = int(input("Digite a pressão: "))

    while pressao_digitada == False:
        print(f"A pressão {pressao} UCPs digitada está correta?")
        confirmacao = int(input("Digite 1 para SIM ou 2 para NÃO: "))
        while confirmacao != 1 and confirmacao != 2:
            confirmacao = input(
                "Valor inválido! Digite 1 para SIM ou 2 para NÃO: ")
        if confirmacao == 2:
            pressao_digitada = False
            pressao = int(input("Digite a pressão: "))
        else:
            pressao_digitada = True

    pressao_ajustada = ajuste_termico(pressao)
    nivel_estabilidade = classificacao_estabilidade(pressao_ajustada)

    qtde_leituras += 1
    soma_pressao_ajustada += pressao_ajustada

    if pressao < menor_pressao:
        menor_pressao = pressao

    if nivel_estabilidade == 2:
        qtde_leituras_zverde += 1

    if nivel_estabilidade == 4:
        qtde_consec_zverm += 1
        if qtde_consec_zverm == 2:
            perc_leituras = (qtde_leituras/qtde_total_leituras)*100
            print(f"\nTravamento necessário. Duas leituras consecutivas na Zona Vermelha registradas"
                  f"\nPercentual de leituras realizadas: {perc_leituras:.0f}%")
    else:
        qtde_consec_zverm = 0

    pressao_digitada = False

media = soma_pressao_ajustada / qtde_leituras
perc_zverde = (qtde_leituras_zverde / qtde_leituras) * 100

print("\n")
print("\n========== INDICADORES DE REGISTRO ==========")
print(f"\nMédia de pressão ajustada: {media:.0f} UPCs ")
print(f"Menor pressão registrada: {menor_pressao} UPCs ")
print(f"Percentual de leituras na Zona verde: {perc_zverde:.0f}%")
print("\n")


# ajustar protecao na validacao da pressao (sim ou nao)
# ajustar formatacoes de saída (centralizacao, cores, símbolos (%) por exemplo)
# podemos usar bibliotecas de cor para destacar atencao para o usuário???
# registra qtde de leituras por turno e qtde de travamentos ocorridos -monitorar
