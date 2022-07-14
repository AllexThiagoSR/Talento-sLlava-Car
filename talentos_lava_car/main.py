import ast
from funcionalidades import datas, dia_conta, veiculo
from ler_valores import leiaint, leiafloat
from informacoes_arquivos.entradas import mostra_relatorio, arqui_form, mes_atual, arqui_mes, arquivo_principal
from informacoes_arquivos.saidas import arquivo_saida, mostra_saida
from informacoes_arquivos.lucro import lucro

data = datas()
date = data.split()
veiculos = []
with open('lavagens.txt', 'rt+') as file:
    lavagens = ast.literal_eval(file.read())
with open('saidas.txt', 'rt+') as file:
    saidas = ast.literal_eval(file.read())
while True:
    print('=' * 100)
    print('Opções:\n1 - Fechar um dia de trabalho\n2 - Mostrar o relatório\n'
          '3 - Mostrar relatório mês atual\n4 - Saídas\n5 - Lucro mensal\n6 - Sair')
    op = leiaint('O que deseja fazer? ')
    if op == 1:
        conta = []
        while True:
            print('-' * 50)
            tipo_vei = input('Qual o tipo de véiculo lavado: ').strip().capitalize()
            while True:
                try:
                    quant = int(input('Quantos desse tipo de veículo foram lavados? ').strip())
                    break
                except ValueError:
                    print('Apenas valores numéricos.')
            veiculos.append(veiculo(tipo_vei, quant))
            print('-' * 42)
            for i in range(0, quant, 1):
                conta.append(leiafloat(f'Qual o preço do {i + 1}º veículo lavado: R$ '))
            cont = 'a'
            while cont not in 'NnSs':
                cont = input('Lavou outro tipo de veículo? [s/n] ').strip().upper()[0]
            if cont in 'Nn':
                conta = dia_conta(val=conta, veiq=veiculos)
                conta.insert(0, data)
                lavagens[date[2]].append(conta[:])
                arqui_form(lavagens)
                arqui_mes(mes=date[2], rel=lavagens)
                arquivo_principal(lavagens)
                break
    elif op == 2:
        mostra_relatorio(lavagens)
        arquivo_principal(lavagens)
    elif op == 3:
        mes_atual(mes=date[2], rel=lavagens)
        arquivo_principal(lavagens)
        pass
    elif op == 4:
        while True:
            print('-' * 50)
            print('Saídas')
            print('-' * 50)
            print('1 - Funcionários\n2 - Água/Energia\n3 - Materiais\n4 - Mostra saídas\n5 - Voltar')
            op = leiaint('Qual o tipo de saída? ')
            print('=' * 50)
            if op == 1:
                while True:
                    nome = input('Nome do funcionário: ').strip().capitalize()
                    valor = leiafloat('Valor da saída: R$ ')
                    print('-' * 50)
                    if nome not in saidas[date[2]]['Funcionarios'].keys():
                        saidas[date[2]]['Funcionarios'][nome] = valor
                    else:
                        saidas[date[2]]['Funcionarios'][nome] += valor
                    more = 'a'
                    while more not in 'SsNn':
                        more = input('Mais saídas de funcionários? [s/n] ').strip().upper()[0]
                    print('-' * 50)
                    if more == 'N':
                        break
                arquivo_saida(saidas)
            elif op == 2:
                valor = leiafloat('Valor pago de água: R$ ')
                valor += leiafloat('Valor pago de energia: R$ ')
                saidas[date[2]]['Agua/Energia'] += valor
                arquivo_saida(saidas)
            elif op == 3:
                while True:
                    valor = leiafloat('Valor do material: R$ ')
                    saidas[date[2]]['Materiais'] += valor
                    more = 'a'
                    while more not in 'NnSs':
                        more = input('Mais gastos com material? [s/n] ').strip().upper()[0]
                    if more == 'N':
                        break
                arquivo_saida(saidas)
            elif op == 4:
                mostra_saida(saidas)
            elif op == 5:
                print('Voltando')
                break
    elif op == 5:
        lucro(lavagens, saidas)
    elif op == 6:
        print('-' * 50)
        print('Saindo')
        break
    else:
        print('Não há essa opção')

arquivo_principal(lavagens)
arquivo_saida(saidas)
