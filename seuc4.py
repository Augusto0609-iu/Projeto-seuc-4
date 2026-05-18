
from colorama import init, Fore, Style


def ajuste_termico(n):
    if n > 150:
        n = n*1.08
    else:
        n = n*0.96
    return n


def classificacao_estabilidade(n):
    if n < 120:
        nivel_n = 1
        print(Fore.CYAN + Style.BRIGHT +
              "\n❄️ Pressão muito baixa. Risco de cristalização")

    elif n <= 180:
        nivel_n = 2
        print(Fore.GREEN + "\n✅ Zona Verde - Estável")

    elif n <= 250:
        nivel_n = 3
        print(Fore.YELLOW + "\n⚠️ Zona Amarela - Oscilação")

    else:
        nivel_n = 4
        print(Fore.RED + Style.BRIGHT + "\n✘ Zona Vermelha - Crítica")

    return nivel_n


sair = 0

while sair == 0:
    init(autoreset=True)

    # variáveis para atender requisitios do sistema
    qtde_leituras = 0
    soma_pressao_ajustada = 0
    menor_pressao = 9999
    qtde_leituras_zverde = 0
    qtde_consec_zverm = 0

    # variáveis para funcionalidades adicionais
    qtde_leituras_zamarela = 0
    qtde_leituras_zvermelha = 0
    qtde_leituras_cristalizacao = 0
    maior_pressao = -9999

    print("\n" + "="*45)
    print(Fore.CYAN + Style.BRIGHT + f"{'REFINARIA DELTA 9':^45}")
    print(Fore.CYAN + f"{'Bem vindo ao SEUC-4!':^45}")
    print("="*45)

    qtde_total_leituras = input(
        "\nSEUC-4 ->>> Para começar, digite a quantidade total de leituras realizadas \n-> Operador: ")

    # validação da qtde total de leituras
    while not qtde_total_leituras.isdigit():
        print(Fore.YELLOW + "\nSEUC-4 ->>> Valor inválido! Digite apenas números, positivos ou maiores que zero.")
        qtde_total_leituras = input(
            "\nSEUC-4 ->>> Digite novamente a quantidade total de leituras realizadas \n-> Operador: ")

    qtde_total_leituras = int(qtde_total_leituras)

    if qtde_total_leituras > 0:  # validacao importante para não quebrar o programa por divisão por zero nos cálculos

        while qtde_consec_zverm < 2 and qtde_leituras < qtde_total_leituras:

            # validacao da pressao
            pressao = input(
                "\nSEUC-4 ->>> Digite a pressão \n-> Operador: ")
            while not pressao.isdigit():
                print(Fore.YELLOW + "\nSEUC-4 ->>>Valor inválido!")
                pressao = input(
                    "Digite novamente a pressão \n-> Operador: ")

            pressao = int(pressao)

            # validacao da confirmacao
            pressao_confirmada = False
            while pressao_confirmada == False:
                print(
                    f"\nSEUC-4 ->>> A pressão {pressao} UCPs digitada está correta?")
                confirmacao = input(
                    "Digite 1 para SIM ou 2 para NÃO \n-> Operador: ")

                while confirmacao != "1" and confirmacao != "2":
                    print(Fore.YELLOW + "SEUC-4 ->>> Valor inválido!")
                    confirmacao = input(
                        "Digite 1 para SIM ou 2 para NÃO \n-> Operador: ")

                if confirmacao == "2":
                    pressao = input(
                        "SEUC-4 ->>> Digite novamente a pressão: \n-> Operador: ")
                    while not pressao.isdigit():
                        print(Fore.YELLOW + "\nSEUC-4 ->>> Valor inválido!")
                        pressao = input(
                            "Digite novamente a pressão: \n-> Operador: ")
                else:
                    pressao_confirmada = True

            pressao = int(pressao)

            pressao_ajustada = ajuste_termico(pressao)
            nivel_estabilidade = classificacao_estabilidade(pressao_ajustada)

            qtde_leituras += 1
            soma_pressao_ajustada += pressao_ajustada

            if pressao < menor_pressao:
                menor_pressao = pressao

            if nivel_estabilidade == 2:
                qtde_leituras_zverde += 1

            if nivel_estabilidade == 4:
                qtde_leituras_zvermelha += 1
                qtde_consec_zverm += 1
                print(Fore.RED + Style.BRIGHT +
                      "\n!! Atenção para risco de rompimento do duto !!")

                if qtde_consec_zverm == 2:
                    perc_leituras = (qtde_leituras/qtde_total_leituras)*100
                    print(Fore.RED + Style.BRIGHT + "\n" + "█"*45)
                    print(Fore.RED + Style.BRIGHT +
                          f"{'⛔  TRAVAMENTO NECESSÁRIO  ⛔':^45}")
                    print(Fore.RED + Style.BRIGHT +
                          f"{'2 leituras consecutivas na Zona Vermelha':^45}")
                    print(Fore.RED + Style.BRIGHT +
                          f"{'Percentual de leituras realizadas: ' + str(int(perc_leituras)) + '%':^45}")
                    print(Fore.RED + Style.BRIGHT + "█"*45)
            else:
                qtde_consec_zverm = 0

            # ------- cálculos adicionais do programa -------

            # registros para 'Relatório Completo'
            if nivel_estabilidade == 1:
                qtde_leituras_cristalizacao += 1
            if nivel_estabilidade == 3:
                qtde_leituras_zamarela += 1
            if pressao > maior_pressao:
                maior_pressao = pressao

        media = soma_pressao_ajustada / qtde_leituras
        perc_zverde = (qtde_leituras_zverde / qtde_leituras) * 100

        print("\n" + "="*45)
        print(Fore.CYAN + Style.BRIGHT + f"{'INDICADORES DE REGISTRO':^45}")
        print("="*45)
        print(f" Média de pressão ajustada:    {media:>6.0f} UPCs")
        print(f" Menor pressão registrada:     {menor_pressao:>6} UPCs")
        print(f" Percentual na Zona Verde:      {perc_zverde:>5.0f}%")
        print("="*45)

    else:
        print(Fore.RED + Style.BRIGHT + f"\nNÃO HÁ LEITURAS A SEREM PROCESSADAS!")

    opcao_valida = False

    while opcao_valida == False:
        print(Fore.CYAN + Style.BRIGHT +
              f"\n========= O que deseja fazer agora? =========")
        print(
            "\nOpção 1 - Voltar ao SEUC-4"
            "\nOpção 2 - Ver relatório completo"
            "\nOpção 3 - Sair do SEUC-4")

        definir_sistema = input("Escolha uma opção: ")
        while not definir_sistema.isdigit():
            print(Fore.YELLOW + "\nSEUC-4 ->>> Valor inválido!")
            definir_sistema = input(
                "Digite novamente uma opção entre 1 e 3 \n-> Operador: ")

        while not "0" < definir_sistema < "4":
            print(Fore.YELLOW + "\nSEUC-4 ->>> Valor inválido!")
            definir_sistema = input(
                "Digite novamente uma opção entre 1 e 3 \n-> Operador: ")

        opcao_valida = True

        match definir_sistema:
            case "1":
                print(Fore.BLACK + Style.BRIGHT + f"\nVoltando ao sistema...")
            case "2":
                print("\n" + "="*60)
                print(Fore.CYAN + Style.BRIGHT + f"{'RELATÓRIO COMPLETO':^60}")
                print("="*60)
                print(
                    f"{'Quantidade total de leituras concluídas:':<45} {qtde_leituras:>8}")
                print(
                    f"{'Quantidade total de leituras a inserir:':<45} {qtde_total_leituras:>8}")
                print(
                    f"{'Percentual de conclusão:':<45} {(qtde_leituras/qtde_total_leituras)*100:>8.0f}%")
                print(
                    f"\n{'Menor pressão registrada:':<45} {menor_pressao:>8} UPCs")
                print(
                    f"{'Maior pressão registrada:':<45} {maior_pressao:>8} UPCs")
                print(f"{'Média de pressão ajustada:':<45} {media:>8.0f} UPCs")
                print(Fore.CYAN + Style.BRIGHT +
                      f"\n{'Total de leituras com risco de Cristalização:':>45} {qtde_leituras_cristalizacao:>8}")
                print(Fore.CYAN + Style.BRIGHT +
                      f"{'Percentual com risco de Cristalização:':<45} {(qtde_leituras_cristalizacao/qtde_leituras)*100:>8.0f}%")
                print(Fore.GREEN + Style.BRIGHT +
                      f"\n{'Total de leituras na Zona Verde:':<45} {qtde_leituras_zverde:>8}")
                print(Fore.GREEN + Style.BRIGHT +
                      f"{'Percentual na Zona Verde:':<45} {perc_zverde:>8.0f}%")
                print(Fore.YELLOW + Style.BRIGHT +
                      f"\n{'Total de leituras na Zona Amarela:':<45} {qtde_leituras_zamarela:>8}")
                print(Fore.YELLOW + Style.BRIGHT +
                      f"{'Percentual na Zona Amarela:':<45} {(qtde_leituras_zamarela/qtde_leituras)*100:>8.0f}% ")
                print(Fore.RED + Style.BRIGHT +
                      f"\n{'Total de leituras na Zona Vermelha:':<45} {qtde_leituras_zvermelha:>8}")
                print(Fore.RED + Style.BRIGHT +
                      f"{'Percentual na Zona Vermelha:':<45} {(qtde_leituras_zvermelha/qtde_leituras)*100:>8.0f}% ")
                print("="*60)

                opcao_valida = False

            case "3":
                print(Fore.RED + Style.BRIGHT +
                      f"\nEncerrando sistema SEUC-4!")
                opcao_valida = True
                sair = 3
