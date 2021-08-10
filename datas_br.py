from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        mes_do_ano = ['janeiro','fevereiro','março','abril',
                      'maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
        mes_cadastro = self.momento_cadastro.month

        return mes_do_ano[mes_cadastro-1]

    def dia_semana(self):
        dia_semana = ['segunda','terça','quarta','quinta','sexta','sabado','domingo']
        dia_cadastro = self.momento_cadastro.weekday()

        return dia_semana[dia_cadastro]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_cadastrado(self):
        tempo_cadastro = datetime.today()  - self.momento_cadastro
        return tempo_cadastro
