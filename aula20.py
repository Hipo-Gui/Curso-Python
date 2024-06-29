# and == e 
# or == ou
# not == não
# and Todas as condições presisam ser verdadeiras.
# se qualquer valor for considerado Falso, a expressão inteira será avaliada naquele Valor.
# São considerados falsy (0.0)'' False
# também existe o tipo None que é usado para representar um não valor.
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True:

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entra')
else:
    print('Sair')   


# avaliação de curto circuito 
print(True and True and True)
print(bool(' '))