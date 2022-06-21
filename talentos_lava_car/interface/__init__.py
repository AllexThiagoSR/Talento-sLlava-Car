def mostra(rel):
    arqui_form(rel)
    fatu_mes = 0
    for mes, dias_mes in rel.items():
        print('=' * 42)
        print(f'{mes:^42}')
        print('=' * 42)
        if len(dias_mes) > 0:
            for dia in dias_mes:
                print(dia[0])
                print('-' * 42)
                print('Veículos     Quantidade')
                print('-' * 42)
                for vei_quant in dia[1]:
                    p = vei_quant.split(';')
                    print(f'{p[0]:<8}     {p[1]:<10}')
                print('-' * 42)
                print(f'Faturamento do dia: R$ {dia[2]:.2f}')
                print('-' * 42)
                fatu_mes += dia[2]
            print(f'Faturamento do mês: R$ {fatu_mes:.2f}')
            print('-' * 42)
            fatu_mes = 0
        else:
            print('Nada no relatório deste mês.')


def arqui_form(rel):
    with open('relatorio_formatado.txt', 'wt+') as file:
        fatu_mes = 0.0
        for mes, dias_mes in rel.items():
            file.write('=' * 42)
            file.write('\n')
            file.write(f'{mes:^42}')
            file.write('\n')
            file.write('=' * 42)
            file.write('\n')
            if len(dias_mes) > 0:
                for dia in dias_mes:
                    file.write(dia[0])
                    file.write('\n')
                    file.write('-' * 42)
                    file.write('\n')
                    file.write('Veiculo     Quantidade')
                    file.write('\n')
                    file.write('-' * 42)
                    file.write('\n')
                    for vei_quant in dia[1]:
                        p = vei_quant.split(';')
                        file.write(f'{p[0]:<8}     {p[1]:<10}')
                        file.write('\n')
                    file.write('-' * 42)
                    file.write('\n')
                    file.write(f'Faturamento do dia: R$ {dia[2]:.2f}')
                    file.write('\n')
                    fatu_mes += dia[2]
                    file.write('-' * 42)
                    file.write('\n')
                file.write(f'Faturamento do mês: R$ {fatu_mes:.2f}')
                file.write('\n')
                file.write('-' * 42)
                file.write('\n')
                fatu_mes = 0.0
            else:
                file.write('Nada no relatório deste mês.')
                file.write('\n')


def mes_atual(mes, rel):
    arqui_mes(mes=mes, rel=rel)
    fatu_mes = 0.0
    print('=' * 42)
    print(f'{mes:^42}')
    print('=' * 42)
    if len(rel[mes]) > 0:
        for dia in rel[mes]:
            print(dia[0])
            print('-' * 42)
            print('Veículos     Quantidade')
            print('-' * 42)
            for vei_quant in dia[1]:
                p = vei_quant.split(';')
                print(f'{p[0]:<8}     {p[1]:<10}')
            print('-' * 42)
            print(f'Faturamento do dia: R$ {dia[2]:.2f}')
            print('-' * 42)
            fatu_mes += dia[2]
        print(f'Faturamento do mês: R$ {fatu_mes:.2f}')
        print('-' * 42)
    else:
        print('Sem relatorio deste mes ate o momento.')


def arqui_mes(mes, rel):
    fatu_mes = 0
    with open(f'{mes}.txt', 'wt+') as file:
        file.write('=' * 42)
        file.write('\n')
        file.write(f'{mes:^42}')
        file.write('\n')
        file.write('=' * 42)
        file.write('\n')
        if len(rel[mes]) > 0:
            for j in rel[mes]:
                file.write(j[0])
                file.write('\n')
                file.write('-' * 42)
                file.write('\n')
                file.write('Veículos     Quantidade')
                file.write('\n')
                file.write('-' * 42)
                file.write('\n')
                for i in j[1]:
                    p = i.split(';')
                    file.write(f'{p[0]:<8}     {p[1]:<10}')
                    file.write('\n')
                file.write('-' * 42)
                file.write('\n')
                file.write(f'Faturamento do dia: R$ {j[2]:.2f}')
                file.write('\n')
                file.write('-' * 42)
                file.write('\n')
                fatu_mes += j[2]
            file.write(f'Faturamento do mes: R$ {fatu_mes:.2f}')
            file.write('\n')
            file.write('-' * 42)
        else:
            file.write('Sem relatorio deste mes ate o momento.')
            file.write('\n')


def arquivo_principal(lavagem):
    import json
    with open('lavagens.txt', 'wt+') as file:
        lavagem = json.dumps(lavagem, indent=True)
        file.write(lavagem)
