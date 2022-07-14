def arquivo_saida(saida):
    saida_formatada(saida)
    import json
    with open('saidas.txt', 'wt+') as file:
        saida = json.dumps(saida, indent=True)
        file.write(saida)


def saida_formatada(saida):
    with open('saidas_formatada.txt', 'wt+') as file:
        for k, v in saida.items():
            total = 0
            file.write(f'{k:^42}\n')
            file.write('=' * 42)
            file.write('\n')
            file.write('Funcionarios:\n')
            for func, sal in v['Funcionarios'].items():
                file.write(f'{func:.<20}R$ {sal:>7.2f}\n')
                total += sal
            file.write('-' * 42)
            file.write('\n')
            file.write(f'Agua/Energia: R$ {v["Agua/Energia"]:.2f}\n')
            total += v['Agua/Energia']
            file.write('-' * 42)
            file.write('\n')
            file.write(f'Materiais: R$ {v["Materiais"]:.2f}\n')
            total += v['Materiais']
            file.write('-' * 42)
            file.write('\n')
            file.write(f'Total de saidas: R$ {total:.2f}\n')
            file.write('=' * 42)
            file.write('\n')


def mostra_saida(saida):
    saida_formatada(saida)
    for k, v in saida.items():
        total = 0
        print(f'{k:^42}')
        print('=' * 42)
        print('Funcionários:')
        for func, sal in v['Funcionarios'].items():
            print(f'{func:.<20}R$ {sal:>7.2f}')
            total += sal
        print('-' * 42)
        print(f'Água/Energia: R$ {v["Agua/Energia"]:.2f}')
        total += v["Agua/Energia"]
        print('-' * 42)
        print(f'Materiais: R$ {v["Materiais"]:.2f}')
        total += v['Materiais']
        print('-' * 42)
        print(f'Total de saídas: R$ {total:.2f}')
        print('=' * 42)
