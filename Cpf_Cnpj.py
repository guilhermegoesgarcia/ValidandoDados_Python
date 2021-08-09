# Buscando pacote para validação de cpf no site https://pypi.org/
from validate_docbr import CPF,CNPJ

#Modelo Fatory
class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos esta incorreta!!')

class DocCpf:
    def __init__(self,documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('Cpf inválido !!')

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('Cnpj inválido')

    def __str__(self):
        return self.formata()

    def valida(self,documento):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(documento)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



# Abaixo é um modelo de estudo que não esta muito legivel
'''
class Cpf_Cnpj:
    def __init__(self, documento,tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if tipo_documento =='cpf' or tipo_documento == 'CPF':

            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF Invalido!')
        elif tipo_documento == 'cnpj' or tipo_documento == 'CNPJ':

            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ Invalido!')

        else:
            raise ValueError('!! DOCUMENTO INVÁLIDO !!')


    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalido !!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)



# >> Definindo Função para CNPJ

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de Digitos do CNPJ invalido !")

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

# >> definindo o print
    def __str__(self):

        if self.tipo_documento == 'cpf' or self.tipo_documento == 'CPF':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj' or self.tipo_documento == 'CNPJ':
            return self.formata_cnpj() '''