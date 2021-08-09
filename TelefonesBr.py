import re

class TelefonesBr:
    def __init__(self, telefone):

        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError('Numero Incorreto !')

    def __str__(self):
        return self.formatar()

    def valida(self, telefone):
        padrao = '([0-9]{2,3})([0-9]{2})?([0-9]{4,5})([0-9]{4})'
        resposta = re.findall(padrao, telefone)

        if resposta:
            return True
        else:
            return False

    def formatar(self):
        padrao = '([0-9]{2,3})([0-9]{2})?([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        numero_formatado = '+{} ({}) {}-{}'.format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4))
        return numero_formatado


