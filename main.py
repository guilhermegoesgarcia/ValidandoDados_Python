"Usaremos este arquivo para testar as lógicas"
from validate_docbr import CPF,CNPJ
from Cpf_Cnpj import Cpf_Cnpj

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

documento = Cpf_Cnpj(exemplo_cnpj,'cnpj')
print('')
print(f'CNPJ: {documento}')

documento2 = Cpf_Cnpj(exemplo_cpf,'cpf')
print(f'CPF: {documento2}')

