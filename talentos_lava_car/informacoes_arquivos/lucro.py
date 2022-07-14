def lucro(lavagens, saidas):
    arquivo_lucro(lavagens, saidas)
    for key, value in lavagens.items():
        lucro_in = 0
        for dia in value:
            lucro_in += dia[-1]
        for item in saidas[key].values():
            if isinstance(item, float) or isinstance(item, int):
                lucro_in -= item
                continue
            for i in item.values():
                lucro_in -= i
        print('=' * 42)
        print(f'{key:^42}')
        print('=' * 42)
        print(f'Lucro do mês: R$ {lucro_in:.2f}')
        print('=' * 42)


def arquivo_lucro(lavagens, saidas):
    with open('lucro.txt', 'wt+') as file:
        for key, value in lavagens.items():
            lucro_in = 0
            for dia in value:
                lucro_in += dia[-1]
            for item in saidas[key].values():
                if isinstance(item, float) or isinstance(item, int):
                    lucro_in -= item
                    continue
                for i in item.values():
                    lucro_in -= i
            file.write('=' * 42)
            file.write('\n')
            file.write(f'{key:^42}\n')
            file.write('=' * 42)
            file.write('\n')
            file.write(f'Lucro do mês: R$ {lucro_in:.2f}\n')
            file.write('=' * 42)
            file.write('\n')

