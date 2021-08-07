"Usaremos este arquivo para testar as lógicas"
from validate_docbr import CPF,CNPJ
from Cpf_Cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cnpj)
print('')
print(f'CNPJ: {documento}')

documento2 = Documento.cria_documento(exemplo_cpf)
print(f'CPF: {documento2}')

