from acesso_cep import BuscaEndereco

" Arquivo usado para teste da classe 'acesso-cep'"

cep ='01001000'
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(f'bairro:{bairro}, cidade:{cidade}, Estado:{uf}')