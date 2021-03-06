from datetime import datetime, date
from math import ceil


cnpj = str('00.125.123/0001-12')
nome_estacionamento = str('Carangola Parking')
endereço = str('Rua Presidente Kennedy, 333 - Centro - Carangola MG')
preco_hora = 3.5
total_vagas = 5
total_vagas_especiais = 3
vagas_disponiveis = total_vagas
vagas_ocupadas = 0
vagas_especiais_disponiveis = total_vagas_especiais
vagas_especiais_ocupadas = 0
quant_entradas = 0
quant_saidas = 0
soma_tempos = 0
vaga = 1
count = 0
faturamento = 0
saida_estacionamento = list()
entradas_estacionamento = list()
entrada_veiculos = dict()
saida_veiculos = dict()

while True:

    print()
    print('##### SISTEMA DE ESTACIONAMENTO #####')
    print()

    try:
        opcao = int(input('[1] - Entrada de veículo\n[2] - Saída de veículo\n[3] - Informações estacionamento\n[4] - Sair do sistema\nEscolha uma opção: '))  
    except ValueError:
        print()
        print(ValueError)
        continue

    print()          
    
    if int(opcao) == 1:

        if vagas_ocupadas == total_vagas:
            print('Estacionamento não tem vagas disponíveis.')
            continue
        else:

            try:
               entrada_veiculos['Vaga'] = vaga
               entrada_veiculos['Nome do motorista'] = input('Nome do motorista: ')
               entrada_veiculos['Idade'] = int(input('Idade: '))

               while True:
                 entrada_veiculos['Deficiente físico'] = input('Deficiente físico: ')

                 if entrada_veiculos['Deficiente físico'].lower() == 'sim' or entrada_veiculos['Deficiente físico'].lower() == 'não':
                    break
                 else: 
                    print('Entrada inválida! Digite [sim] ou [não].')

               entrada_veiculos['Tipo veículo'] = str(input('Tipo veículo: '))
               entrada_veiculos['Cor veículo'] = str(input('Cor veículo: '))
               entrada_veiculos['Ano veículo'] = str(input('Ano veículo: '))
               entrada_veiculos['Placa veículo'] = str(input('Placa veículo: '))
               entrada_veiculos['Horário de entrada'] = datetime.today().strftime('%H:%M')
            except ValueError:
                print()
                print(ValueError)
                continue
                            
            if vagas_ocupadas == (total_vagas - total_vagas_especiais + vagas_especiais_ocupadas) and vagas_especiais_ocupadas < total_vagas_especiais and (entrada_veiculos['Idade'] < 65 or entrada_veiculos['Deficiente físico'] == 'sim'):
                print('Total de vagas para quem não é idoso preenchidas.')
                continue
            
            vaga += 1
            vagas_disponiveis -= 1
            vagas_ocupadas += 1
            quant_entradas += 1

            print()

            if entrada_veiculos['Idade'] >= 65 and vagas_especiais_ocupadas < total_vagas_especiais:
                vagas_especiais_disponiveis -= 1 
                vagas_especiais_ocupadas += 1

            entradas_estacionamento.append(entrada_veiculos.copy())

    elif int(opcao) == 2:
        
        if vagas_ocupadas > 0:

            try:
                saida = int(input('Informe a vaga do veículo: '))
            except ValueError:
                print(ValueError)
                break
            
            saida_veiculos = entradas_estacionamento[saida - 1]
            
            saida_veiculos['Horário de saída'] = datetime.today().strftime('%H:%M')

            total_tempo = datetime.strptime(saida_veiculos['Horário de saída'], '%H:%M') - datetime.strptime(saida_veiculos['Horário de entrada'], '%H:%M')
            
            saida_veiculos['Total tempo'] = total_tempo

            quant_horas = ceil(total_tempo.total_seconds() / 3600)
            valor_pago = preco_hora * quant_horas
                        
            saida_veiculos['Valor pago'] = f'R${valor_pago:.2f}'

            saida_estacionamento.append(saida_veiculos.copy())
            
            soma_tempos += total_tempo.total_seconds() / 3600
            tempo_medio_horas = (soma_tempos // len(saida_estacionamento))
            tempo_medio_minutos = (abs(soma_tempos - abs(tempo_medio_horas))) * 60
            faturamento += valor_pago
            faturamento_medio = faturamento / len(saida_estacionamento)
            
            for i, j in saida_veiculos.items():
                # Horário sempre arredondado para cima, então se ficar 20 minutos vai pagar como 1 hora
                print(f'{i} = {j}')
            
            del(entradas_estacionamento[(saida - 1)])

            vagas_disponiveis += 1
            vagas_ocupadas -= 1
            quant_saidas += 1   

        else:
            print('Estacionamento com nenhum vaga ocupada.')

    elif int(opcao) == 3:

        print(f'Vagas disponíveis =  {vagas_disponiveis}\n'
              f'Vagas ocupadas = {vagas_ocupadas}\n'
              f'Vagas especiais disponíveis = {vagas_especiais_disponiveis}\n'
              f'Vagas especiais ocupadas = {vagas_especiais_ocupadas}\n'
              f'Quantidade de entrada de veículos = {quant_entradas}\n'
              f'Quantidade de saída de veículos = {quant_saidas}\n'
              f'Tempo médio de um veículo no estacionado = {tempo_medio_horas:.0f} horas e {tempo_medio_minutos:.0f} minutos\n'
              f'Valor médio pago por veículo no estacionado = R$ {faturamento_medio:.2f}\n'
              f'Faturamento = R$ {faturamento:.2f}\n')

    elif int(opcao) == 4:
        break

    else:
        print('Opção inválida.')
        