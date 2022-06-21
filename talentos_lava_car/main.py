import ast
from funcionalidades import datas, dia_conta, veiculo
from ler_valores import leiaint
from interface import mostra, arqui_form, mes_atual, arqui_mes, arquivo_principal

data = datas()
date = data.split()
conta = []
veiculos = []
with open('lavagens.txt', 'rt+') as file:
    lavagens = ast.literal_eval(file.read())
while True:
    print('=' * 100)
    print('Opções:\n1 - Fechar um dia de trabalho\n2 - Mostrar o relatório\n'
          '3 - Mostrar relatório mês atual\n4 - Sair')
    op = leiaint('O que deseja fazer? ')
    if op == 1:
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
                while True:
                    try:
                        conta.append(float(input(f'Qual o preço do {i + 1}º veículo lavado: R$ ').strip()))
                        break
                    except ValueError:
                        print('Apenas valores numéricos.')
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
        mostra(lavagens)
        arquivo_principal(lavagens)
    elif op == 3:
        mes_atual(mes=date[2], rel=lavagens)
        arquivo_principal(lavagens)
        pass
    elif op == 4:
        print('Saindo')
        break
    else:
        print('Não há essa opção')

arquivo_principal(lavagens)
