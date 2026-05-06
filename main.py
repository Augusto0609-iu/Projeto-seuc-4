from processamentos import ajuste_termico, classificacao_estabilidade, validador_input

qtde_leituras = 0
soma_pressao_ajustada = 0
menor_pressao = 9999
qtde_leituras_zverde = 0
qtde_consec_zverm = 0


print("\n" + "="*45)
print(f"{'REFINARIA DELTA 9':^45}")
print(f"{'Bem vindo ao SEUC-4!':^45}")
print("="*45)

qtde_total_leituras = input(
    "\nPara começar, digite a quantidade total de leituras realizadas: ")

# validação da qtde total de leituras
while not qtde_total_leituras.isdigit():
    print("\nValor inválido! Digite apenas números, positivos ou maiores que zero.")
    qtde_total_leituras = input(
        "\nDigite novamente a quantidade total de leituras realizadas: ")

qtde_total_leituras = int(qtde_total_leituras)


while qtde_consec_zverm < 2 and qtde_leituras < qtde_total_leituras:

    # validacao da pressao
    pressao = input("\nDigite a pressão: ")
    while not pressao.isdigit():
        pressao = input("\nValor inválido! Digite novamente a pressão: ")

    pressao = int(pressao)

    # validacao da confirmacao
    pressao_confirmada = False
    while pressao_confirmada == False:
        print(f"\nA pressão {pressao} UCPs digitada está correta?")
        confirmacao = input("\nDigite 1 para SIM ou 2 para NÃO: ")

        while confirmacao != "1" and confirmacao != "2":
            confirmacao = input(
                "Valor inválido! Digite 1 para SIM ou 2 para NÃO: ")

        if confirmacao == "2":
            pressao = input("Digite novamente a pressão: ")
            while not pressao.isdigit():
                pressao = input(
                    "\nValor inválido! Digite novamente a pressão: ")

        else:
            pressao_confirmada = True

    pressao = int(pressao)

    pressao_ajustada = ajuste_termico(pressao)
    nivel_estabilidade = classificacao_estabilidade(pressao_ajustada)

    qtde_leituras += 1
    soma_pressao_ajustada += pressao_ajustada

    if pressao < menor_pressao:  # menor pressao, ou menor pressao registrada?
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


media = soma_pressao_ajustada / qtde_leituras
perc_zverde = (qtde_leituras_zverde / qtde_leituras) * 100

print("\n" + "="*45)
print(f"{'INDICADORES DE REGISTRO':^45}")  # O ^ centraliza em 45 espaços
print("="*45)
print(f" Média de pressão ajustada:    {media:>6.0f} UPCs")
print(f" Menor pressão registrada:     {menor_pressao:>6} UPCs")
print(f" Percentual na Zona Verde:      {perc_zverde:>5.0f}%")
print("="*45)


# ajustar formatacoes de saída (centralizacao, cores, símbolos (%) por exemplo)
# podemos usar bibliotecas de cor para destacar atencao para o usuário???
# registra qtde de leituras por turno e qtde de travamentos ocorridos -monitorar
