def datas():
    import datetime
    meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', ' Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dias = {'Mon': 'Segunda', 'Tue': 'Terça', 'Wed': 'Quarta', 'Thu': 'Quinta',
            'Fri': 'Sexta', 'Sat': 'Sabado', 'Sun': 'Domingo'}
    data = str(datetime.date.today()).split('-')
    dia_semana = datetime.date(int(data[0]), int(data[1]), int(data[2])).ctime()[0:3]
    mes = int(data[1])
    dia = int(data[2])
    ano = int(data[0])
    return f'{dia} de {meses[mes - 1]} de {ano} - {dias[dia_semana]}'


def veiculo(vei='', quant=0):
    return vei + ';' + str(quant)


def dia_conta(val, veiq):
    return [veiq, sum(val)]
